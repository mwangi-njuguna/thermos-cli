from . import m

@m.route('/')
def index():
	return '<h1> Hello world </h1>'