class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:    
        self.counter = 0
        while target!=1:
            if maxDoubles == 0:
                self.counter = self.counter + target - 1 
                target = target - target + 1
            elif target %2 == 1:
                target = target -1
                self.counter = self.counter + 1 
            else:
                target = target/2
                maxDoubles = maxDoubles - 1
                self.counter = self.counter + 1
        return int(self.counter)