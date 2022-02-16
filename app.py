import csv # import csv
from flask import Flask # Flask is a framework for designing websites # we'll write everything here in one file
from flask import render_template # Render template function to render a page from a template
app = Flask(__name__)  # Note the double underscores on each side!

def get_csv(): # define csv file path
    csv_path = './static/la-riots-deaths.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file) # take the header row and combine each header with each value
    csv_list = list(csv_obj)
    return csv_list


# This is the file that will serve as your application’s “backend,” routing data to the appropriate pages.
@app.route("/") # Now use one of Flask’s coolest tricks, the app.route decorator, to connect that function with the root URL of our site, /.
def index(): # Then create a function called index that returns our rendered index.html template
    template = 'index.html'
    object_list = get_csv() # call the function that we created above
    return render_template(template, object_list=object_list) # here, it'll return a list of csv

# Following code block creates a 'details' page for each person
@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    return render_template(template, row_id=row_id)



if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
