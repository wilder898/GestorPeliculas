from fastapi import FastAPI
import uvicorn

# Crear la instancia de FastAPI
app = FastAPI()

# Lista de peliculas

lista_peliculas = [
    {"id": 1, "nombre": "Avatar", "año": 2012, "director": "James Cameron" },
]

contador_id = 2

@app.get("/")
def root():
    return {"mensaje": "¡Bienvenido a mi API con FastAPI!"}

@app.get("/peliculas")
def listar_peliculas():
    return {"peliculas": lista_peliculas}

# Ejecutar la aplicación
# uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

