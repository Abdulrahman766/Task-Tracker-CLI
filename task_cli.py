import os
import task_storage


args = os.sys.argv


def add_task(task):
    task_id=task_storage.add(task)
    print(f"Task added successfully (ID: {task_id})")
    
    
    









if __name__ == "__main__":
    
    if "add" in args:
        add_task(args[2])
        
        