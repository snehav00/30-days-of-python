print("==== TO-DO LIST ====\n")

all_tasks = []

def add_task(all_tasks):
    task = input("Enter task to add: ")
    new_task = {"task": task, "done": False}
    all_tasks.append(new_task)

def display(all_tasks):
    for i, item in enumerate(all_tasks):
        if item['done']:
            print(f"Task {i+1}: {item['task']} \u2713")
        else:    
            print(f"Task {i+1}: {item['task']}")


add_task(all_tasks)
display(all_tasks)