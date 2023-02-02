import datetime
import libtextcat
import re
from collections import Counter

class MessageCharacteristics:
    def __init__(self):
        self.hours = Counter()
        self.sources = Counter()
        self.languages = Counter()
        self.topics = Counter()
        self.domains = Counter()
        self.direct_interactions = Counter()
        self.types = Counter()

    def add_message(self, message):
        # Add hour of the day
        hour = datetime.datetime.fromtimestamp(message["timestamp"]).hour
        self.hours[hour] += 1

        # Add source of message
        source = message["source"]
        self.sources[source] += 1

        # Add language of message
        text = message["text"]
        language = self.detect_language(text)
        self.languages[language] += 1

        # Add topic of message
        topic = self.extract_topic(text)
        self.topics[topic] += 1

        # Add domain of links in message
        links = re.findall(r"(?P<url>https?://[^\s]+)", text)
        for link in links:
            domain = link.split("//")[-1].split("/")[0]
            self.domains[domain] += 1

        # Add direct user interaction
        interaction = message["interaction"]
        self.direct_interactions[interaction] += 1

        # Add type of message
        type = message["type"]
        self.types[type] += 1

    def detect_language(self, text):
        # Use libtextcat to detect language
        return libtextcat.classify(text)

    def extract_topic(self, text):
        # Extract topic using hashtags or other methods
        return None
