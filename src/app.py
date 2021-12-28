# -*- coding:utf-8 -*-
import json
import uuid

from flask import Flask, request, jsonify
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from src.controllers import init_routes
from src.libs.flask_ import JSONEncoder
from src.models import db
from src.config import SENTRY_DSN, SENTRY_TRACES_SAMPLE_RATE, ENVIRONMENT
from src.libs.exceptions import APIException
from src.libs.logging import logger


def create_app(config=None):
    app = Flask(__name__)
    config_app(app, config)
    app.json_encoder = JSONEncoder
    db.init_app(app)

    if not (app.testing or app.debug):
        sentry_sdk.init(
            dsn=SENTRY_DSN,
            environment=ENVIRONMENT,
            integrations=[FlaskIntegration()],
            traces_sample_rate=SENTRY_TRACES_SAMPLE_RATE,
        )

    init_routes(app)

    @app.before_request
    def init_request():
        request_id = request.headers.get("request_id", str(uuid.uuid1()))
        request.headers.request_id = request_id

        if request.endpoint == "ping":
            return
        logger.info("before_request")

    @app.errorhandler(APIException)
    def handle_error(e):
        resp = {
            "code": e.error_code,
            "message": e.message,
        }
        logger.error(f"[exception]|request_id:{request.headers.request_id}|resp={resp}")
        return jsonify(resp), e.http_code

    @app.after_request
    def add_extra_info(resp):
        obj = resp.get_json()
        if isinstance(obj, dict):
            obj["request_id"] = request.headers.request_id
            resp.set_data(json.dumps(obj))
        return resp

    return app


def config_app(app, config):
    app.config.from_object("src.config")
    if config is not None and isinstance(config, dict):
        app.config.update(config)
