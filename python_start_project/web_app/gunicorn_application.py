from flask import Flask
from gunicorn.app.base import BaseApplication

from python_start_project.web_app.flask_application import FlaskApplication


class GunicornApplication(BaseApplication):

    def __init__(self, app: Flask, flask_application: FlaskApplication):
        self.app = app
        self.host = flask_application.get_host()
        self.port = flask_application.get_port()
        self.workers = flask_application.get_workers()
        super().__init__()

    def load_config(self):
        self.cfg.set("bind", f"{self.host}:{self.port}")
        self.cfg.set("workers", self.workers)
        self.cfg.set("worker_class", "gevent")
        self.cfg.set("accesslog", "-")
        self.cfg.set("errorlog", "-")
        '''
        self.cfg.set(
            "access_log_format",
            '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
            # 127.0.0.1 - - [13/Oct/2023:10:45:12 +0300] "POST /post HTTP/1.1" 200 21 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
            # Our format: '%(asctime)s.%(msecs)03d [%(h)s] [%(threadName)s] %(levelname)s %(name)s - %(message)s %(r)s %(H)s %(U)s'
        )
        '''

    def load(self):
        return self.app
