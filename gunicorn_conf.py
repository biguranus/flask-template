# RTFM -> http://docs.gunicorn.org/en/latest/settings.html#settings
import os

bind = "0.0.0.0:8080"
workers = os.cpu_count() * 2 + 1

timeout = 300

max_requests = 2000
max_requests_jitter = 500

proc_name = "cabinet_iot_service"
