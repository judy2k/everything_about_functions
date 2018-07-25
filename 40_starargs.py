import re
from functools import partial


def printf(fmt, *args):
    pass
    print(re.sub(r'%s', partial(next, iter(args)), fmt))


printf("A greeting: %s", 'hello')

printf("Two greetings: %s, %s", 'hello', 'hi')

printf("Three greetings: %s, %s, %s", 'hello', 'hi', 'hey')


def send_sms(message, *recipients):
    print(f"Send a message to: {recipients}")


# 'star-arg' is 0..*:
send_sms("How's it going?")
# Send a message to: ()

send_sms("How's it going?", "447700900770")
# Send a message to: ('447700900770',)

# Call with positional arguments:
send_sms("How's it going?", "447700900770", "447700900771")
# Send a message to: ('447700900770', '447700900771')


"""
This doesn't work - recipients is **not** a parameter:

# Provide args explicitly:
>>> send_sms("How's it going?", recipients=("447700900770", "447700900771"))
Traceback (most recent call last):
  File "40_starargs.py", line 17, in <module>
    send_sms("How's it going?", recipients=("447700900770", "447700900771"))
TypeError: send_sms() got an unexpected keyword argument 'recipients'
"""

# 'recipients' is usually called 'args'