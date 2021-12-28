# -*- coding:utf-8 -*-
from src.libs.exceptions import CABINET_NOT_FOUND


class TestGetInfo:
    def test_200_when_get_info(self, test_client):
        resp = test_client.get("/api/v1/info")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["data"]["name"] == "yqsl"


def test_get_info(test_client):
    resp = test_client.get("/api/v1/info")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["data"]["name"] == "yqsl"


def test_exception(test_client):
    resp = test_client.get("/api/v1/exception")
    assert resp.status_code == 404
    data = resp.get_json()
    assert data["code"] == CABINET_NOT_FOUND
