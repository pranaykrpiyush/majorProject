import csv
from collections import defaultdict

# Read the dataset of tweets stored in a tsv file
with open('tweets.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    header = next(reader)

    # Dictionary to store the interaction history for each user
    user_interaction = defaultdict(set)

    for row in reader:
        user = row[0]
        message = row[1]
        if '@' in message:
            # Extract the mention from the message
            mention = message.split('@')[1].split()[0]
            user_interaction[user].add(mention)

# Print the interaction history for each user
for user in user_interaction:
    print('User:', user)
    print('Interaction history:', user_interaction[user])
    print()
