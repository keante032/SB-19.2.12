from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)



@app.route('/')
def homepage():
    """Show a form with prompts for all the words needed for the story."""

    return render_template('homepage.html', story=story)

@app.route('/story')
def story_page():
    """Show the story with the user-provided words filled in."""

    text = story.generate(request.args)

    return render_template('story_page.html', text=text)