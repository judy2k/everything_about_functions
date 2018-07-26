
USE_HTTPS = True


# Reading a global variable in a function is fine:
def using_https():
    return USE_HTTPS

print(using_https())


ALLOWED_DOMAINS = [
    ".europython.eu",
    ".ninjarockstar.guru",
]


def add_allowed_domain(domain):
    ALLOWED_DOMAINS.append(domain)


# Setting a global variable is **not** fine -----------------------------------

def set_https(value):
    USE_HTTPS = value
    print("USE_HTTPS set to", USE_HTTPS)


set_https(False)
print("USE_HTTPS is", USE_HTTPS)


# Fix it with `global` --------------------------------------------------------

def set_https(value):
    global USE_HTTPS
    USE_HTTPS = value
    print("USE_HTTPS set to", USE_HTTPS)


set_https(False)
print("USE_HTTPS is", USE_HTTPS)


# Trying to set a local variable and access a global:


def toggle_https():
    print("Toggling USE_HTTPS. Value before:", USE_HTTPS)
    USE_HTTPS = not USE_HTTPS
    print("Toggling USE_HTTPS. Value after:", USE_HTTPS)


"""
Note that the error is raised when *accessing* USE_HTTPS, but the **cause** is
in the line that sets the value.
>>> toggle_https()
Traceback (most recent call last):
  File "80_scope.py", line 44, in <module>
    toggle_https()
  File "80_scope.py", line 39, in toggle_https
    print("Toggling USE_HTTPS. Value before:", USE_HTTPS)
UnboundLocalError: local variable 'USE_HTTPS' referenced before assignment
"""

def toggle_https():
    USE_HTTPS = not USE_HTTPS


toggle_https()