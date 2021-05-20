# from flask import render_template, request
from app import app
# from models.event_planner import events, add_new_event
# from models.event import Event

@app.route('/')
def index():
    return "Hello World!"