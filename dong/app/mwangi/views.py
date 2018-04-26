from . import mwangi

@mwangi.route('/')
def index():
	return '<h1> Hello world </h1>'