# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate ) -> None:
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

        


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase) -> None:
        self.phrase = phrase.lower()


    def is_phrase_in(self, text) -> bool:
        txt = text.lower()
        for c in string.punctuation:
            txt = txt.replace(c, ' ')
        txt = txt.split()
        phrase = self.phrase.split()

        for i in range(len(txt)):
            if phrase[0] == txt[i]:
                txt = txt[i:i+len(phrase)]
                break
        if txt == phrase:
            return True
        return False


# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())


# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, time) -> None:
        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        if self.time > story.get_pubdate().replace(tzinfo=pytz.timezone("EST")):
            return True
        return False

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        if self.time < story.get_pubdate().replace(tzinfo=pytz.timezone("EST")):
            return True
        return False

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger) -> None:
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)
        

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger_1, trigger_2) -> None:
        self.triggers = (trigger_1, trigger_2)
    
    def evaluate(self, story: NewsStory):
        return self.triggers[0].evaluate(story) and self.triggers[1].evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger_1, trigger_2) -> None:
        self.triggers = (trigger_1, trigger_2)
    
    def evaluate(self, story):
        return self.triggers[0].evaluate(story) or self.triggers[1].evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """

    triggered = []
    for story in stories:
        for trigger in triggerlist:
            if story not in triggered and trigger.evaluate(story):
                triggered.append(story)
    return triggered



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    triggers = {}
    triggerlist = []
    for tr in lines:
        t = tr.split(',')
        if t[0][0] == 't':
            match t[1]:
                case 'TITLE':
                    triggers[t[0]] = TitleTrigger(t[2])
                case 'DESCRIPTION':
                    triggers[t[0]] = DescriptionTrigger(t[2])
                case 'AFTER':
                    triggers[t[0]] = AfterTrigger(t[2])
                case 'BEFORE':
                    triggers[t[0]] = BeforeTrigger(t[2])
                case 'NOT':
                    triggers[t[0]] = NotTrigger(triggers[t[2]])
                case 'AND':
                    triggers[t[0]] = AndTrigger(triggers[t[2]], triggers[t[3]])
                case 'OR':
                    triggers[t[0]] = OrTrigger(triggers[t[2]], triggers[t[3]])
        if t[0] == 'ADD':
            for i in range(1, len(t)):
                triggerlist.append(triggers[t[i]])
    return triggerlist



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

