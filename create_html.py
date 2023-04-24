import os
#создает файл html с картмаи стадионов
def create_html(dirs):
    with open('a.html', 'r', encoding='utf-8') as f:
        atmp = f.read()
    styles = []
    svgs = []
    for e in dirs:
        if not os.path.exists(e + '/style.css') or not os.path.exists(e + '/svg.html'):
            continue
        styles.append(f'<link rel="stylesheet" href="{e}/style.css">')
        with open(e + '/svg.html', 'r', encoding='utf-8') as f:
            svg = f.read()
        svg = f'<h2>{e}</h2>' + svg    
        svgs.append(svg)

    stxt = "\n".join(styles)    
    vtxt = "\n".join(svgs)
    atmp = atmp.replace('<!--style.css-->', stxt)
    atmp = atmp.replace('<!--svg-->', vtxt)
    with open('arena.html', 'w', encoding='utf-8') as w:
            w.write(atmp)




if __name__ == '__main__':
      dirs = os.listdir()
      print(len(dirs))
      create_html(dirs)
