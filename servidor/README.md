# Servidor

## Pasos para configurar base de datos

1. Instalar flask-sqlalchemy
```
pip install flask-sqlalchemy
```

2. Instalar flask-migrate
```
pip install flask-migrate
```

3. Crear la migración inicial (sólo correr si la carpeta *migrations* no existe)
```
flask db init
```

4. Realizar la migración de la base de datos (sólo hace algo si existen migraciones pendientes)
```
flask db migrate
```

5. Actualizar la DB

The flask db migrate command does not make any changes to the database, it just generates the migration script. To apply the changes to the database, the flask db upgrade command must be used.
```
flask db upgrade
```

## Pasos para crear/almacenar un modelo

```python
from models import Respuesta
r = Respuesta(pregunta=1, respuesta=2)
db.session.add(r)
db.session.commit()
```

## Trabajar con formularios

1. Instalar flask-wtf
```
pip install flask-wtf
```
