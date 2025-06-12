from dishka import Provider, Scope, provide

from app.application.common.ports.transaction_manager import (
    TransactionManager,
)
from app.infrastructure.adapters.main_transaction_manager_sqla import (
    SqlaMainTransactionManager,
)


class ApplicationProvider(Provider):
    scope = Scope.REQUEST

    # Ports Persistence
    tx_manager = provide(
        source=SqlaMainTransactionManager,
        provides=TransactionManager,
    )
