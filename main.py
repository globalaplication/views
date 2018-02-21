import urllib
class youtube(object):
    def __init__(self, channel):
        url = "https://www.youtube.com/channel/" +channel+ "/about"
        object = urllib.urlopen(url)
        self.source = object.readlines()
    def getviews(self, source):
        for test in range(0, len(source), +1):
            if source[test:test+len("<b>")] == "<b>":
                start = test + len("<b>")
                end = source.find("</b>", start)
        return "{} izlenme".format(source[start:end])
    def views(self):
        for line in self.source:
            if line.find('<span class="about-stat">') is not -1 and line.find("views") is not -1 :
                return self.getviews(line)
get = youtube("UCRx5NnTE3bK_gMXm0-lKlpw")
print get.views()
#2.7python
