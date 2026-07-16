import os
import task_storage


args = os.sys.argv


def add_task(task):
    task_id=task_storage.add(task)
    print(f"Task added successfully (ID: {task_id})")

def delete_task(id):
    task_id=task_storage.delete(id)
    
    
    
    









if __name__ == "__main__":
    
    if "add" in args:
        add_task(args[2])
    elif "delete" in args:
        delete_task(args[2])
        
        