import urllib
class youtube(object):
    def __init__(self, channel):
        self.channel = channel
    def getviews(self, source):
        for test in range(0, len(source), +1):
            if source[test:test+len("<b>")] == "<b>":
                start = test + len("<b>")
                end = source.find("</b>", start)
        return "{} izlenme".format(source[start:end])
    def views(self):
        url = "https://www.youtube.com/channel/" +self.channel+ "/about"
        object = urllib.urlopen(url)
        source = object.readlines()
        for line in source:
            if line.find('<span class="about-stat">') is not -1 and line.find("views") is not -1 :
                return self.getviews(line)
get = youtube("UCRx5NnTE3bK_gMXm0-lKlpw")
print get.views()
#2.7python
