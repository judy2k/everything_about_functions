

def get_callers_class():
    print("My caller's class is: ", __class__)


class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_sms(self, sender, recipient, message):
        url = self.base_url + "send_sms"

    def what_class_am_i(self):
        print(__class__)


my_client = Client("https://api.example.org/")
my_client.send_sms("sender", "recipient", "Hey, how's it going?")


"""
# Can't call it on the class - need to provide self!
>>> Client.send_sms("sender", "recipient", "Hey, how's it going?")
Traceback (most recent call last):
  File "100_methods.py", line 14, in <module>
    Client.send_sms("sender", "recipient", "Hey, how's it going?")
TypeError: send_sms() missing 1 required positional argument: 'message'
"""

Client.send_sms(my_client, "sender", "recipient", "Hey, how's it going?")

"""
>>> Client.send_sms
<function Client.send_sms at 0x10f891510>
"""

# So our *function* still exists on the class.
# What is it on the instance?

"""
>>> my_client.send_sms
<bound method Client.send_sms of <__main__.Client object at 0x10f88afd0>>
"""

# They're different! So where does the bound method come from?

"""
>>> Client.send_sms.__get__(my_client)
<bound method Client.send_sms of <__main__.Client object at 0x10f88afd0>>
"""

my_client.what_class_am_i()

"""
Calls to `super` are detected by the Python compiler and converted from:
super()

to

super(__class__, self)
"""

