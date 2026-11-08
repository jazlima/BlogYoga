# BlogYoga

Blog de yoga hecho con Django 4.0.4, SQLite y CKEditor.

## Levantar en local con Docker

Requisitos: [Docker Desktop](https://www.docker.com/products/docker-desktop/) (en Windows con backend WSL2).
No hace falta instalar Python.

```powershell
# Construir la imagen y levantar el contenedor
docker compose up --build

# En otra terminal: crear un superusuario o resetear la clave del existente
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py changepassword admin

# Detener
docker compose down
```

Luego abrir:

- Blog: http://localhost:8000/
- Admin: http://localhost:8000/admin/

El `docker-compose.yml` monta la carpeta del proyecto dentro del contenedor, así que
se usan el `db.sqlite3` y las imágenes de `media/` que ya están en el repo, y los
cambios de código se ven en caliente. Si cambiás `requirements.txt`, reconstruí con
`docker compose up --build`.

### Empezar con una base limpia

```powershell
docker compose down
# renombrá o borrá db.sqlite3
docker compose up --build
docker compose exec web python manage.py createsuperuser
```

Después entrá al admin y creá al menos una categoría antes de publicar posts.

> Nota: la configuración (`DEBUG=True`, `SECRET_KEY` en el código) es solo para
> desarrollo local, no para producción.
