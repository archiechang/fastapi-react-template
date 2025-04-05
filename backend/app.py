import uvicorn
from src import create_app

app = create_app()


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8100, reload=True)
