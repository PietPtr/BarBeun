#!/usr/bin/python

from communication import *

NAME = "pieter"
to = input("To whom? ")
message = input("Message: ")

print(write(NAME, to, message))
