from models.event import *

event_1 = Event("2021-12-14", "Ceilidh", "50", "1", "St Andrews Day event")
event_2 = Event("2021-05-23", "Gardening Club Meeting", "10", "14", "meeting to discuss new town project")
events = [event_1, event_2]

def add_new_event(event):
    events.append(event)

def delete_existing_event(event):
    events.pop(event)


