import requests

def get_later(url):
    def get():
        return requests.get(url)
    return get

getter = get_later(
    'https://media3.giphy.com/media/l41m4emQlTwc4COxG/giphy.gif')

# Time goes by ...

http_response = getter()
print("Returned status code:", http_response.status_code)


# nonlocal --------------------------------------------------------------------

# Can't assign to outer variable unless we use `nonlocal` statement:

def counter():
    value = -1

    def increment_and_return():
        nonlocal value
        value = value + 1
        return value

    return increment_and_return


my_counter = counter()
for _ in range(10):
    print(my_counter())