import json
from tabulate import tabulate
from datetime import datetime


file="data.json"
json_data = {}


try: 
    with open(file , "r",encoding="utf-8") as f:
        json_data = json.load(f)

except Exception as e:
        print(e)
             
            
            
    

def write_tasks(tasks_entry):

    try:
        with open(file , "w") as f:
             json.dump(tasks_entry,f,indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)


def save_changes():

    try:
        with open(file , "w") as f:
             json.dump(json_data,f,indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)
            

def add(task):

    id = len(json_data)+1
    date_time=datetime.now()
    json_data[id] = [task,date_time.strftime("%d-%M-%Y %H:%M:%S %p")]
    write_tasks(json_data)

    return id

def update(id,updated_task):
    date_time=datetime.now()
    json_data[id] = [updated_task,date_time.strftime("%d-%M-%Y %H:%M:%S %p")]
    write_tasks(json_data)



def delete(id):
    del json_data[id] 
    write_tasks(json_data)


def in_progress(id):
    json_data[id].append("in progress")
    write_tasks(json_data)


def is_done(id):
    if "in progress" in json_data[id]:
        json_data[id].remove("in progress")
        json_data[id].append("done")
    else:
         print("Error: the task has to be marked as \"in progress\" before you marke it as \"done\". ")
    write_tasks(json_data)

def list():
   

    task_list={
        "id":[],
        "todo":[],
        "in progress":[],
        "done":[],
        "date-time":[]

    }

    for k,v in json_data.items():
        if "in progress" in v:
            task_list["id"].append(k)
            task_list["todo"].append("")
            task_list["done"].append("")
            task_list["in progress"].append(v[0])
            task_list["date-time"].append(v[1])
        
            
        elif "done" in v:
                    task_list["id"].append(k)
                    task_list["todo"].append("")
                    task_list["in progress"].append("")
                    task_list["done"].append(v[0])
                    task_list["date-time"].append(v[1])
        else:
             task_list["id"].append(k)
             task_list["todo"].append(v[0])
             task_list["date-time"].append(v[1])
             
    print(tabulate(task_list,headers="keys",tablefmt="grid"))


   
    




    
    




