from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")



@app.route('/')
def homepage():
    return "hi there, how ya doin?"


@ask.launch
def start_skill():
    welcome_message = 'Tell me the genre you want to watch. You can pick between Comedy,Action,Mystery,Drama  !'
    return question(welcome_message)


@ask.intent("YesIntent")
def share_headlines():
    headline_msg = 'My favorite books based around new year are... Middlemarch, by George Eliot..., White Teeth, by Zadie Smith....., Bridget Jones Diary, by Helen Fielding. and.., A Long Way Down, by Nick Hornby. This one is really hillarious'
    return statement(headline_msg)


@ask.intent("NoIntent")
def no_intent():
    bye_text = 'OK. as you wish.., but you should try to develop reading habit this year'
    return statement(bye_text)

@ask.intent("HelpIntent")


if __name__ == '__main__':
    app.run(debug=True)
