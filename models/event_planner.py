from models.event import *

event_1 = Event("Ceilidh", "50", "1", "St Andrews Day event", "2021-30-11")
event_2 = Event("Gardening Club Meeting", "10", "14", "meeting to discuss new town project", "2021-6-12")
events = [event_1, event_2]

def add_new_event(event):
    events.append(event)
    


# def get_event_index(event_name):
#     return events.index(event_name)

# def delete_existing_event(index):
#     events.pop(index)


