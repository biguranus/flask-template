# -*- coding:utf-8 -*-
from flask import request

from src.libs.flask_ import BlueprintRouter, make_ok_resp
from src.libs.exceptions import CabinetNotFound
from src.models.cabinet import CabinetWorkStatistics


bp = BlueprintRouter()


@bp.route("/hello", methods=["GET"], strict_slashes=False)
def hello():
    params = request.args
    print(type(params))
    print(params)
    print(params.get("name"))
    return "hello world"


@bp.route("/info", methods=["GET"], strict_slashes=False)
def get_info():
    """
    test for make_resp
    :return:
    """
    data = {"name": "yqsl"}
    return make_ok_resp(data)


@bp.route("/debug-sentry", methods=["GET"], strict_slashes=False)
def trigger_error():
    """
    test for sentry
    :return:
    """
    division_by_zero = 1 / 0  # noqa


@bp.route("/exception", methods=["GET"], strict_slashes=False)
def test_exception():
    """
    test for exception
    :return:
    """
    raise CabinetNotFound


@bp.route("/cabinet-work-statics", methods=["POST"], strict_slashes=False)
def create_work_statics():
    body = request.json
    print(f"request body: {body}")
    CabinetWorkStatistics.create(
        asset_id=body.get("asset_id"), online_time=body.get("online_time")
    )
    return make_ok_resp()
