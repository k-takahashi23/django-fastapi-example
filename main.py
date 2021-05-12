from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def users():
    return {"users": [
        {
            "id": "id1",
            "name": "Tanaka Taro"
        },
        {
            "id": "id2",
            "name": "Tanaka Jiro"
        }
    ]}