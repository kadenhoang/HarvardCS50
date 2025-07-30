class Jar:
    def __init__(self, capacity=12, n=0):
        self._capacity = capacity
        self._n = 0

    def __str__(self):
        ...return "🍪" * self._n

    def deposit(self, n):
        if n < 0:
            raise ValueError("Where is the cookies?")
        if self._n + n > self._capacity:
            raise ValueError("The jar is full")
        self._n += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Are you gonna take some cookies?")
        if n > self._n
            raise ValueError("You are Greedy, There is not enough")
        self._n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n
        ...
    @capacity.setter
    def capacity(self,capacity):
        if not capacity > 0:
            raise ValueError("Empty")


def main():
    jar = Jar()
    jar.deposit(input("Add some cookies:"))
    print(jar)
