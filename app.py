import csv # import csv
from flask import Flask # Flask is a framework for designing websites # we'll write everything here in one file
from flask import abort # returns a 404 page
from flask import render_template # Render template function to render a page from a template
app = Flask(__name__)  # Note the double underscores on each side!

def get_csv():
    csv_path = './static/la-riots-deaths.csv' # define csv file path
    csv_file = open(csv_path, 'r') # open and read csv
    csv_obj = csv.DictReader(csv_file) # takes each row in the csv and turns it into a dictionary
    csv_list = list(csv_obj) # convert to a permanent list
    return csv_list


# This is the file that will serve as your application’s “backend,” routing data to the appropriate pages.
@app.route("/") # Now use one of Flask’s coolest tricks, the app.route decorator, to connect that function with the root URL of our site, /.
def index(): # Then create a function called index that returns our rendered index.html file and puts it on our "site"
    template = 'index.html'
    object_list = get_csv() # call the function that we created above
    return render_template(template, object_list=object_list) # here, it'll return a list of csv

# Following code block creates a 'details' page for each person
@app.route('/<row_id>/')
def detail(row_id): # creates a detail function
    template = 'detail.html' # uses our detail.html file as its face
    object_list = get_csv() # pull csv
    for row in object_list:     #following function matches each row's id against the 'row_id' provided by the url.
        if row['id'] == row_id: # When you find a match, pass that row out to the template for rendering with the name 'object'
            return render_template(template, object=row)
    abort(404)



if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
