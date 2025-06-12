from collections.abc import Iterable

from dishka import Provider

from app.setup.ioc.di_providers.settings import SettingsProvider


def get_providers() -> Iterable[Provider]:
    return (SettingsProvider(),)
