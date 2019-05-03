import falcon
from prometheus_client import Counter
from prometheus_client import generate_latest
from werkzeug.serving import run_simple

REQUESTS = Counter('hello_worlds_total', 'Hello Worlds requested.')

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080
PROMETHEUS_PORT = 8081


class RootResource(object):
    def on_get(self, req, resp):
        REQUESTS.inc()
        resp.body = "Hello World"
        resp.status = falcon.HTTP_200


class PrometheusResource(object):
    def on_get(self, req, resp):
        data = generate_latest()
        resp.content_type = 'text/plain; version=0.0.4; charset=utf-8'
        resp.body = str(data.decode('utf-8'))


app = falcon.API()
app.add_route('/', RootResource())
app.add_route('/metrics', PrometheusResource())

if __name__ == "__main__":
    run_simple(SERVER_HOST, SERVER_PORT, app, use_reloader=True, use_debugger=True)
