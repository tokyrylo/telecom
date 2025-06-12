from dishka import Provider, Scope, from_context, provide

from app.infrastructure.persistence_sqla.config import PostgresDsn, SqlaEngineConfig
from app.setup.config.settings import AppSettings


class SettingsProvider(Provider):
    scope = Scope.APP

    settings = from_context(provides=AppSettings)

    @provide
    def provide_postgres_dsn(self, settings: AppSettings) -> PostgresDsn:
        return PostgresDsn(settings.postgres.dsn)

    @provide
    def provide_sqla_engine_config(self, settings: AppSettings) -> SqlaEngineConfig:
        return SqlaEngineConfig(**settings.sqla.model_dump())
