# In fulfillment to the coding challenge sent by ClearBlade (Yash Jain).
# By Sahil Mehta
# Email: mehtasahil31@gmail.com


from clearblade.ClearBladeCore import System
import random
import time
import psutil
import os

# System credentials
SystemKey = os.environ.get("SYSTEM_KEY")
SystemSecret = os.environ.get("SYSTEM_SECRET")

mySystem = System(SystemKey, SystemSecret)

# Log in as Sahil
sahil = mySystem.User("mehtasahil31@gmail.com", "sahilmehta")

# Use Sahil to access a messaging client
mqtt = mySystem.Messaging(sahil)


# Set up callback function
def on_connect(client, userdata, flags, rc):
    # When we connect to the broker, start publishing our data to the Test Topic channel
    payload = "CPU Utilization : " +str(psutil.cpu_percent()) + ", Available Virtual Memory: "+ str(psutil.virtual_memory()[2])

# Connect callback to client
mqtt.on_connect = on_connect

# Connect and spin for 30 seconds before disconnecting
mqtt.connect()
time.sleep(30)
mqtt.disconnect()
