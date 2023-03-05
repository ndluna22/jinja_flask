from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret1"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    word = story.word

    return render_template("madlibs.html", word=word)


@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)  # accesses attribute data

    return render_template("story.html", text=text)
