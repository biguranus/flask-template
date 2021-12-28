#! /usr/bin/env bash
set -e

if [[ $1 == "gitlab" ]]; then
    export TEST_DB_URI="mysql+pymysql://root:root@mysql:3306/test_db?charset=utf8mb4"
else
    export TEST_DB_URI="mysql+pymysql://root:root@127.0.0.1:53306/test_db?charset=utf8mb4"
fi

flake8 --max-line-length=120 src commands
coverage erase
py.test -sx tests