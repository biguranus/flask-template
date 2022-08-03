# -*- coding:utf-8 -*-
from flask import request

from src.libs.logging import logger
from src.libs.flask_ import BlueprintRouter, make_ok_resp


bp = BlueprintRouter()


@bp.route("/responseall", methods=["POST"], strict_slashes=False)
def handle_door_lock_status_callback():
    obj = request.get_data()
    logger.info(f"[callback][dock_lock_status] request body: {obj}")
    return make_ok_resp()


@bp.route("/responseexception", methods=["POST"], strict_slashes=False)
def handle_exception_callback():
    obj = request.get_data()
    logger.info(f"[callback][exception] request body: {obj}")
    return make_ok_resp()


@bp.route("/order", methods=["POST"], strict_slashes=False)
def handle_order_callback():
    obj = request.get_data()
    logger.info(f"[callback][order] request body: {obj}")
    return make_ok_resp()


@bp.route("/freezerDetail", methods=["POST"], strict_slashes=False)
def handle_online_callback():
    obj = request.get_data()
    logger.info(f"[callback][online] request body: {obj}")
    return make_ok_resp()
