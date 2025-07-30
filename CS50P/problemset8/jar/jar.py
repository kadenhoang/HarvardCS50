class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        ...return (f"{self.n}")

    def deposit(self, n):
        self.n = n

    def withdraw(self, n):
        if not n:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n
        ...
    @capacity.setter
    def capacity(self,capacity):
        if not capacity >= 0:
            raise ValueError

    @deposit.setter
    def deposit(self,n):
        if len(n) is > 12:
            raise ValueError


def main():
    n = input(")
