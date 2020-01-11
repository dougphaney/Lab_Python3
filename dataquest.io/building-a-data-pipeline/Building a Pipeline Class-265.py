## 3. Function Closures ##

def add(a, b):
    return a + b
def partial(func, *args):
    parent_args = args
    def inner(*inner_args):
        return func(*(parent_args + inner_args))
    return inner

add_two = partial(add, 2)
print(add_two(7))

## 4. Python Decorators ##

# @catch_error
def throws_error():
    raise Exception('Throws Error')
def catch_error(func):
    def inner(*args):
        try:
            return func(*args)
        except Exception as e:
            return e
    return inner

@catch_error
def throws_error():
    raise Exception('Throws Error')
    
print(throws_error())

## 5. Method Decorators ##

class Pipeline:
    def __init__(self):
        self.tasks = []
class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self):
        def inner(f):
            self.tasks.append(f)
            return f
        return inner

pipeline = Pipeline()
    
@pipeline.task()
def first_task(x):
    return x + 1

print(pipeline.tasks)

## 6. Decorator Arguments ##

class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self):
        def inner(f):
            self.tasks.append(f)
            return f
        return inner

pipeline = Pipeline()
    
@pipeline.task()
def first_task(x):
    return x + 1

def second_task(x):
    return x * 2

def last_task(x):
    return x - 4
class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
            idx = self.tasks.index(depends_on) + 1
        def inner(f):
            self.tasks.insert(idx, f)
            return f
        return inner

pipeline = Pipeline()
    
@pipeline.task()
def first_task(x):
    return x + 1

@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2

@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4

print(pipeline.tasks)

## 7. Running the Pipeline ##

class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
            idx = self.tasks.index(depends_on) + 1
        def inner(f):
            self.tasks.insert(idx, f)
            return f
        return inner

pipeline = Pipeline()
    
@pipeline.task()
def first_task(x):
    return x + 1

@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2

@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4
class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
            idx = self.tasks.index(depends_on) + 1
        def inner(f):
            self.tasks.insert(idx, f)
            return f
        return inner
    
    def run(self, input_):
        output = input_
        for task in self.tasks:
            output = task(output)
        return output
    
pipeline = Pipeline()
    
@pipeline.task()
def first_task(x):
    return x + 1

@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2

@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4

print(pipeline.run(20))