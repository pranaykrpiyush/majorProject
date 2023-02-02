import csv
import textcat

# load the textcat library
tc = textcat.TextCat()

# open the tsv file containing the tweets
with open("tweets.tsv", "r") as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        # get the text of the tweet
        message_text = row["Message Text"]

        # use the libtextcat library to determine the language of the message
        language = tc.guess_language(message_text)

        # print the language of the message
        print("Message Text: {}\nLanguage: {}\n".format(message_text, language))
