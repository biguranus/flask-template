# -*- coding:utf-8 -*-
from flask import request

from src.libs.logging import logger
from src.libs.flask_ import BlueprintRouter, make_ok_resp


bp = BlueprintRouter()


@bp.route("/", methods=["POST"], strict_slashes=False)
def callback():
    obj = request.get_data()
    logger.info(f"[callback] request body: {obj}")
    return make_ok_resp()
