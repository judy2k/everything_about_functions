

def send_sms(sender,
             recipient,
             message,
             message_type,
             headers,
             ttl=None,
             callback=None,
             message_class=None,
             ):
    pass


send_sms("447700900775", "447700900963", "447700900963", "text", None)


send_sms(
    sender="447700900775",
    recipient="447700900963",
    message="447700900963",
    message_type="text",
    headers=None)


# Redefine with kw_only args --------------------------------------------------

def send_sms(sender,
             recipient,
             message,
             *,
             message_type,
             headers,
             ttl=None,
             callback=None,
             message_class=None,
             ):
    pass



"""
>>> send_sms("447700900775", "447700900963", "447700900963", "text", None)
Traceback (most recent call last):
  File "60_keyword_only_args.py", line 41, in <module>
    send_sms("447700900775", "447700900963", "447700900963", "text", None)
TypeError: send_sms() takes 3 positional arguments but 5 were given
"""


send_sms(
    "447700900775", "447700900963", "I'll meet you at 5!",
    message_type="text",
    headers=None)
