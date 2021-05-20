from flask import render_template, request
from flask.templating import render_template
from app import app
from models.event_planner import events, add_new_event
from models.event import Event

@app.route('/')
def index():
    return "Hello World!"

@app.route('/events')
def events_index():
    return render_template('index.html', title="Home", my_events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['name']
    event_num_of_guests = request.form['num_of_guests']
    event_room = request.form['room']
    event_description = request.form['description']
    # Create a new event object with the events posted from form
    new_event = Event(event_name, event_num_of_guests, event_room, event_description)
    # Append event to the list (you could do this directly here, but we put it in the event_planner file)
    add_new_event(new_event)
    return render_template('index.html', title='Home', my_events=events)


    