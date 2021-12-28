# -*- coding:utf-8 -*-
import json

import pytest
from flask import Response


class APIResponse(Response):
    def get_json(self):
        return json.loads(self.data)


@pytest.fixture()
def test_client(app):
    app.response_class = APIResponse
    return app.test_client()
