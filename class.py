s = open("schedule.pl.mhtml", 'r').read()
import re
get_course_info = lambda a: [b for b in a.split('\r\n') if 'Course Info' in b]
x = s.split("<hr>")
y = map(get_course_info, x)
print y
