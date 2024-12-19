def Selector(name):
    print(f"Hola {name}, ¿en que puedo ayudarte?")
    print("""
        1. Ver lista de tareas pendientes.
        2. Editar tareas.
        3. Gestionar tareas.
        4. Salir
        """)
    option = input()
    return option