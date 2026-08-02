import datetime
import json
import os
import random
import time

levels = ["INFO", "WARN", "ERROR"]
timestamp = datetime.datetime.now(tz=datetime.UTC).isoformat()

def corruption_chance():
    if random.random() < 0.5:
        corrupt_dict = {
            "timestamp": timestamp,
            "log_level": random.choice(levels),
            "status_code": random.choice(
                ["200", "404", "500", "SUCCESS", "NO", "FAIL"]
            ),
            "response_time_in_ms": random.randint(10, 1000),
        }
        rand_corrupt_dict = random.sample(
            list(corrupt_dict.keys()), random.randint(1, 4)
        )
        return {key: corrupt_dict[key] for key in rand_corrupt_dict}


if not os.path.exists("json"):
    os.makedirs("json")
with open("json/server_logs.json", "w") as f:
    all_logs = []
    for log in range(500):
        random_log_dict = {
            "timestamp": timestamp,
            "log_level": random.choice(levels),
            "status_code": 0,
            "response_time_in_ms": 0,
        }
        if random_log_dict["log_level"] == "INFO":
            random_log_dict["status_code"] = 200
            random_log_dict["response_time_in_ms"] = random.randint(10, 150)
        elif random_log_dict["log_level"] == "ERROR":
            random_log_dict["status_code"] = 500
            random_log_dict["response_time_in_ms"] = random.randint(400, 1000)
        else:
            random_log_dict["status_code"] = 404
            random_log_dict["response_time_in_ms"] = random.randint(151, 399)

        get_corrupted = corruption_chance()

        if get_corrupted:
            all_logs.append(get_corrupted)
        else:
            all_logs.append(random_log_dict)


        time.sleep(0.1)
    json.dump(all_logs, f, indent=4)
