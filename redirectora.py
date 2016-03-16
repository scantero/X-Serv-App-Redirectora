#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random

class redirectora (webapp.webApp):

    def process(self, parsedRequest):

        number = random.randint(1,10000)
        htmlAnswer = '<html><body><head>Estas siendo redirigido a /'
        htmlAnswer += str(number)
        htmlAnswer += '<meta http-equiv="refresh" content="3; url='
        htmlAnswer += str(number) + '" />'
        returnCode = '302 Found'

        return returnCode, htmlAnswer

if __name__ == "__main__":
    testWebApp = redirectora("localhost", 1234)
