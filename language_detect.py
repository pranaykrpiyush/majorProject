#!pip install langdetect

from langdetect import detect

tweet = "RT @NarutoCyborg: #cancelcusatsemexams #cancelexamscusat Extremely shameful and disgusting as they were doing their protest in a peaceful..."

try:
    language = detect(tweet)
    print("The language of the tweet is:", language)
except Exception as e:
    print("Error detecting language:", e)
