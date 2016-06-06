#!/usr/bin/env python
import os
import jinja2
import webapp2



template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        num1 = int(self.request.get("num1"))
        num2 = int(self.request.get("num2"))
        operacija = self.request.get("operacija")

        if operacija == "+":
            rezultat = num1 + num2

        elif operacija == "-":
            rezultat = num1 - num2

        elif operacija == "*":
            rezultat = num1 * num2

        elif operacija == "/":
            rezultat = float(num1) / float(num2)

        rezultat = {
            "rezultat": rezultat
        }
        return self.render_template("rezultat.html", params=rezultat)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
