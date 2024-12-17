def create_task(tasks: list):
    task_title = input("Ingrese el titulo de la tarea: ")
    task_desc = input("Ingrese la descripcion de la tarea: ")
    task = [task_title, task_desc, False]
    tasks.append(task)

def list_tasks(tasks: list):
    if not tasks:
        print("No hay tareas para mostrar.")
        return
    for i, elem in enumerate(tasks):
        print("<-------------->")
        print(f"ID: {i}")
        print(f"Título: {elem[0]}")
        print(f"Descripción: {elem[1]}")
        print(f"Estado: {'Completada' if elem[2] else 'Pendiente'}")
        print("<-------------->\n")


def mark_task(tasks: list):
    try:
        task_id = int(input("Ingrese el id de la tarea: "))
        tasks[task_id][2] = True
    except IndexError:
        print("Ingrese una id valida")

def clear_tasks(tasks: list):
    tasks[:] = [elem for elem in tasks if elem[2] != True]