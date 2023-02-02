import csv

# function to extract message source from tsv file
def extract_message_source(filename):
    sources = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader) # skip the header row
        for row in reader:
            sources.append(row[2]) # source is in the 3rd column
    return sources

# test the function
filename = 'tweets.tsv'
sources = extract_message_source(filename)
print(sources)
