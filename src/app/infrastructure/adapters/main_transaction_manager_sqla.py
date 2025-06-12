import logging

from sqlalchemy.exc import SQLAlchemyError

from app.application.common.ports.transaction_manager import (
    TransactionManager,
)
from app.infrastructure.adapters.types import MainAsyncSession
from app.infrastructure.constants import (
    DB_COMMIT_DONE,
    DB_COMMIT_FAILED,
    DB_FLUSH_DONE,
    DB_FLUSH_FAILED,
    DB_QUERY_FAILED,
)
from app.infrastructure.exceptions.gateway import DataMapperError

log = logging.getLogger(__name__)


class SqlaMainTransactionManager(TransactionManager):
    def __init__(self, session: MainAsyncSession):
        self._session = session

    async def flush(self) -> None:
        """
        :raises DataMapperError:
        :raises UsernameAlreadyExists:
        """
        try:
            await self._session.flush()
            log.debug("%s Main session.", DB_FLUSH_DONE)

        except SQLAlchemyError as error:
            raise DataMapperError(f"{DB_QUERY_FAILED} {DB_FLUSH_FAILED}") from error

    async def commit(self) -> None:
        """
        :raises DataMapperError:
        """
        try:
            await self._session.commit()
            log.debug("%s Main session.", DB_COMMIT_DONE)

        except SQLAlchemyError as error:
            raise DataMapperError(f"{DB_QUERY_FAILED} {DB_COMMIT_FAILED}") from error
