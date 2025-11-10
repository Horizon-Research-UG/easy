# Easy Backend

FastAPI service exposing the core platform API. The service is engineered for modular growth via an opt-in plugin registry located under `backend.plugins`.

## Local development

```bash
poetry install
poetry run backend-api
```

## Testing

```bash
poetry run pytest
```
