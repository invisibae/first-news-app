import csv # import csv
from flask import Flask # Flask is a framework for designing websites # we'll write everything here in one file
from flask import render_template # Render template function to render a page from a template
app = Flask(__name__)  # Note the double underscores on each side!

def get_csv(): # define csv file path
    csv_path = './static/la-riots-deaths.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)


# This is the file that will serve as your application’s “backend,” routing data to the appropriate pages.
@app.route("/") # Now use one of Flask’s coolest tricks, the app.route decorator, to connect that function with the root URL of our site, /.
def index(): # Then create a function called index that returns our rendered index.html template
    template = 'index.html'
    return render_template(template)


if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
