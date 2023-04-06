
from flask import Flask, render_template

import urllib.request
import json
import pprint
app = Flask(__name__)
@app.get()