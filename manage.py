# -*- coding:utf-8 -*-
from flask_script import Manager

from src.app import create_app
from commands.dwd_cron_worker import manager as dwd_cron_manager


manager = Manager(create_app())

manager.add_command("dwd_cron_worker", dwd_cron_manager)


if __name__ == "__main__":
    manager.run()
