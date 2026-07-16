import json

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
            

def add(task):

    id = len(json_data)+1
    json_data[id] = task
    write_tasks(json_data)

    return id
    




