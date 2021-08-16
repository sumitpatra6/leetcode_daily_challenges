from heapq import heapify, heappop, heappush, nsmallest
from typing import Any

class Item:
    def __init__(self, key, value, count=1, time = 0) -> None:
        self.key = key
        self.value = value
        self.count = count
        self.time = time

    def increase_count(self):
        self.count += 1

    def set_time(self, time):
        self.time = time

    def copy(self):
        return Item(self.key, self.value, self.count)
    
    def reset_count(self):
        self.count = 1

    def __repr__(self):
        return "[Key {}, Value {}, Count: {}, Time {}] \n".format(self.key, self.value, self.count, self.time)
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.time < other.time
        return self.count < other.count


class LFUCache:
    _REMOVED = 'REMOVED'
    time = 0
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.heap = []
        self.cache = {}
        self.time = 0

    def _create_item(self, key: Any, value: Any) -> Item:
        return Item(key, value, time=self.time)
        
    def _copy_item(self, item: Item) -> Item:
        new_item = item.copy()
        new_item.increase_count()
        new_item.set_time(self.time)
        return new_item
    
    def delete_item(self, item: Item) -> None:
        del self.cache[item.key]
        item.value = self._REMOVED
    
    def insert_into_heap(self, item: Item):
        heappush(self.heap, item)


    def get(self, key: int) -> int:
        self.time += 1
        print("--------")
        print("Get key {}".format(key))
        if key in self.cache:
            item: Item = self.cache[key]
            ret_value = item.value
            new_item = self._copy_item(item)
            self.delete_item(item)
            self.cache[key] = new_item
            self.insert_into_heap(new_item)
            print(ret_value)
            return ret_value
        return -1


 
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        self.time += 1
        print("----------")
        print("Put: Key {}, Value {}".format(key, value))
        if key in self.cache:
            item: Item = self.cache[key]
            new_item = self._copy_item(item)
            self.delete_item(item)
            self.cache[key] = new_item
            self.insert_into_heap(new_item)
            print(self.cache)
            print(self.heap)
            return 
        
        # if the key is not present
        if len(self.cache.keys()) >= self.capacity:
            to_evict = None
            while self.heap:
                _to_evict: Item = heappop(self.heap)
                if _to_evict.value != self._REMOVED:
                    to_evict = _to_evict
                    break

            # 1. delete it from the cache
            # new_item: Item = Item(key, value)
            # new_item.set_time(self.time)
            new_item = self._create_item(key, value)
            self.delete_item(to_evict)
            self.cache[key] = new_item
            self.insert_into_heap(new_item)
        else:
            new_item = self._create_item(key, value)
            self.cache[key] = new_item
            self.insert_into_heap(new_item)

        print(self.cache)
        print(self.heap)





# Test

commands = ["put","put","get","get","put","get","get","get"]
data = [[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]
lfu_cache = LFUCache(2)
result = []
for i in range(len(commands)):
    c = commands[i]
    if c == "put":
        r = lfu_cache.put(data[i][0], data[i][1])
    if c == 'get':
        r = lfu_cache.get(data[i][0])
    result.append(r)

print(result)