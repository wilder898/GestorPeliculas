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

@app.delete("/peliculas/{pelicula_id}")
def eliminar_pelicula(pelicula_id: int):
    for i, p in enumerate(lista_peliculas):
        if p["id"] == pelicula_id:
            pelicula_eliminada = lista_peliculas.pop(i)
            return {"mensaje": "Película eliminada", "pelicula": pelicula_eliminada}
    return {"error": f"Película con ID {pelicula_id} no encontrada"}

# Ejecutar la aplicación
# uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
