import os
import task_storage


args = os.sys.argv


def add_task(task):
    task_id=task_storage.add(task)
    print(f"Task added successfully (ID: {task_id})")

def delete_task(id):
    task_storage.delete(id)

def update_task(id,updated_task):
    task_storage.update(id,updated_task)
    
    
    
    









if __name__ == "__main__":
    
    if "add" in args:
        add_task(args[2])
    elif "delete" in args:
        delete_task(args[2])
    elif "update" in args:
        update_task(args[2],args[3])
        
        