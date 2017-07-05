# -*- coding: utf-8 -*-

import os
import logging

import webapp2


class RedirectHandler(webapp2.RequestHandler):
    def get(self, slug):
        path = self.request.path_qs
        redirect = os.getenv("DOMAIN") + path
        logging.info(redirect)
        self.redirect(redirect)


app = webapp2.WSGIApplication([
    webapp2.Route(r'/<:.*>', RedirectHandler)
], debug=True)
