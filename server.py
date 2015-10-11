from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    #self.response.headers['Content-Type'] = 'text/plain'
    # Set the cross origin resource sharing header to allow AJAX
    #self.response.headers.add_header("Access-Control-Allow-Origin", "*")
    headers = {'Access-Control-Allow-Origin': "*"}

    return render_template('index.html'), 200, headers


if __name__=="__main__":
    app.run( debug=True )
