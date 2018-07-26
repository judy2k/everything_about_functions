def send_many_sms(sender, message, recipients=["447700900770"]):
    for recipient in recipients:
        print(f"Sending a message to {recipient}")
    print("Done.")

# Previous calls still work ---------------------------------------------------


# Call with positional arguments:
send_many_sms("447700900730", "How's it going?")
# -> Sending a message to 447700900770


# Call with named argument:
send_many_sms("447700900730", "How's it going?", recipients=["447700900770", "447700900771"])
# -> Sending a message to 447700900770
# -> Sending a message to 447700900771


# Providing value for sender: -------------------------------------------------


# Positional args:
send_many_sms("447700900730", "How's it going?", ["447700900770", "447700900771"])


# Optional arg as named argument:
send_many_sms("447700900730", "How's it going?", recipients=["447700900770", "447700900771"])


print("Now let's 'log' the SMS messages")


def send_many_sms(sender, message, recipients=["447700900770"]):
    # Always send a copy to our "logging" phone:
    recipients.append("447700900666")
    for recipient in recipients:
        print(f"Sending a message to {recipient}")
    print("Done.")


# Call with positional arguments:
send_many_sms("447700900730", "How's it going?")
# Sending a message to 447700900770
# Sending a message to 447700900666
# Done.

send_many_sms("447700900730", "How's it going?")
# Sending a message to 447700900770
# Sending a message to 447700900666
# Sending a message to 447700900666
# Done.

send_many_sms("447700900730", "How's it going?")
# Sending a message to 447700900770
# Sending a message to 447700900666
# Sending a message to 447700900666
# Sending a message to 447700900666
# Done.


print("Provide recipients value:")

recipients = ["447700900770"]
send_many_sms("447700900730", "How's it going?", recipients)
print(recipients)
# ['447700900770', '447700900666']

# -----------------------------------------------------------------------------

print()
print("Let's fix that")


def send_many_sms(sender, message, recipients=None):
    if recipients is None:
        recipients = ["447700900770"]
    # Always send a copy to our "logging" phone:
    recipients.append("447700900666")
    for recipient in recipients:
        print(f"Sending a message to {recipient}")
    print("Done.")


send_many_sms("447700900730", "How's it going?")
# Sending a message to 447700900770
# Sending a message to 447700900666
# Done.

send_many_sms("447700900730", "How's it going?")
# Sending a message to 447700900770
# Sending a message to 447700900666
# Done.


# Warning! We are STILL modifying provided recipients!

recipients = ["447700900770"]
send_many_sms("447700900730", "How's it going?", recipients)
print(recipients)
# ['447700900770', '447700900666']

# -----------------------------------------------------------------------------


print()
print("Let's fix the 'modify parameter problem:")


def send_many_sms(sender, message, recipients=None):
    if recipients is None:
        recipients = ["447700900770"]
    # Create a *new* `recipients` variable:
    recipients = recipients + ["447700900666"]
    for recipient in recipients:
        print(f"Sending a message to {recipient}")
    print("Done.")


recipients = ["447700900770"]
send_many_sms("447700900730", "How's it going?", recipients)
print(recipients)
# ['447700900770']