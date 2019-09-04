#!/usr/bin/env python
# coding: utf-8

# In[14]:


'''
Created By: Mayank
8/4/2019 12:31 AM
'''

import json
from flask import Flask ,request
import spacy
from spacy.util import minibatch, compounding
import random

# In[22]:

app = Flask(__name__)
nlp = spacy.load('./models/')

@app.route('/', methods=["POST"])
def login_page():
    in_data = request.data.decode()
    in_data = json.loads(in_data)

    text = in_data["text"]
    input_text = text.lower()
    doc = nlp(input_text)
    out_data = dict()
    out_data['text'] = text

    entities= list()
    for e in doc.ents:
        entity = dict()
        entity['entity'] = e.text
        entity['type'] = e.label_
        entities.append(entity)

    out_data['entities'] = entities


    return json.dumps(out_data,indent=4)


app.run('0.0.0.0')


