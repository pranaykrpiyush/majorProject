import csv
from collections import defaultdict

# Read the dataset of tweets stored in a tsv file
with open('tweets.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    header = next(reader)

    # Dictionary to store the network of each user
    user_network = defaultdict(list)

    # Read the network information from the file
    for row in reader:
        user = row[0]
        network = row[2]
        user_network[user].append(network)

# Dictionary to store the proximity information for each user
user_proximity = defaultdict(lambda: [0, 0])

# Read the dataset of tweets stored in a tsv file
with open('tweets.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    header = next(reader)

    for row in reader:
        sender = row[0]
        recipient = row[1]

        # Check if the recipient is in the same network as the sender
        if recipient in user_network[sender]:
            user_proximity[sender][0] += 1
        else:
            user_proximity[sender][1] += 1

# Calculate the fraction of local vs. non-local messages for each user
for user in user_proximity:
    total = sum(user_proximity[user])
    if total > 0:
        local_fraction = user_proximity[user][0] / total
    else:
        local_fraction = 0
    user_proximity[user] = local_fraction

# Print the proximity information for each user
for user in user_proximity:
    if user_proximity[user]>0:

        print('User:', user)
        print('Proximity:', user_proximity[user])
        print()
