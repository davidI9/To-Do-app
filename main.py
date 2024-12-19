from menus import Selector
from settings import name, path
import functions

option=0
tareas={}
while option!="4":
    option=Selector(name)
    if (option == 1):
        tareas=functions.read_list(path)