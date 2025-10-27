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

@app.get("/peliculas/{pelicula_id}")
def obtener_por_id(pelicula_id: int):
    for pelicula in lista_peliculas:
        if pelicula["id"] == pelicula_id:
            return {"pelicula": pelicula}
    return {"mensaje": f"No existe pelicula con el id {pelicula_id}"}

# Ejecutar la aplicación
# uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
