from fastapi import FastAPI

from src.routes import contacts

app = FastAPI()

app.include_router(contacts.router, prefix='/api')



@app.get("/api")
def read_root():
    return {'message': 'Text'}
