import json
import random
import datetime
import time

levels = ["INFO", "WARN", "ERROR"]



# how to write json file in python (python file)
# how to use datetime
# dict = {timestamp: random(datetime), log-level: random(levels), status-code: random(http_status), response_time_ms: random(number generator?)  }
# rand_timestamp = datetime.datetime.now().isoformat()

# data = f" \"timestamp\": {generator_timestamp}, \"log_level\": {random.choice(levels)} \"status_code\": {random.choice(HTTP_Status)}, \"response_time_ms\" : {random.randint(10, 1000)}\n"


# with open('server_logs.json', 'w') as f:
#     for log in range(500):
#         f.write(json.dumps(data, indent = 4))


# with open("server_logs.json", "w") as f:
#     for log in range(5):
#         random_log_dict = {
#             "timestamp": datetime.datetime.now().isoformat(),
#             "log_level": random.choice(levels),
#             "status_code": random.choice(HTTP_Status),
#             "response_time_in_ms": random.randint(10, 1000),
#         }
#         f.write(json.dumps(random_log_dict))


# with open("server_logs.json", "w") as f:
#     all_logs=[]
#     for log in range(5):
#         random_log_dict = {
#             "timestamp": datetime.datetime.now().isoformat(),
#             "log_level": random.choice(levels),
#             "status_code": random.choice(HTTP_Status),
#             "response_time_in_ms": random.randint(10, 1000),
#         }
#         all_logs.append(random_log_dict)
#     f.write(json.dumps(all_logs, indent=4))


with open("server_logs.json", "w") as f:
    all_logs=[]
    for log in range(500):
        random_log_dict = {
            "timestamp": datetime.datetime.now().isoformat(),
            "log_level": random.choice(levels),
            "status_code": 0,
            "response_time_in_ms": 0,
        }
        if random_log_dict['log_level'] == "INFO":
            random_log_dict['status_code'] = 200
            random_log_dict['response_time_in_ms'] = random.randint(10, 150)
        elif random_log_dict['log_level'] == "ERROR":
            random_log_dict['status_code'] = 500
            random_log_dict['response_time_in_ms'] = random.randint(400, 1000)
        else:
            random_log_dict['status_code'] = 404
            random_log_dict['response_time_in_ms'] = random.randint(151, 399)
        
        all_logs.append(random_log_dict)
        time.sleep(0.5)
    f.write(json.dumps(all_logs, indent=4))
