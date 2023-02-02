import csv
from collections import defaultdict

# Read the dataset of tweets stored in a tsv file
with open('tweets.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    header = next(reader)

    # Dictionary to store the frequency of links for each user
    user_links = defaultdict(int)

    # Dictionary to store the consistency of links for each user
    user_consistency = defaultdict(lambda: defaultdict(int))

    for row in reader:
        user = row[0]
        message = row[1]
        if 'http' in message:
            # Extract the domain name from the link
            link = message.split('http')[1].split('/')[0]
            user_links[user] += 1
            user_consistency[user][link] += 1

# Calculate the consistency of links for each user
for user in user_consistency:
    total_links = user_links[user]
    consistency = {}
    for link in user_consistency[user]:
        consistency[link] = user_consistency[user][link] / total_links
    user_consistency[user] = consistency

# Print the frequency of links and consistency of links for each user
for user in user_links:
    print('User:', user)
    print('Frequency of links:', user_links[user])
    print('Consistency of links:', user_consistency[user])
    print()
