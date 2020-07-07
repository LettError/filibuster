
from blurb import Blurb
from content import index

from pprint import pprint 
import codecs
import os

# see if we can generate all of them
w = Blurb()
names = w.getBlurbTypes()

dst = os.path.join(os.getcwd(), "test")
if not os.path.exists(dst):
	os.makedirs(dst)

maxTests = 20
count = 0

usage = {}	# keep a tally of how often names are used

class Page(object):
	def __init__(self, path, title="Filibuster"):
		self.path = path
		self.body = []
		self.head = ["<title>%s</title> <link rel=\"stylesheet\" href=\"styles.css\">"%title]
		self.head.append("<link href=\"https://fonts.googleapis.com/css?family=Source+Sans+Pro\" rel=\"stylesheet\">")

	def add(self, wrap=None, stuff=None):
		if wrap is None:
			self.body.append(stuff)
		else:
			self.body.append("<%s>"%wrap+stuff+"</%s>"%wrap)

	def addBlurb(self, stuff):
		self.body.append("<p class=\"blurb\">"+stuff+"</p>")

	def write(self):
		f = codecs.open(self.path, 'wb', 'utf-8')
		f.write(u"<html><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">")
		f.write(u"\n".join(self.head))
		f.write(u"\n<body>")
		f.write(u"\n".join(self.body))
		f.write(u"\n</body>")
		f.write(u"</html>")
		f.close()

indexPage = Page(os.path.join(dst, "index.html"))
indexPage.add('h1', "All Filibuster Patterns")
indexPage.add(None, '<ul>')

for name in names:
	count += 1
	namePath = os.path.join(dst, "%s.html"%name)
	indexPage.add("li", "\n<a href=\"%s\">%s</a>\n"%(namePath, name))
	nameTagPath = os.path.join(dst, "___%s_trying.html"%name)
	page = Page(namePath)
	t = codecs.open(nameTagPath, 'w', 'utf-8')
	t.write("a")
	success = False
	page.add("h1", "Results for \"%s\""%name)
	page.add('p', "<a href=\"index.html\">Index</a>")
	definedIn, usedIn = index(name)
	usedMods = {}
	for a,b in usedIn:
		usedMods[a] = True
	#page.add("p", "Defined in module %s"%definedIn[0])
	if usedMods:
		k = usedMods.keys()
		k.sort()
		page.add("p", "\nUsed in %s"%", ".join(k))
	if not name in usage:
		usage[name] = []
	for usedIn in usedMods:
		if usedIn not in usage[name]:
			usage[name].append(usedIn)
	for i in range(maxTests):
		result = w.getBlurb(name)
		try:
			page.addBlurb(result)
			success = True
		except:
			print("UnicodeDecodeError", definedIn[0], name)
	if success:
		t.close()
		os.remove(nameTagPath)
	page.write()

indexPage.add(None, '</ul>')
indexPage.write()

print('generated %d files'%count)
print('done')
