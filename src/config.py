# -*- coding:utf-8 -*-
import os

env = os.getenv

ENVIRONMENT = env("ENVIRONMENT", "dev")
DEBUG = env("DEBUG", "False").lower() == "true"

# aliyun account
ALIYUN_ACCESS_KEY_ID = env("ALIYUN_ACCESS_KEY_ID")
ALIYUN_ACCESS_KEY_SECRET = env("ALIYUN_ACCESS_KEY_SECRET")

ALIYUN_OSS_ENDPOINT = env("ALIYUN_OSS_POINT")
ALIYUN_OSS_PUBLIC_ENDPOINT = env("ALIYUN_OSS_PUBLIC_POINT")
ALIYUN_OSS_BUCKET = env("ALIYUN_OSS_BUCKET", "")
ALIYUN_OSS_KEY_PREFIX = env("ALIYUN_OSS_KEY_PREFIX", "")

ALIYUN_IOT_REGION_ID = env("ALIYUN_IOT_REGION_ID", "cn-shenzhen")

# MySQL
SQLALCHEMY_DATABASE_URI = env("SQLALCHEMY_DATABASE_URI", "sqlite://")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_size": int(env("pool_size", 200)),
    "pool_recycle": int(env("pool_recycle", 3600)),
    "pool_timeout": int(env("pool_timeout", 180)),
}

# Redis
REDIS_URI = env("REDIS_URI", "/tmp/redis.db")

# MongoDB
MONGODB_URI = env("MONGODB_URI")

# Sentry_DSN    SDK: https://docs.sentry.io/platforms/python/
SENTRY_DSN = env(
    "SENTRY_DSN", "https://8ad93808791048d08f88efbd9378de17@sentry.yqslmall.com/6"
)
SENTRY_TRACES_SAMPLE_RATE = float(env("SENTRY_TRACES_SAMPLE_RATE", 1.0))
