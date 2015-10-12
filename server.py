from flask import Flask, render_template, send_file, request
import requests
from requests import ConnectionError
import urllib

app = Flask(__name__)

#template="index.html"
template="index.html"

@app.route('/')
def hello(name=None):
    #self.response.headers['Content-Type'] = 'text/plain'
    # Set the cross origin resource sharing header to allow AJAX
    #self.response.headers.add_header("Access-Control-Allow-Origin", "*")
    headers = {'Access-Control-Allow-Origin': "*"}

    return render_template(template), 200, headers

@app.route("/check")
def check_route():
    url = request.args.get("url")

    #url_test_encoding = urllib.urlencode({"url":"http://google.com"})
    #return "testing {0}".format(url) if url else "no Url Provided. Use /check?url=htt..."
    try:
        r = requests.get(url)
    except ConnectionError as e:
        return render_template("check.html", url = url), 500

    return render_template("check.html", url = url), r.status_code

if __name__=="__main__":
    app.run( debug=True )
