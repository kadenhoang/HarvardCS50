class Jar:
    def __init__(self, capacity=12, n=0):
        self.capacity = capacity
        self.n = n

    def __str__(self):
        ...return "🍪" * self._n

    def deposit(self, n):
        self.n = n

    def withdraw(self, n):


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
            raise ValueError("Cannot be non-negative int")


def main():
    n = input("cookies")
    return Jar(n)
