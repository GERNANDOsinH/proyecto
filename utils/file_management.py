def read_task_file():
    dir = input("Ingrese la direccion de las tareas: ")
    tasks = []
    with open(dir, "r") as file:
        for line in file:
            elem = line.split(";")
            tasks.append(elem)
    return tasks

def save_in_a_task_file(tasks: list):
    dir = input("Ingrese la direccion de las tareas: ")
    with open(dir, "w") as file:
        for elem in tasks:
            task = f"{elem[0]};{elem[1]};{elem[2]}\n"
            file.write(task)