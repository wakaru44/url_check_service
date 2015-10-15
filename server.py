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
    if url is None or url == "":
        return "Pleaze Bitch..." #TODO: Be more P.C. (Politically correct)

    try:
        r = requests.get(url)
        status = r.status_code
    except ConnectionError as e:
        status = 600

    return render_template("check.html", url=url,status=status), status

if __name__=="__main__":
    app.run( debug=True )
