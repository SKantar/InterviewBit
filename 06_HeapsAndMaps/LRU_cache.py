# LRU Cache
# https://www.interviewbit.com/problems/lru-cache/
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It should
# support the following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
# otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache
# reaches its capacity, it should invalidate the least recently used item before inserting the new item.
# The LRUCache will be initialized with an integer corresponding to its capacity. Capacity indicates
# the maximum number of unique keys it can hold at a time.
#
# Definition of “least recently used” : An access to an item is defined as a get or a set operation
# of the item. “Least recently used” item is the one with the oldest access time.
#
#  NOTE: If you are using any global variables, make sure to clear them in the constructor.
# Example :
#
# Input :
#          capacity = 2
#          set(1, 10)
#          set(5, 12)
#          get(5)        returns 12
#          get(1)        returns 10
#          get(10)       returns -1
#          set(6, 14)    this pushes out key = 5 as LRU is full.
#          get(5)        returns -1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Content(object):
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None


class LRUCache(object):
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.tail = self.head = None
        self.values = dict()

    # @return an integer
    def get(self, key):
        """ Get element if exist and refresh last used """
        if key in self.values:
            self.refresh(key)
            return self.values[key].val
        return -1

    def invalidate(self):
        """ Release first used element in list """
        if self.head is None:
            raise Exception('Cannot invalidate empty cache...')

        key, value = self.head, self.values[self.head]

        if value.next is None:
            self.head = self.tail = None
        else:
            self.values[value.next].prev = None
            self.head = value.next

        del self.values[key]
        self.capacity += 1

    def refresh(self, key):
        """ Set element with key as last used """
        if key not in self.values:
            raise Exception('Cannot refresh non-existing key...')

        value = self.values[key]

        if value.next is None:
            return

        if value.prev is None:
            self.values[value.next].prev = None
            self.head = value.next
        else:
            self.values[value.next].prev = value.prev
            self.values[value.prev].next = value.next

        self.values[self.tail].next = key
        self.values[key].next = None
        self.values[key].prev = self.tail
        self.tail = key

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        """ Put element in cache """
        if key in self.values:
            self.refresh(key)
            self.values[key].val = value
        else:
            if self.capacity == 0:
                self.invalidate()

            self.values[key] = Content(value)
            self.capacity -= 1

            if self.tail is None:
                self.tail = self.head = key
            else:
                self.values[self.tail].next = key
                self.values[key].prev = self.tail
                self.tail = key

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
