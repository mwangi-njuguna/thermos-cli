from flask import render_template
from . import m

@m.app_errorhandler(404)
def four_Ow_four(error):
	'''
	Function to render the 404 error page
	'''
	return render_template('fourOwfour.html'),404