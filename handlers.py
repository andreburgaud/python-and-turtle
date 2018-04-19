import os

import jinja2
import webapp2

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(), 'templates')))

class EditorPage(webapp2.RequestHandler):
  def get(self):
    template = template_env.get_template('index.html')
    self.response.write(template.render())

class TurtlePage(webapp2.RequestHandler):
  def get(self):
    template = template_env.get_template('turtle.html')
    self.response.write(template.render())

class ShellPage(webapp2.RequestHandler):
  def get(self):
    template = template_env.get_template('shell.html')
    self.response.write(template.render())
