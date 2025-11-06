from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}


@app.get("/saludo")
def read_saludo(nombre: str = "Mundo"):
    return {"message": f"Hola, {nombre}"}
