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



@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
    abort(404)



if __name__ == '__main__':
    
    app.run(debug=True, use_reloader=True)
