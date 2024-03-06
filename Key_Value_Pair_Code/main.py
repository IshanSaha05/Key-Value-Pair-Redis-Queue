# Importing all the neccessary packages.
from huey_tasks import readTask, createTask, updateTask, deleteTask, huey
from fastapi import FastAPI
import uvicorn
from models import pair, val    

# Declares the api.
app = FastAPI()

# Route to read existing key-value pair.
@app.get("/api/record/{key}")
def read(key: str):
    # Makes the task and enqueues it.
    task = readTask.s(key)
    result = huey.enqueue(task)
    
    # Returns the respond from task.
    response = dict(result.get(blocking=True))
    return response

# Route to create new key-value pair.
@app.post("/api/record")
def create(record: pair):
    # Makes the task and enqueues it.
    task = createTask.s(record)
    result = huey.enqueue(task)
    
    # Returns the respond from task.
    response = dict(result.get(blocking=True))
    return response

# Route to update existing key-value pair.
@app.put("/api/record/{key}")
def update(key: str, value: val):
    # Makes the task and enqueues it.
    task = updateTask.s(key, value)
    result = huey.enqueue(task)
    
    # Returns the respond from task.
    response = dict(result.get(blocking=True))
    return response

# Route to delete existing key-value pair.
@app.delete("/api/record/{key}")
def delete(key: str):
    # Makes the task and enqueues it.
    task = deleteTask.s(key)
    result = huey.enqueue(task)
    
    # Returns the respond from task.
    response = dict(result.get(blocking=True))
    return response
        
# Runs the server using uvicorn.
if __name__ == '__main__':
    uvicorn.run(app, host = '0.0.0.0', port = 8000)