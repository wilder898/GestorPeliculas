from fastapi import FastAPI, Body
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

@app.put("/peliculas/{pelicula_id}")
def actualizar_pelicula(pelicula_id: int, request: dict = Body(...)):
    # Validación manual
    if "nombre" not in request or "año" not in request or "director" not in request:
        return {"error": "Faltan campos: nombre, año y director son requeridos"}
    
    nombre = request["nombre"]
    año = request["año"]
    director = request["director"]

    for i, p in enumerate(lista_peliculas):
        if p["id"] == pelicula_id:
            lista_peliculas[i] = {
                "id": pelicula_id,
                "nombre": nombre,
                "año": año,
                "director": director
            }
            return {"mensaje": "Película actualizada", "pelicula": lista_peliculas[i]}
    return {"error": f"Película con ID {pelicula_id} no encontrada"}

# Ejecutar la aplicación
# uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

