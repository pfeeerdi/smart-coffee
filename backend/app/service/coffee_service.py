from flask import abort
from app.model import Coffee
from app import mqtt
from app import db
from datetime import datetime
import ast

def update_coffee_hist():
    mqtt.subscribe("ferdi9@hotmail.de/coffeeshistory")
    #mqtt.subscribe("ferdi9@hotmail.de/makecoffee")
    @mqtt.on_message()
    def handle_mqtt_message(client, userdata, message):
        data = dict(
            topic = message.topic,
            payload = message.payload.decode()
            )
        print(data)
        try:
            payloads = data['payload'].split(", ")
            date, time, type_coffee = payloads
            dt = date + " " + time #2022-2-2 18:17:05
            dt = datetime.strptime(dt, '%Y-%m-%d %X')
        except:
            print("Error while handeling Payload")
        data = get_hist()
        data["dates"].append(str(dt))
        data["coffee_types"].append(type_coffee)
        save_hist(data)
        print(f"Added a coffe with the details: dateimte: {dt}, coffee_type: {type_coffee}")
     

def get_hist():
        with open('history.txt', 'r') as hist_file:
            try:
                dates, coffee_types = [ast.literal_eval(x) for x in hist_file.readlines()]
            except:
                dates, coffee_types = [],[]
            return {"dates" : dates, "coffee_types" : coffee_types}

def save_hist(data):
    with open('history.txt', 'w') as hist_file:
        dates = data["dates"]
        coffee_types = data["coffee_types"]

        hist_file.write(str(dates) + "\n")
        hist_file.write(str(coffee_types) + "\n")


def make_coffee(coffee_type):
    return mqtt.publish('ferdi9@hotmail.de/makecoffee', coffee_type)