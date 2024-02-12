# Mystic Archive

`litestar run`

## Alembic Migrations

### create a migration

```
alembic revision --autogenerate -m "Init"
```

### upgrade

```
alembic upgrade head
```