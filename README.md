# ClearBlade

## Phase 1

1. Firstly, I created an account on www.platform.clearblade.com
2. Selected Add system option and added an Empty system. 
3. Once a system is created, I selected that system. In the gear near the system name, I got System Key and System Secret from there.
4. Then I added a user from the Users menu and granted him Authenticated role.
5. Then I went in the roles menu and in the Authenticated/Message Topic section, I added a message topic and subscribed to that.


## Phase 2

I installed cClearBlade-Python-SDK

	pip install clearblade

Before running the above code, we will have to set two environment varibales

	export SYSTEM_KEY='a0b1c6ca0b9cdb89d3f9ea82e86a'
	export SYSTEM_SECRET='A0B1C6CA0BE8F8DFA7ABF198A864'

I have used [psutil](https://psutil.readthedocs.io/en/latest/) python library to send the cpu status.

Then I ran the mqtt.py

	python mqtt.py
	

#### After this you should get the message (CPU Staus and Memory) on the ClearBlade platform
	
