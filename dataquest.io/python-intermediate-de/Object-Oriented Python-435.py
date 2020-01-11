## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}
my_set = {2, 3, 5}
print(type(l))
print(type(s))
print(type(d))
print(type(my_set))

## 2. Sets ##

tri_num_sequence = [1, 3, 6, 10, 15, 10, 6, 3, 1]
odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
trinum_5 = set(tri_num_sequence)
odd_20 = set(odd_numbers)
odd_trinum = trinum_5.intersection(odd_20)

## 4. Defining a Class ##

class NewList():
    pass

## 5. Instantiating a Class ##

class NewList(DQ):
    pass

newlist_1 = NewList()
print(type(newlist_1))

## 6. Creating Methods ##

class NewList(DQ):
    def first_method():
        return "This is my first method"

newlist = NewList()

## 7. Understanding 'self' ##

# class NewList(DQ):
#     def first_method():
#         return "This is my first method"
class NewList(DQ):
    def first_method(self):
        return "This is my first method"

newlist = NewList()
result = newlist.first_method()

## 8. Creating a Method That Accepts an Argument ##

class NewList(DQ):
    def return_list(self, input_list):
        return input_list

newlist = NewList()
result = newlist.return_list([1, 2, 3])

## 9. Attributes and the Init Method ##

class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state

my_list = NewList([1, 2, 3, 4, 5])
print(my_list.data)

## 10. Creating an Append Method ##

# The NewList definition from the previous
# screen is copied here for your convenience

# class NewList(DQ):
#     """
#     A Python list with some extras!
#     """
#     def __init__(self, initial_state):
#         self.data = initial_state
class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
    
    def append(self, new_item):
        """
        Append `new_item` to the NewList
        """
        self.data = self.data + [new_item]

my_list = NewList([1, 2, 3, 4, 5])
print(my_list.data)
my_list.append(6)
print(my_list.data)

## 11. Creating and Updating an Attribute ##

# The NewList definition from the previous
# screen is copied here for your convenience

# class NewList(DQ):
#     """
#     A Python list with some extras!
#     """
#     def __init__(self, initial_state):
#         self.data = initial_state
    
#     def append(self, new_item):
#         """
#         Append `new_item` to the NewList
#         """
#         self.data = self.data + [new_item]
class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
        self.calc_length()
    
    def calc_length(self):
        """
        A helper function to calculate the .length
        attribute.
        """
        length = 0
        for item in self.data:
            length += 1
        self.length = length
    
    def append(self, new_item):
        """
        Append `new_item` to the NewList
        """
        self.data = self.data + [new_item]
        self.calc_length()

fibonacci = NewList([1, 1, 2, 3, 5])
print(fibonacci.length)

fibonacci.append(8)
print(fibonacci.length)