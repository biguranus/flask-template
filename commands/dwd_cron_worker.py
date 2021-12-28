# -*- coding:utf-8 -*-
import os
import time

import schedule
from flask_script import Manager

from src.libs.logging import logger

CRON_TIME = os.getenv("CRON_TIME", "02:00")

manager = Manager(description="sync pull data from dwd")


def sync_data():
    logger.info("sync data")
    pass


@manager.command
def start():
    logger.info("Start sync pull data ...")
    schedule.every().day.at(CRON_TIME).do(sync_data)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # convenience for local run
    sync_data()
