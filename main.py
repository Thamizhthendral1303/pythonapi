from fastapi import FastAPI

app = FastAPI()

todolst=[]

@app.post("/inserting")
def adding(task:str):
    todolst.append(task)
    
@app.get("/getting")
def getting():
    return todolst

    