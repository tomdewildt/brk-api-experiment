# BRK API Experiment
[![License](https://img.shields.io/github/license/tomdewildt/brk-api-experiment)](https://github.com/tomdewildt/brk-api-experiment/blob/master/LICENSE)

Experiment with the [BRK](https://api.kadastralekaart.com/public/v1/docs/) (Kadaster) API using [FastAPI](https://fastapi.tiangolo.com/).

# How To Run

Prerequisites:
* mise version ```2025.1.0``` or later
* uv version ```0.6.0``` or later
* python version ```3.12.0``` or later

### Development

1. Run ```mise run init``` to initialize the environment.
2. Copy ```.env.example``` to ```.env``` and configure the settings.
3. Run ```mise run start``` to start the API server.

# References

[Kadaster BRK Docs](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brk)

[PDOK Locatieserver Docs](https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/)

[KadastraleKaart.com API Docs](https://api.kadastralekaart.com/public/v1/docs/)

[FastAPI Docs](https://fastapi.tiangolo.com/)

[Pydantic Docs](https://docs.pydantic.dev/)

[Pydantic Settings Docs](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

[HTTPX Docs](https://www.python-httpx.org/)

[Loguru Docs](https://loguru.readthedocs.io/)
