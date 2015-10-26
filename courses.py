f = open('class.py','r')
s = open("schedule.pl.mhtml", 'r').read()
import re
get_course_info = lambda a: [b for b in a.split('\r\n') if 'Course Info' in b]
x = s.split("<hr>")
y = map(get_course_info, x)
#print y
g = open('times.py','r')
import re
get_meeting_info = lambda a: [b for b in a.split('\r\n') if 'Meeting Info' in b]
r = s.split("<hr>")
n = map(get_meeting_info, r)
#print n
zip(n,y)
t = zip(n,y)
t
t_new = filter(lambda x : len(x[0]) > 0 and len(x[1])>0, t)
t_new
t_new[0]
{x[0]:y[0] for (x,y) in t_new}
t_dict = {x[0]:y[0] for (x,y) in t_new}
{x[0]:y[0] for (x,y) in t_new}
t_new
import re
print t
