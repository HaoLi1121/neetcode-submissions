class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        for t,v in self.store[key]:
            if t <= timestamp:
                res = v
            else:
                break
        return res
