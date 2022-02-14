from flask import Flask # Flask is a framework for designing websites # we'll write everything here in one file
from flask import render_template # Render template function to render a page from a template
app = Flask(__name__)  # Note the double underscores on each side!

# This is the file that will serve as your application’s “backend,” routing data to the appropriate pages.
def index(): # Then create a function called index that returns our rendered index.html template
    template = 'index.html'
    return render_template(template)


if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
