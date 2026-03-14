from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

# Home page route
@app.route("/")
def hello_world():
    return render_template("index.html")

# About page route
@app.route("/about")
def about():
    return render_template("about.html")

# Run the server
if __name__ == "__main__":
    app.run(debug=True)