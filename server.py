from flask import Flask, render_template, url_for, request
from marionette import Marionette

import local_tests 

app = Flask(__name__)

class TestInfo():
    def __init__(self):
        # test wide useful data
        self.phone_number = None
        self.network_name = None
        self.network_password = None

app.m = Marionette()
app.test_info = TestInfo()
app.test_results = {}

@app.route("/")
def index():
    if not app.m.session:
        app.m.start_session()
    return render_template("index.html", url=app.m.get_url(), js_url=url_for("static", filename="jquery.js"))

@app.route("/run_auto_tests/", methods=["GET"])
def run_auto_tests():
    return "I should run all the fully automated tests and return when I'm done"

@app.route("/get_results/")
def get_results():
    return "I should return the app.test_results"

@app.route("/run_test/<name>", methods=["GET", "POST"])
def run_test(name):
    # This should be used by the pseudo-manual tests.
    print name
    if hasattr(local_tests, name):
        test_function = getattr(local_tests, name)
        try:
            if request.form.get("test_data", None):
                print "Request data: %s" % request.form["test_data"]
                test_function(app.m, app.test_info, request.form["test_data"])
            else:
                test_function(app.m, app.test_info)
        except AssertionError as e:
            #add this to errors
            pass
        except Exception as e:
            # unexpected exception, return with appropriate error
            pass
    else:
        # return unsupported test
        print "unsupported test"
    return "apparently ran a test!"

@app.route("/set/<name>/<value>", methods=["POST"])
def set(name, value):
    # use this to set attributes to TestInfo
    if hasattr(app.test_info, name):
        setattr(app.test_info, name, value)
    return getattr(app.test_info, name)

if __name__ == "__main__":
    app.run(debug=True)
