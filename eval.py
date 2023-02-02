import csv

def train_model(input_file, s):
    models = {}
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            for feature in row:
                if feature not in models:
                    models[feature] = {}
                if row[feature] in models[feature]:
                    models[feature][row[feature]] += 1
                else:
                    models[feature][row[feature]] = 1
    for feature in models:
        N = sum(models[feature].values())
        if N < s:
            return None
        if feature == 'time_of_day':
            time_of_day_dict = models[feature]
            for hour in time_of_day_dict:
                hour_value = int(hour)
                prev_hour_value = (hour_value - 1) % 24
                next_hour_value = (hour_value + 1) % 24
                prev_hour = str(prev_hour_value)
                next_hour = str(next_hour_value)
                c0 = (time_of_day_dict[hour] + time_of_day_dict.get(prev_hour, 0) + time_of_day_dict.get(next_hour, 0)) / 3
                models[feature][hour] = c0
        M_bar = sum(models[feature].values()) / N
        models[feature]['M_bar'] = M_bar
    return models

def evaluate_message(message, models):
    anomaly_scores = {}
    for feature in message:
        if feature in models:
            if message[feature] in models[feature]:
                c = models[feature][message[feature]]
                M_bar = models[feature]['M_bar']
                if c >= M_bar:
                    anomaly_scores[feature] = 0
                else:
                    f = c / sum(models[feature].values())
                    anomaly_scores[feature] = 1 - f
            else:
                if 'null' in models[feature]:
                    p = models[feature]['null'] / sum(models[feature].values())
                    anomaly_scores[feature] = p
                else:
                    anomaly_scores[feature] = 1
    return anomaly_scores

def combine_scores(anomaly_scores):
    final_anomaly_score = sum(anomaly_scores.values()) / len(anomaly_scores)
    return final_anomaly_score
