# -*- coding:utf-8 -*-
import datetime as dt

from flask.json import JSONEncoder as _JSONEncoder, jsonify
from flask.views import MethodView


def make_ok_resp(data=None, **kwargs):
    resp = {"code": 0, "message": "request succeed", "data": data}
    resp.update(kwargs)
    return jsonify(resp)


def is_subclass(obj, cls):
    try:
        return issubclass(obj, cls)
    except TypeError:
        return False


class BlueprintRouter:
    def __init__(self, url_prefix=None):
        self.url_prefix = url_prefix
        self.deferred = []

    def route(self, rule, **options):
        def wrapper(f):
            if is_subclass(f, MethodView):
                view_f = f.as_view(f.__name__)
            else:
                view_f = f
            self.deferred.append((view_f, rule, options))
            return f

        return wrapper

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = self.url_prefix

        if url_prefix is None:
            raise RuntimeError("url_prefix can not be None")

        for f, rule, options in self.deferred:
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)


class JSONEncoder(_JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dt.datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%SZ")
        return super(JSONEncoder, self).default(obj)
