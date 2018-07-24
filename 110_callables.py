

class Counter:
    def __init__(self):
        self.value = -1

    def __call__(self):
        self.value += 1
        return self.value


my_counter = Counter()

print(my_counter())
print(my_counter())