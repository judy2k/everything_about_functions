import inspect


def add_numbers(x, y):
    return x + y


sig = inspect.signature(add_numbers)

print(sig.parameters)

args = [2, 3]
bound_args = sig.bind(*args)
print(bound_args)
# <BoundArguments (x=2, y=3)>

for k, v in bound_args.arguments.items():
    print(f"{k}: {v}")

"""
>>> args = [2]
>>> print(sig.bind(*args))
Traceback (most recent call last):
  File "120_introspection.py", line 12, in <module>
    print(sig.bind(*args))
  File "/usr/local/var/pyenv/versions/3.6.3/lib/python3.6/inspect.py", line 2965, in bind
    return args[0]._bind(args[1:], kwargs)
  File "/usr/local/var/pyenv/versions/3.6.3/lib/python3.6/inspect.py", line 2880, in _bind
    raise TypeError(msg) from None
TypeError: missing a required argument: 'y'
"""


# Type hints ------------------------------------------------------------------


def add_numbers(x: int, y: int):
    return x + y


sig = inspect.signature(add_numbers)

# But we can call with strings!
print(sig.parameters)
args = ["a", "b"]
bound_args = sig.bind(*args)
print(bound_args)


print("validating -----------------------")


def validated(target):
    sig = inspect.signature(target)

    def wrapper(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        for name, value in bound_args.arguments.items():
            t = sig.parameters[name].annotation
            if not isinstance(value, t):
                raise TypeError(f"Argument {value!r} is not of type {t}")
        return target(*bound_args.args, **bound_args.kwargs)
    return wrapper


@validated
def add_numbers(x: int, y: int):
    return x + y


print(add_numbers(1, 2))


"""
>>> print(add_numbers(1, "two"))
Traceback (most recent call last):
  File "120_introspection.py", line 71, in <module>
    print(add_numbers(1, "two"))
  File "120_introspection.py", line 61, in wrapper
    raise TypeError(f"Argument {value!r} is not of type {t}")
TypeError: Argument 'two' is not of type <class 'int'>
"""