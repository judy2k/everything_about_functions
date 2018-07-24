def send_sms(recipient, message, sender="447700900730"):
    print(f"Sending a message to {recipient}, from {sender}: {message!r}")


# Previous calls still work ---------------------------------------------------


# Call with positional arguments:
send_sms("447700900770", "How's it going?")


# Call with named arguments:
send_sms(recipient="447700900770", message="How's it going?")


# Call with named arguments in different order:
send_sms(message="How's it going?", recipient="447700900770")


# Call with a combination of positional and named:
send_sms("447700900770", message="How's it going?")


# Providing value for sender: -------------------------------------------------


# Positional args:
send_sms("447700900770", "How's it going?", "447700900289")


# Optional arg as named argument:
send_sms("447700900770", "How's it going?", sender="447700900289")


"""

# This doesn't work!
>>> def send_many_sms(recipient, sender="447700900289", message):
    print(f"Sending a message to {recipient}, from {sender}: {message!r}")
File "scratchpad.py", line 1
    def send_many_sms(recipient, sender="447700900289", message):
                ^
SyntaxError: non-default argument follows default argument

Read as: Parameter with non-default argument follows parameter with default argument
[Illustrate with arrows]
"""