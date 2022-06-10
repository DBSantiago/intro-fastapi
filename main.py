from fastapi import FastAPI

app = FastAPI(title="Movie Reviews", description="In this project we'll be able to review movies", version="1")


@app.on_event("startup")
def startup():
    print("Server is starting up...")


@app.on_event("shutdown")
def shutdown():
    print("Server is shutting down...")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
