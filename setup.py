#!/usr/bin/env python

from setuptools import setup

setup(name = "Filibuster",
      version = "3",
      description = "Python generator for nonsense language on all sorts of subjects.",
      author = "Erik van Blokland, Jonathan Hoefler, Rich Roat, Petr van Blokland, Just van Rossum and many others.",
      author_email = "erik@letterror.com",
      url = "https://github.com/LettError/filibuster",
      license = "MIT",
      packages = [
              "filibuster",
      ],
      package_dir = {"":"Lib"},
)
