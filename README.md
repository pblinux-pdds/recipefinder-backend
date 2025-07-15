# RecipeFinder - Backend

Este es el backend de RecipeFinder, una API construida con Flask y SQLAlchemy para gestionar recetas, ingredientes y categorías.

## Estructura del Proyecto

```
app/
    __init__.py
    models.py
    resources/
        category.py
        ingredient.py
        recipe.py
config.py
run.py
requirements.txt
instance/
    app.db
```

## Instalación

1. **Crea un entorno virtual**  
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Instala las dependencias**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Configura la base de datos**  
   La configuración por defecto usa SQLite y crea `instance/app.db`.

## Uso

Para iniciar el servidor de desarrollo:

```sh
python run.py
```

El servidor estará disponible en `http://127.0.0.1:5000/`.

## Endpoints Principales

- **Categorías**
  - `POST /categories` — Crear una categoría
  - `GET /categories` — Listar todas o buscar por nombre

- **Ingredientes**
  - `POST /ingredients` — Crear un ingrediente
  - `GET /ingredients` — Listar todos

- **Recetas**
  - `POST /recipes` — Crear una receta
  - `GET /recipes` — Listar todas o buscar por nombre

## Estructura de la Base de Datos

- **Recipe**: nombre, descripción, instrucciones, tiempos, porciones, imagen, ingredientes, categorías
- **Ingredient**: nombre
- **Category**: nombre

## Licencia

MIT