print("==== TO-DO LIST ====\n")

all_tasks = []

def add_task(all_tasks):
    task = input("Enter task to add: ")
    new_task = {"task": task, "done": False}
    all_tasks.append(new_task)
    return all_tasks

