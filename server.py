from flask import Flask, render_template, send_file, request
import urllib

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    #self.response.headers['Content-Type'] = 'text/plain'
    # Set the cross origin resource sharing header to allow AJAX
    #self.response.headers.add_header("Access-Control-Allow-Origin", "*")
    headers = {'Access-Control-Allow-Origin': "*"}

    return render_template('index.html'), 200, headers

@app.route("/check")
def check_route():
    # TODO: find out the best way to pass the url. for now it seems to be a param
    url = request.args.get("url")

    return "testing {0}".format(url) if url else "no Url Provided. Use /check?url=htt..."
    #r = requests.get(decoder_url)
    #return render_template("check.html", url = decoder_url), r.status_code

if __name__=="__main__":
    app.run( debug=True )
