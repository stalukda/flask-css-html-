from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def home_page():
    """Home page."""

    return render_template("index.html")


@app.route('/application-form')
def app_form():
    """Present form to fill out"""

    return render_template("application-form.html")


@app.route('/application-success', methods=["POST"])
def submitted_form():
    """Acknowledge application"""

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    salary_req = float(request.form.get("salary_req"))
    jobs = request.form.getlist("jobs")
    
    return render_template("application-response.html", 
                            first_name = first_name, 
                            last_name = last_name, 
                            salary_req = '${:,.2f}'.format(salary_req),
                            jobs = jobs)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
