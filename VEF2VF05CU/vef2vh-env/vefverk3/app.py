from flask import Flask, render_template
from markupsafe import escape
import urllib.request

with urlibs.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', data=data)



@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

@app.errorhandler(500)
def servererror(error):
    return render_template('servererror.html'), 500

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)