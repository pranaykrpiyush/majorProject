import tweepy
from langdetect import detect
from collections import defaultdict

# Twitter API credentials
consumer_key = "eGFRLcG4b6a91TE7DtG5zwrjT"
consumer_secret = "a6MVrWlyqLtDYDun0yPraLG35iWDItzXcdRtkGv0602pPT7W2G"
access_key = "1109516604575043584-POPzgSoVocK6b1ekvtI70GJRqo38IL"
access_secret = "6eOXdRBrffjgNmyvQRSuyTfJms9dnii2rI2YXFU2fCUbG"
# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Create API object
api = tweepy.API(auth)

# Function to check if the account is compromised or not
def is_compromised(username):
    try:
        # Collect the latest 200 tweets from the account
        tweets = api.user_timeline(screen_name=username, count=200)

        # Extract topics from the tweets
        topics = set()
        for tweet in tweets:
            message = tweet.text
            # Extract hashtags from the message
            hashtags = [word for word in message.split() if word.startswith('#')]
            topics.update(hashtags)

        # Extract message sources from the tweets
        sources = []
        for tweet in tweets:
            sources.append(tweet.source)

        # Extract the language used in the tweets
        languages = []
        for tweet in tweets:
            try:
                language = detect(tweet.text)
                languages.append(language)
            except:
                pass

        # Extract the interaction history for the account
        user_interaction = defaultdict(set)
        for tweet in tweets:
            message = tweet.text
            if '@' in message:
                # Extract the mention from the message
                mention = message.split('@')[1].split()[0]
                user_interaction[username].add(mention)

        # Get the active hours for the account
        hours = defaultdict(int)
        for tweet in tweets:
            time = tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')
            hour = int(time.split()[1].split(':')[0]) # Extracting the hour from the time
            hours[hour] += 1
        # Sorting the hours dictionary by the number of tweets for each hour
        sorted_hours = sorted(hours.items(), key=lambda x: x[1], reverse=True)
        active_hours = [hour for hour, count in sorted_hours[:3]] # Selecting the top 3 most active hours

        # Analyze the collected data to determine if the account is compromised
        if len(topics) == 0 or len(sources) == 0 or len(languages) == 0 or len(user_interaction[username]) == 0 or len(active_hours) == 0:
            return True
        else:
            return False
    except:
        return True

# Test the function with a sample Twitter username
print("Enter username:")
username = input()
if is_compromised(username):
    print(f"The Twitter account '{username}' is potentially compromised")
else:
    print(f"The Twitter account '{username}' is likely not compromised")



def predict_account_compromise(api_key, api_secret_key, access_token, access_token_secret, account):
    # Authenticate with Twitter API
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get latest tweets of the account
    tweets = api.user_timeline(screen_name=account, count=200)

    # Preprocess the tweets and extract features
    X = preprocess_tweets(tweets)

    # Load the trained logistic regression model
    model = load_model()

    # Predict the class labels and probabilities
    y_pred = model.predict(X)
    y_prob = model.predict_proba(X)

    # Calculate the probability of the account being compromised
    compromised_prob = y_prob[:, 1].mean()

    # Return the predicted class label and the probability of the account being compromised
    if y_pred.mean() == 0:
        return f"The account '{account}' is not compromised. Probability of being compromised: {compromised_prob:.2f}"
    else:
        return f"The account '{account}' is compromised. Probability of being compromised: {compromised_prob:.2f}"



#predict_account_compromise(consumer_key, consumer_secret, access_key, access_secret, username)
