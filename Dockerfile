FROM ludotech/python3.9-poetry

LABEL maintainer="litian01@yuanqisenlin.com"
RUN mkdir "/code"
WORKDIR /code
COPY requirements.txt .
COPY deploy-requirements.txt .

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN pip install -r deploy-requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

COPY ./ .
CMD ["gunicorn", "-k", "gevent", "-c", "gunicorn_conf.py", "wsgi:app"]