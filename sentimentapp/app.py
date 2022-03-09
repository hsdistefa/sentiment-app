"""
Given a Financial News headline, returns sentiment score based our trained
model
"""
import re

import flask
from flask import render_template, request, flash

import numpy as np
import pandas as pd
import tensorflow as tf
from transformers import BertTokenizer, TFBertModel


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
        sentiment_score = get_sentiment(headline)
        if headline == 'positive':
            sentiment_score = 1
        elif headline == 'negative':
            sentiment_score = -1
        return render_template('index_action.html',
                               headline=headline,
                               sentiment_score=sentiment_score)

    return render_template('index.html')


def get_sentiment(headline):
    model_path = './model/BERT_l.430_AC84.6_8Epochs.h5'
    loaded_model = tf.keras.models.load_model(model_path,
                                              custom_objects={
                                                  'TFBertModel': TFBertModel})

    #cleaned_headline = _clean_punctuation(headline)
    temp_df = pd.DataFrame(columns=['title'])
    temp_df.loc['title'] = headline

    # Encode input with bert encoder
    temp_df['title'] = temp_df['title'].astype(str)
    temp_input_encoded = _bert_encode(temp_df['title'])

    # Predict input based on model
    pred = loaded_model.predict(temp_input_encoded)
    idx = np.argmax(pred)
    if idx == 0:
        return 'negative'
    elif idx == 1:
        return 'neutral'
    else:
        return 'positive'


def _bert_encode(data):
    # Initializing BERT Tokenizer
    model_name = "bert-base-cased"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    tokens = tokenizer.batch_encode_plus(data,
                                         max_length=512,
                                         padding="max_length",
                                         truncation=True)
    return tf.constant(tokens["input_ids"])


def _clean_punctuation(sentence):
    cleaned = re.sub(r'[?|!|\'|"|#]', r'', sentence)
    cleaned = re.sub(r'[,|)|(|\|/]', r' ', cleaned)
    cleaned = cleaned.strip()
    cleaned = cleaned.replace("\n", " ")
    return cleaned


app.run()
