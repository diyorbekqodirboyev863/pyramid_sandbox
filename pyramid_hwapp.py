from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
	return Response('Hello World!')

if __name__ == '__main__':
	with Configurator() as cfg:
		cfg.add_route('hello', '/')
		cfg.add_view(hello_world, route_name='hello')
		app = cfg.make_wsgi_app()
	server = make_server('0.0.0.0', 6543, app)
	server.serve_forever()
