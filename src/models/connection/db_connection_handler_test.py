import pytest
from .db_connection_handler import DbConnectionHandler


@pytest.mark.skip(reason="Integration with Db")
def test_db_connection_handler():
    db_conn_handler = DbConnectionHandler()

    assert db_conn_handler.session is None

    with db_conn_handler:
        assert db_conn_handler.session is not None
