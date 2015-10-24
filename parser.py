from bs4 import BeautifulSoup
#import urllib
#r = urllib.urlopen('http://www.albany.edu/cgi-bin/general-search/search.pl').read()
r = open('schedule.pl.mhtml', 'r')
soup = BeautifulSoup(r,'lxml')
#print type(soup)
#print soup.prettify()
tag = soup.b
type(tag)
tag.name = "br"
print tag
string = "Meeting Info:"
tag.string
print type(tag.string)
print soup.find_all('br',text = "Meeting")
