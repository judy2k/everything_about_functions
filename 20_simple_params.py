def send_sms(recipient, message):
    print(f"Sending a message to {recipient}: {message!r}")


"""
All arguments are required!

>>> send_many_sms()
Traceback (most recent call last):
  File "20_simple_params.py", line 5, in <module>
    send_many_sms()
TypeError: send_many_sms() missing 2 required positional arguments: 'recipient' and 'message'
"""


# Call with positional arguments:
send_sms("447700900770", "How's it going?")


# Call with named arguments:
send_sms(recipient="447700900770", message="How's it going?")


# Call with named arguments in different order:
send_sms(message="How's it going?", recipient="447700900770")


# Call with a combination of positional and named:
send_sms("447700900770", message="How's it going?")


"""
First arg is 'recipient', then we provide a named 'recipient' argument.

>>> send_many_sms("How's it going?", recipient="447700900770")
Traceback (most recent call last):
  File "20_simple_params.py", line 22, in <module>
    send_many_sms("How's it going?", recipient="447700900770")
TypeError: send_many_sms() got multiple values for argument 'recipient'
"""

"""
Can't provide arguments without matching parameter:

>>> send_sms("447700900770", "How's it going?", 42)
Traceback (most recent call last):
  File "20_simple_params.py", line 43, in <module>
    send_sms("447700900770", "How's it going?", 42)
TypeError: send_sms() takes 2 positional arguments but 3 were given

>>> send_sms("447700900770", "How's it going?", the_answer=42)
Traceback (most recent call last):
  File "20_simple_params.py", line 50, in <module>
    send_sms("447700900770", "How's it going?", the_answer=42)
TypeError: send_sms() got an unexpected keyword argument 'the_answer'
"""