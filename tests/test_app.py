# import os
# import tempfile

import pytest

from fanpi.app import App


@pytest.fixture
def client():
    # db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True

    yield client

    # with flaskr.app.test_client() as client:
    #     with flaskr.app.app_context():
    #         flaskr.init_db()
    #     yield client

    # os.close(db_fd)
    # os.unlink(flaskr.app.config['DATABASE'])

def test_landing_page(client):

    rv = client.get('/')
    assert b'No entries here so far' in rv.data
