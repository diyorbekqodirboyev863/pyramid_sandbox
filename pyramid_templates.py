from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

@view_config(route_name='hello', renderer='templates/hello.jinja2')
def hello(request):
	return {'greet': 'Welcome', 'name': 'Diyorbek Qodirboyev', 'proname': 'Pyramid Sandbox'}

if __name__ == '__main__':
	with Configurator() as cfg:
		cfg.include('pyramid_jinja2')
		cfg.add_static_view(name='static', path='static')
		cfg.add_route('hello', '/welcome')
		cfg.scan()
		app = cfg.make_wsgi_app()
	server = make_server('0.0.0.0', 6543, app)
	server.serve_forever()