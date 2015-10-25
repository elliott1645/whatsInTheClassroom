%load class.py
s = open("schedule.pl.mhtml", 'r').read()
import re
get_course_info = lambda a: [b for b in a.split('\r\n') if 'Course Info' in b]
x = s.split("<hr>")
y = map(get_course_info, x)
print y
%load times.py
s = open("schedule.pl.mhtml", 'r').read()
import re
get_meeting_info = lambda a: [b for b in a.split('\r\n') if 'Meeting Info' in b]
r = s.split("<hr>")
n = map(get_meeting_info, r)
print n
zip(n,y)
t = zip(n,y)
t
{x:y for (x,y) in t}
{x0:y0 for (x,y) in t}
{x[0]:y[0] for (x,y) in t}
{x[1]:y[1] for (x,y) in t}
len x
len x
len(x)
len(y)
{x[0]:y[0] for (x,y) in t}
t
t[0
  ]
t_new = filter(lambda x : len(x[0]) > 0 and len(x[1])>0, t)
t_new
t_new[0]
{x[0]:y[0] for (x,y) in t_new}
t_dict = {x[0]:y[0] for (x,y) in t_new}
{x[0]:y[0] for (x,y) in t_new}
t_new
import re
help(re.find)
help(re.search)
re.search('', t_new[0][0])
re.search('l', t_new[0][0])
t_new[0][0]
t_new[0][0][0]
%save courses.py
%save 'courses.py'
%save courses.py
%hist
