import logging
import json
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session


app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def welcome():
    """
    Message that runs on app launch
    """
    return question(render_template('welcome'))


@ask.intent("ReadStoryIntent")
def read_story():
    """
    Returns the day's story.
    """
    story = None

    with open("story.json", "r") as f:
        story = json.loads(f.read())
        print(story)

    if not story:
        return statement('story_error')

    story = render_template('story', title=story.get('title'), body=story.get('body'))
    return statement(story)


if __name__ == '__main__':
    app.run(debug=True)
