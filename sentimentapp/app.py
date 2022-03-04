"""
Given a Financial News headline, returns sentiment score based our trained
model
"""
import flask
from flask import render_template, request, flash


app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'A#IPmd83B*d7Z'


# test data
sentiment_scores = [
    {'positive': 1},
    {'negative': -1},
    {'neutral': 0}
]


@app.route('/', methods=['GET', 'POST'])
def home():
    headline = None
    if request.method == 'POST':
        headline = request.form['headline']
    if not headline:
        flash('Headline is required!')
    else:
        # Get sentiment score
        sentiment_score = 0
        if headline == 'positive':
            sentiment_score = 1
        elif headline == 'negative':
            sentiment_score = -1
        return render_template('index_action.html',
                               headline=headline,
                               sentiment_score=sentiment_score)

    return render_template('index.html')


app.run()
