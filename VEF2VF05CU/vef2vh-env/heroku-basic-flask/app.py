import os
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <p><a href="/sida2" title="Síða 2">Síða 2 </a> | <a href="/sida3" title="Síða 3">Síða 3 </a></p>
    <img src="http://loremflickr.com/600/400" />
    """ .format(time=the_time)


if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True)