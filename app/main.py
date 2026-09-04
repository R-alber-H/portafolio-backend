from fastapi import FastAPI

app = FastAPI(title="Portafolio API")

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando"}
