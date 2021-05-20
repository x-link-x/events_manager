from flask import render_template, request
from app import app
from models.event_planner import events, add_new_event, delete_existing_event
from models.event import Event

@app.route('/')
def index():
    return "Hello World!"

@app.route('/events')
def events_index():
    return render_template('index.html', title="Home", my_events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_num_of_guests = request.form['num_of_guests']
    event_room = request.form['room']
    event_description = request.form['description']
    event_recurring = request.form['recurring']
     # Create a new event object with the events posted from form
    new_event = Event(event_date, event_name, event_num_of_guests, event_room, event_description)
    # Append event to the list (you could do this directly here, but we put it in the event_planner file)
    add_new_event(new_event)
    if event_recurring == "on":
        new_event.description += "\nThis is a recurring event"
    return render_template('index.html', title='Home', my_events=events)

# @app.route('/events/delete')
# def delete_page():
#     return render_template('delete.html', title="Delete an event", my_events=events)

# @app.route('/events/delete/<index>', methods=['POST'])
# def delete_event():
#     delete_name = request.form['delete_name']
#     for event in events:
        # if delete_name == event.name:
            # delete_existing_event(delete_name)
#     return render_template('index.html', title='Home', my_events=events)
    