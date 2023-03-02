import csv
from collections import defaultdict

def get_active_hours(filename):
    hours = defaultdict(int)

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            time = row[1] # Assuming the time is in the first column of the tsv file
            hour = int(time.split()[1].split(':')[0]) # Extracting the hour from the time
            hours[hour] += 1

    # Sorting the hours dictionary by the number of tweets for each hour
    sorted_hours = sorted(hours.items(), key=lambda x: x[1], reverse=True)
    active_hours = [hour for hour, count in sorted_hours[:3]] # Selecting the top 3 most active hours

    return active_hours

filename = 'tweets.tsv'
active_hours = get_active_hours(filename)
print(f"The active hours for this account are: {active_hours}")
