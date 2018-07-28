import json, os
from time import sleep
import datetime
from slackclient import SlackClient

usertoken = os.environ["SLACK_USER_TOKEN"]
sc = SlackClient(usertoken)

while True:
    if sc.rtm_connect():
        while True:
            try:
                sleep(1)
                records = sc.rtm_read()
                logname = "slack." + "{0:%Y%m%d}".format(datetime.datetime.now())
                with open(logname, "a") as f:
                    for record in records:
                        f.write(json.dumps(record) + "\n")
                    f.flush()
            except:
                break
    else:
        sleep(5)
        sc = SlackClient(usertoken)

