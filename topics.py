import csv

def extract_topics(file_path):
    topics = set()
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            message = row[0]
            timestamp = row[1]
            source = row[2]
            # Extract hashtags from the message
            hashtags = [word for word in message.split() if word.startswith('#')]
            topics.update(hashtags)
    return topics

if __name__ == '__main__':
    file_path = 'tweets.tsv'
    topics = extract_topics(file_path)
    print(f'Topics: {topics}')
