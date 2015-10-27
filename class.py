import re
schedule = open("schedule.pl.mhtml", 'r').read()

def make_query(q_str):
    
    def partial_query(rows, query):
        matches = []
        for row in rows:
            lines = row.split('\r\n')
            for line in lines:
                if query in line:
                    matches.append(line)
        return matches

    # because how do I curry in python?
    return lambda x: partial_query(x, q_str)

# extract the relevent lines
get_course_info = make_query('Course Info')
get_meeting_info = make_query('Meeting Info')
classes = schedule.split("<hr>")[1:]
course_info = get_course_info(classes)
meeting_info = get_meeting_info(classes)

# get the room numbers out of the meeting info string
rooms = map(lambda x : re.findall('[A-Z]{2}\d{4}', x), meeting_info)

# create a nice mapping from room->info
zipped = zip(rooms, course_info)
filtered = filter(lambda x : len(x[0])>0, zipped)
final_form = {x[0]:y for (x,y) in filtered}
print final_form

