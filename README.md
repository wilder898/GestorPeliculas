# API de Películas

Esta API permite gestionar un catálogo de películas. Puedes listar, registrar, consultar, actualizar y eliminar películas mediante endpoints RESTful.

---

## Instrucciones de ejecución

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/api-peliculas.git
   cd api-peliculas

2. **Instala las dependencias desde**
   ```bash
   pip install -r requirements.txt

3. **Ejecuta el servidor**
   ```bash
   cd 
   uvicorn main:app --reload

---

## Endpoints disponibles

### 1. Listar todas las películas
- **Método:** `GET`
- **Ruta:** `/peliculas`
- **Descripción:** Retorna una lista con todas las películas registradas.
- **Respuesta de ejemplo:**
  ```json
  {
    "id": 1,
    "nombre": "Avatar",
    "año": 2012,
    "director": "James Cameron"
  }
  
### 2. Registrar nueva película
- **Método:** `POST`
- **Ruta:** `/peliculas`
- **Descripción:** Crea una nueva película con los datos proporcionados.
- **Cuerpo esperado:**
  ```json
  {
    "nombre": "Avatar",
    "año": 2012,
    "director": "James Cameron"
  }
  
- **Respuesta de ejemplo:**
  ```json
  {
    "id": 2,
    "nombre": "Sueño de fuga",
    "año": 1994,
    "director": "Frank Darabont"
  }

### 3. Obtener película por ID
- **Método:** `GET`
- **Ruta:** `/peliculas/{pelicula_id}`
- **Descripción:** Retorna los datos de la película con el ID especificado.
- **Respuesta de ejemplo:**
  ```json
  {
    "id": 1,
    "nombre": "Avatar",
    "año": 2012,
    "director": "James Cameron"
  }

### 4. Actualizar información de una película
- **Método:** `PUT`
- **Ruta:** `/peliculas/{pelicula_id}`
- **Descripción:** Actualiza uno o más campos de la película con el ID especificado.
- **Cuerpo esperado:**
  ```json
  {
    "nombre": "Avatar 2",
    "año": 2022,
    "director": "James Cameron"
  }

- **Respuesta de ejemplo:**
  ```json
  {
    "mensaje": "Película actualizada",
    "pelicula": {
      "id": 1,
      "nombre": "Avatar 2",
      "año": 2022,
      "director": "James Cameron"
    }
  }

### 5. Eliminar película
- **Método:** `DELETE`
- **Ruta:** `/peliculas/{pelicula_id}`
- **Descripción:** Elimina la película con el ID especificado.
- **Respuesta de ejemplo:**
  ```json
  {
    "mensaje": "Película eliminada",
    "pelicula": {
      "id": 1,
      "nombre": "Avatar",
      "año": 2012,
      "director": "James Cameron"
    }
  }