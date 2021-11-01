# loki-grafana-demo-app
The app demonstrating various log formats.

Don't forget `pip install`.
Run `uvicorn main:app --reload` for dev server.

Automatically generated docs available on `/docs` or `/redoc`, raw schema on `/openapi.json`.

## Docker

- `./docker/build.sh`
- `docker run -p 8000:8000 logger-demo-app-local`

### Docker system prune

- `sudo docker system prune -a`
