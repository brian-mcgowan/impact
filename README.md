# Impact

Log accomplishments, track impact, and draft promotion narratives

## Development

Install development dependencies:

```shell
poetry install --with dev
```

### Testing

Run the test suite:

```shell
poetry run pytest
```

Check code coverage:

```shell
poetry run pytest --cov
```

Generate a browsable coverage report:

```shell
poetry run pytest --cov --cov-report html
```

### Linting

Run linter:

```shell
poetry run flake8
```

> Code formatting errors can usually be fixed by running `black`:
>
> ```shell
> poetry run black src/
> ```
