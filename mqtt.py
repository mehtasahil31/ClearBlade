from clearblade.ClearBladeCore import System
import random
import time
import psutil
import os

# System credentials
SystemKey = os.environ.get("SYSTEM_KEY")
SystemSecret = os.environ.get("SYSTEM_SECRET")

mySystem = System(SystemKey, SystemSecret)

# Log in as Adam
sahil = mySystem.User("mehtasahil31@gmail.com", "sahilmehta")

# Use Adam to access a messaging client
mqtt = mySystem.Messaging(sahil)


# Set up callback function
def on_connect(client, userdata, flags, rc):
    # When we connect to the broker, start publishing our data to the keelhauled channel
    for i in range(20):
        payload = "CPU Utilization : " +str(psutil.cpu_percent()) + ", Available Virtual Memory: "+ str(psutil.virtual_memory()[2])
        client.publish("Test Topic", payload)
        time.sleep(1)

# Connect callback to client
mqtt.on_connect = on_connect

# Connect and spin for 30 seconds before disconnecting
mqtt.connect()
time.sleep(30)
mqtt.disconnect()


#export SYSTEM_KEY='a0b1c6ca0b9cdb89d3f9ea82e86a'
#export SYSTEM_SECRET='A0B1C6CA0BE8F8DFA7ABF198A864'
