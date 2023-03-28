# ieb_service_http

servicio desarrollado con Django REST framework para la gestión de los datos de la aplicación ieb_challenge de la empresa IEB.

## Instalación

- Clonar el repositorio
- Crear un entorno virtual
- Instalar las dependencias del proyecto
- copiar el archivo .env.example a .env y configurar las variables de entorno
- Crear la base de datos
- Ejecutar las migraciones
- Crear un superusuario
- correr el comando que carga el cron de la aplicación
- Ejecutar el servidor

```bash
git clone
cd ieb_service_http
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py crontab
manage.py add-superuser
cron
```

## Ejecución

```bash
python manage.py runserver 8001
```

## Ejecución de pruebas

```bash
tox
```
