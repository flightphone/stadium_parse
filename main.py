import os
from get_stadium_list import getlist
from save_svg import parse_svg
from create_html import create_html

stadiums = getlist()  #список
parse_svg(stadiums)  #сохраняем
create_html(os.listdir()) #генерируем arena.html
