'''
Time Complexity - O(1) for all operation.
Space Complexity - O(n). we are using a queue and hashSet to store the allocated numbers.
'''
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        #create the hashSet and the queue. store the numbers in the queue
        self.hashSet = set()
        self.queue = deque()
        for i in range(0,maxNumbers):
            self.queue.append(i)
        

    def get(self) -> int:
        #to allocate numbers remove from front of queue and then add to hashSet. If empty queue return -1
        if self.queue:
            num = self.queue.popleft()
            self.hashSet.add(num)
            return num
        else:
            return -1

    def check(self, number: int) -> bool:
        #check whether the number is not present in the hashSet. An allocated number will be present in the hashSet
        return not number in self.hashSet

    def release(self, number: int) -> None:
        #if allocated number then remove from  hashSet and insert in the queue
        if number in self.hashSet:
            self.hashSet.remove(number)
            self.queue.append(number)
        return
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)