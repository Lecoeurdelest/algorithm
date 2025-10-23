class TinySet:
    def __init__(self, capacity=8):
        self._capacity = capacity
        self._buckets = [[] for _ in range(capacity)]
    
    def _hash(self, item):
       return hash(item) % self._capacity
    
    def add(self, item):
        bucket = self._buckets[self._hash(item)]
        if item not in bucket:
            bucket.append(item)

ts = TinySet()
ts.add("apple")
ts.add("banana")
print(ts._buckets)