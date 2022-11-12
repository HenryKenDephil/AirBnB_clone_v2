#!/usr/bin/python3
#script to display python

from flask import Flask

app = Flask(_name_)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    "displays the message, hello hbnb"
    return "Hello HBNB"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c():
    "returns c is fun and replaces underscore"
    return 'c %s' % text.replace('_', '')

@app.route('/python/(<text>)' strict_slashes=False)
def python():
    "display python"
    return 'python %s' % text.replace('_', 'is cool')
    
if __name__ == "__main__":
    "starting flask web"
    app.run(host='0.0.0.0', port=5000)