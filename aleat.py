#!/usr/bin/python3

import webapp
import random

class Aleat(webapp.webApp):
    def process(self, parsedRequest):
        numRand = str(random.randint(0,999999999))
        newUrl = "http://localhost:1234/" + numRand

        return("200 OK", "<html><body><h1><a href=" + newUrl + ">Dame otra.</a></h1></body></html>")


if __name__ == "__main__":
    appUrlAleat = Aleat("127.0.0.1", 1234) #instancio la clase Aleat
