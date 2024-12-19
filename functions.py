def read_list(path):
    db=open(path)
    i=db.readline()
    tareas={}
    x=0
    while (x < int(i)):
        tareas[db.readline]=db.readline
        print(tareas)
        x+=1
    db.close