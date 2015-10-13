from flask import Flask, render_template, send_file, request
import requests
from requests import ConnectionError
from urllib3.exceptions import HTTPError, SSLError

app = Flask(__name__)

#template="index.html"
template="jenkins.html"
SSL_verification=False

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
    try:
        r = requests.get(url, verify=SSL_verification)
    except SSLError as e:
        print "SSL ERROR on {0}".format(url)
        # and retry without try and no-verify SSL
        r = requests.get(url, verify=False)
        print "Attempted with no verify {0}".format(r.status_code)
        return render_template("check.html", url = url), r.status_code

    except HTTPError as e:
        print "HTTP ERROR on {0}".format(url)
        return render_template("check.html", url = url), 600
    except ConnectionError as e:
        print "URL CHECK ERROR: {0}".format(e)
        return render_template("check.html", url = url), 600

    return render_template("check.html", url = url), r.status_code

if __name__=="__main__":
    app.run( debug=True )
