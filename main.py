import logging
import webapp2
from webapp2_extras import routes

def handle_404(request, response, exception):
    """Return a custom 404 error response."""
    response.write('Not Found')
    response.set_status(404)

def handle_500(request, response, exception):
    """Return a custom 500 error response."""
    logging.exception(exception)
    response.write('Internal Server Error')
    response.set_status(500)

app = webapp2.WSGIApplication([('/', 'handlers.EditorPage'),
                               ('/editor', 'handlers.EditorPage'),
                               ('/turtle', 'handlers.TurtlePage'),
                               ('/shell', 'handlers.ShellPage')], debug=True)

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
