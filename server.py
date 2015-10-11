from flask import Flask, render_template, send_file
import urllib

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    #self.response.headers['Content-Type'] = 'text/plain'
    # Set the cross origin resource sharing header to allow AJAX
    #self.response.headers.add_header("Access-Control-Allow-Origin", "*")
    headers = {'Access-Control-Allow-Origin': "*"}

    return render_template('index.html'), 200, headers

@app.route("/test/<url>")
def check_route(url=None):
    # TODO: find out the best way to pass the url. for now it seems to be a param
    return "testing {0}".format(url)
    #r = requests.get(decoder_url)
    #return render_template("check.html", url = decoder_url), r.status_code

if __name__=="__main__":
    app.run( debug=True )
