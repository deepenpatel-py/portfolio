from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')                             # Adding Actual website file (index.html) using render_templates
def my_port():
    return render_template('index.html')

