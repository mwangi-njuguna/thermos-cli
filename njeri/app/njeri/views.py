from . import njeri

@njeri.route('/')
def index():
	return '<h1> Hello world </h1>'