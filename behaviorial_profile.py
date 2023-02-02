def calculate_threshold(n):
    k = -0.005
    d = 0.82
    return max(0.1, k * n + d)

def detect_suspicious_group(group, behavioral_profiles):
    count = 0
    for message in group:
        if message not in behavioral_profiles:
            count += 1
    th = calculate_threshold(len(group))
    if count/len(group) > th:
        return True
    return False

def declare_compromised(group, behavioral_profiles):
    if detect_suspicious_group(group, behavioral_profiles):
        return [user for user in group]
    return []

# # Sample Data
# group1 = ['message1', 'message2', 'message3']
# group2 = ['message4', 'message5', 'message6', 'message7']
# behavioral_profiles = {'message1': 'profile1', 'message2': 'profile2', 'message3': 'profile3',
#                        'message4': 'profile4', 'message5': 'profile5', 'message6': 'profile6',
#                        'message7': 'profile7'}
#
# # Example Usage
# compromised_group1 = declare_compromised(group1, behavioral_profiles)
# compromised_group2 = declare_compromised(group2, behavioral_profiles)
#
# if compromised_group1:
#     print("The following users in group 1 are compromised:")
#     for user in compromised_group1:
#         print(user)
# else:
#     print("No users in group 1 are compromised.")
#
# if compromised_group2:
#     print("The following users in group 2 are compromised:")
#     for user in compromised_group2:
#         print(user)
# else:
#     print("No users in group 2 are compromised.")

