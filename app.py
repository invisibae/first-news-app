from flask import Flask # Flask is a framework for designing websites # we'll write everything here in one file
app = Flask(__name__)  # Note the double underscores on each side!

# This is the file that will serve as your application’s “backend,” routing data to the appropriate pages.

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
