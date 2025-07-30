class Jar:
    def __init__(self, capacity=12,n):
        if not capacity >= 0:
            raise ValueError
        self.capacity = capacity
        self.n = n

    def __str__(self):
        ...return (f"{n}")

    def deposit(self, n):
        if len(n) is > 12:
            raise ValueError
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

def main():
    n = 
