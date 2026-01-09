#project 3 is a simple to do list using concepts like lists 
#core idea is to create a list of tasks that can be added to, viewed, and saved to a list 

#fuction to display menu and take user input
def user_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")
    choice = int(input("Choose an option (1-5): "))
    return choice

#defining an empty list to store dictionaries of tasks
tasks = []

#function to add a task to the list
def add_task(tasks):
    task_description = input("Enter your task: ")

    if task_description.strip() != "":
        task = {
            "description": task_description,
            "completed": False
        }
        tasks.append(task)
        print("Task added!")
    else:
        print("Task cannot be empty.")


#function to view tasks in the list
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    
    print("\nYour Tasks:")

    for index, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index + 1}. {task['description']} - {status}")

#function to delete a task from the list
def delete_task(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    
    for index, task in enumerate(tasks):
        print(index + 1, "-", task["description"])
    
    task_index=int(input("enter task number to delete: "))-1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f'Task "{removed_task["description"]}" deleted.')
    else:
        print("Invalid task number.")

    print("task deleted")

#update the status of the task to completed
def mark_task_completed(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    
    for index, task in enumerate(tasks):
        print(index + 1, "-", task["description"])
    
    task_index=int(input("enter task number to mark as completed: "))-1

    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f'Task "{tasks[task_index]["description"]}" marked as completed.')
    else:
        print("Invalid task number.")

#driver code
while True:
   choice=user_menu()
   match choice:
       case 1:
           view_tasks(tasks)
       case 2:
           add_task(tasks)
       case 3:
           delete_task(tasks)
       case 4:
           mark_task_completed(tasks)
       case 5:
           break
       case _:
           print("Invalid choice. Please try again.")