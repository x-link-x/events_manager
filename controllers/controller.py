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

@app.route('/events', methods=['GET', 'POST'])
def add_event():
    try:
        event_date = request.form['start_date']
        event_name = request.form['name']
        event_num_of_guests = request.form['num_of_guests']
        event_room = request.form['room']
        event_description = request.form['description']
        event_recurring = request.form['recurring']
    
        new_event = Event(event_name, event_num_of_guests, event_room, event_description, event_date)

        add_new_event(new_event)
        
        if event_recurring == "on":
            new_event.description += ". This is a recurring event" 

        return render_template('index.html', title='Home', my_events=events)

    except:
        return render_template('index.html', title='Home', my_events=events)

@app.route('/events/delete')
def delete_page():
    return render_template('delete.html', title="Delete an event", my_events=events)

@app.route('/events/delete/<index>', methods=['POST'])
def delete_event():
    delete_name = request.form['delete_name']
    delete_existing_event(delete_name)
    return render_template('index.html', title='Home', my_events=events)
   
    # else:
    #     return render_template('index.html', title='Home', my_events=events)
        