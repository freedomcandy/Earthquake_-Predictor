class Fib(object):
    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 1, 1
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.a >= self.max_value:
            raise StopIteration()
        return_num, self.a, self.b = self.a, self.b, self.a+self.b
        return return_num
    
def funcFib(max_value):
    a, b = 1, 1
    while a <= max_value:
        return_num, a, b = a, b, a+b
        yield return_num
    
print list(funcFib(100))