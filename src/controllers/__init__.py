# -*- coding:utf-8 -*-
from flask import Blueprint, Markup

from src.controllers import api, callback, yuanqi_go_callback

bp = Blueprint("api_v1", __name__)


def init_routes(app):
    api.bp.register(bp, "/")
    callback.bp.register(bp, "/v1/callback")
    yuanqi_go_callback.bp.register(bp, "/gos-infrastructure/thirdpart/callback/fbbzy")

    @app.route("/ping")
    def ping():
        return Markup("pong")

    app.register_blueprint(bp, url_prefix="/api")

    return app
