from flask import Flask, render_template, send_file, request
import requests
import markdown
from requests import ConnectionError
from urllib3.exceptions import HTTPError, SSLError
from bs4 import BeautifulSoup
import souplib

app = Flask(__name__)

template="index.html"
SSL_verification=False

links = None  # set to none by default

def build_url_list(url_list = "links.md"):
    """
    get the list of urls from a markdown file, and create some HTML
    It should only do it once each time we restart the server.
    """
    global links
    # check that we dont have it already
    if links is not None:
        return links
    # check that no one passed us garbage
    assert url_list is not None

    # This is the by-file way, that is troublesome, we cant edit it easily.
    html_links = None
    with open(url_list) as mdfh:
       md_links = mdfh.readlines()
       html_links_raw = markdown.markdown(" ".join(md_links))
       # Now that we have the links as html, we need to insert the class="button" to the a's
       bs = BeautifulSoup(html_links_raw)
       for link in bs.find_all("a"):
           souplib.update_attr(link, "class","button")

    # For now, till removed, we put the links in a template file as well
    with open("templates/links.html", "w") as fh:
        fh.write(bs.prettify())

    return html_links


    #m = markdown.Markdown()
    #m.convertFile(input = url_list, output = "templates/links.html")


@app.route('/')
def hello(name=None):
    #self.response.headers['Content-Type'] = 'text/plain'
    # Set the cross origin resource sharing header to allow AJAX
    #self.response.headers.add_header("Access-Control-Allow-Origin", "*")
    headers = {'Access-Control-Allow-Origin': "*"}

    build_url_list()

    return render_template(template), 200, headers

@app.route("/check")
def check_route():
    url = request.args.get("url")
    if url is None or url == "":
        return "Pleaze Bitch..." #TODO: Be more P.C. (Politically correct)

    try:
        r = requests.get(url, verify=SSL_verification)
        status = r.status_code

    except SSLError as e:
        print "SSL ERROR on {0}".format(url)
        # and retry without try and no-verify SSL
        r = requests.get(url, verify=False)
        print "Attempted with no verify {0}".format(r.status_code)
        status = r.status_code
    except HTTPError as e:
        print "HTTP ERROR on {0}".format(url)
        return render_template("check.html", url = url, status=status), status
    except ConnectionError as e:
        print "URL CHECK ERROR: {0}".format(e)
        return render_template("check.html", url = url, status=status), status
    except HTTPSConnectionPool as e:
        print "URL CHECK ERROR: {0}".format(e)
        return render_template("check.html", url = url, status=status), status

    return render_template("check.html", url=url,status=r.status_code), r.status_code

if __name__=="__main__":
    app.run( debug=True )
