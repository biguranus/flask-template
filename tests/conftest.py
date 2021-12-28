# -*- coding:utf-8 -*-
import os

import pytest

from src.app import create_app
from src.models import db


@pytest.fixture()
def app():
    app = create_app(
        {
            "SQLALCHEMY_DATABASE_URI": os.getenv("TEST_DB_URI", "sqlite://"),
            "TESTING": True,
        }
    )

    with app.app_context():
        db.init_app(app)
        db.create_all()
        yield app
