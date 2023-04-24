import re
import requests
import json
import os

#сохраняет карты стадионов по папкам на основе списка stadiums
def parse_svg(stadiums):
    tmp_style = r'href="(.*?)/style.css"'
    tmp_svg = r'''<div class="stadium-map">(.|\n)*?<svg(.*?)</svg>'''
    for e in stadiums:
        try:
            e = e.replace('\n', '')
            fld = e.split(";")
            sname = fld[0]
            # if os.path.exists(sname):
            #     continue
            
            surl = fld[2]
            stxt = requests.get(surl).text
            
            res = re.findall(tmp_svg, stxt)
            if len(res) == 0:
                continue

            svg_text = f'<svg width="600" height="400" id="{sname}"' + res[0][1] + '</svg>'
            
            sty_url = re.findall(tmp_style, stxt)
            if len(sty_url) == 0:
                continue
            sty_url = "https://www.footballticketpad.com" + sty_url[0] + "/style.css"
            sty_text = requests.get(sty_url).text

            if not os.path.exists(sname):
                os.mkdir(sname)

            with open(sname + "/style.css", "w", encoding="utf-8") as w:
                w.write(sty_text)

            with open(sname + "/svg.html", "w", encoding="utf-8") as w:
                w.write(svg_text)
        except Exception as ex:
            print(ex)

        


if __name__ == "__main__":
    with open('list_area.txt', 'r', encoding='utf-8') as f:
        stadi = f.readlines()
        parse_svg(stadi)
