

class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, starter=None) -> None:
        self.head = None
        if starter:
            for item in reversed(starter):
                self.insert(item)

    def insert(self, value) -> None:
        self.head = Node(value, self.head)

    def __str__(self):
        output = ""
        for value in self:
            output += f"[ {value} ] -> "
        return output + "None"

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __len__(self):
        count = 0
        for item in self:
            count += 1
        return count

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError

    def __setitem__(self, index, value)  -> None:
        current = self.head
        currIdx = 0
        while current and currIdx != index:
            current = current.next
            currIdx += 1

        current.value = value

from functools import wraps
from datetime import datetime

def speed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tstart = datetime.now()
        output = func(*args, **kwargs)
        tend = datetime.now()
        print(tend - tstart)
        return output
    return wrapper


def UpPeRlOwEr(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        string = ""
        for index in range(len(output)):
            if (index % 2) == 0:
                string += output[index].lower()
            else: 
                string += output[index].upper()
        return string
    return wrapper

@UpPeRlOwEr
@speed
def studlycaps(text):
    return text

print(studlycaps("hello"))
