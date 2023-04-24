import re
import requests
import json
import os


#возвращает уникальный список стадионов по текущим продажам билетов
def getlist():
    stnames = set(os.listdir())
    #stnames = set()
    stadiums = []
    #все комманды
    all_teams_url = 'https://www.footballticketpad.com/teams' 
    t_data = requests.get(all_teams_url).text

    templ = r'<a href="/group/club/(.*?)" class="inner">'
    tmp_game = r'<script type="application/ld\+json">(.*?)</script>'

    res_team = re.findall(templ, t_data)
    for e in res_team:
        #перебираем футбольные комманды
        try:
            url1 = "https://www.footballticketpad.com/group/club/" + e 
            txt_url1 = requests.get(url1).text
            games = re.findall(tmp_game, txt_url1)
            for g in games:
                try:
                    jgame = json.loads(g)
                    if jgame['@graph']['location'] == "N/A":
                        continue
                    urlgame = jgame['@graph']['url']
                    stad_name = jgame['@graph']['location']['name'].replace(" ", "_").replace("'", "")
                    stad_adress = ", ".join(jgame['@graph']['location']['address'].values())
                    if urlgame.find('club//') > -1:
                        continue
                    if stad_name in stnames:
                        #эта арена уже есть в списке
                        continue
                    stnames.add(stad_name)
                    stadiums.append(stad_name + ';' + stad_adress + ';' + urlgame)
                except Exception as er:
                    print(er)

        except Exception as er:
                    print(er)
                  
                  
    return  stadiums               


if __name__ == "__main__":
    stadi = getlist()
    alls = "\n".join(stadi)
    with open('list_area.txt', 'w', encoding='utf-8') as w:
            w.write(alls)

