from utils import file_management, task_controller

def task_management():
    tasks = []
    oper = ""
    while oper != "STOP":
        oper = input("Ingrese la operacion: ")
        if oper == "INSERT":
            task_controller.create_task(tasks)
        elif oper == "PRINT":
            task_controller.list_tasks(tasks)
        elif oper == "MARK TASK":
            task_controller.mark_task(tasks)
        elif oper == "CLEAR LIST":
            task_controller.clear_tasks(tasks)
        elif oper == "READ":
            tasks = file_management.read_task_file()
        elif oper == "SAVE":
            file_management.save_in_a_task_file(tasks)

task_management()