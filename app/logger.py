import datetime

def log(message):
    with open("../output/log.txt","a") as f:
        f.write(f"{datetime.datetime.now()} : {message}\n")
