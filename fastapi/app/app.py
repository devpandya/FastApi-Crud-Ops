from fastapi import FastAPI

app = FastAPI()

@app.get("/",tags=['ROOT'])
async def root() -> dict:
    return {"Ping":"pong"}


@app.get('/todo',tags=['ToDo'])
async def get_todo() -> dict:
    return {"data":todos}

@app.post('/todo',tags=['ToDo'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {"data":"Post Successfull"}

@app.put('/todo/{id}',tags=['ToDo'])
async def update_todo(id:int,body:dict) -> dict:
    for todo in todos:
        if(int(todo['id']) == id):
            todo['Activity']= body['Activity']
            return {
                "data": f"Todo with id {id} has been updated"
            }
    return {"data":f"Todo with id {id} not found"}

@app.delete('/todo/{id}',tags=['ToDo'])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if(int(todo['id']) == id):
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been deleted"
            }
    return {"data":f"Todo with id {id} not found"}


todos=[{"id":1,"Activity":"Jogging"},
{
    "id":2,
    "Activity":"Writng"
}]