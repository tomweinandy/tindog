"""
It's like Tinder, but for dogs
"""
from flask import Flask, render_template

# Add name of current directory
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
