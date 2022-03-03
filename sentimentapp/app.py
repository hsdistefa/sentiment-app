"""
Given a Financial News headline, returns sentiment score based our trained
model
"""
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# test data
sentiment_scores = [
    {'positive': 1},
    {'negative': -1},
    {'neutral': 0}
]


@app.route('/', methods=['GET', 'POST'])
def home():
    return flask.render_template('home.html')

app.run()
