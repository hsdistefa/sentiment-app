"""
Given a Financial News headline, returns sentiment score based our trained
model
"""
import flask
from flask import render_template, request, flash


app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'A#IPmd83B*d7Z'

LAST_HEADLINE = None

# test data
sentiment_scores = [
    {'positive': 1},
    {'negative': -1},
    {'neutral': 0}
]


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        headline = request.form['headline']
    if not headline:
        flash('Headline is required!')
    else:
        return render_template('home_action.html', headline=headline)

    return render_template('home.html')


app.run()
