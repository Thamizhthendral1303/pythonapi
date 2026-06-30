from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# List to store tasks
todolst = []


# Model for input
class Todo(BaseModel):
    task: str


# Home API
@app.get("/")
def home():
    return {"message": "Welcome to Todo API"}


# Insert Task
@app.post("/insert")
def add_task(todo: Todo):

    data = {
        "id": len(todolst) + 1,
        "task": todo.task,
        "status": "Pending"
    }

    todolst.append(data)

    return {
        "message": "Task Added Successfully",
        "data": data
    }


# View All Tasks
@app.get("/view")
def view_tasks():

    if len(todolst) == 0:
        return {"message": "No Tasks Found"}

    return {
        "total_tasks": len(todolst),
        "tasks": todolst
    }


# Update Task
@app.put("/update/{task_id}")
def update_task(task_id: int, todo: Todo):

    for task in todolst:

        if task["id"] == task_id:
            task["task"] = todo.task
            task["status"] = todo.status

            return {
                "message": "Task Updated Successfully",
                "updated_task": task
            }

    raise HTTPException(status_code=404, detail="Task Not Found")


# Delete Task
@app.delete("/delete/{task_id}")
def delete_task(task_id: int):

    for task in todolst:

        if task["id"] == task_id:
            todolst.remove(task)

            return {
                "message": "Task Deleted Successfully",
                "deleted_task": task
            }

    raise HTTPException(status_code=404, detail="Task Not Found")
