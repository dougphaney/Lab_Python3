## 1. Fixed Bit Integers ##

import numpy as np
x = np.int8(100)
y = np.int8(28)
z = x + y
print(z)

## 2. Two's Complement Representation ##

x = 1 * (-2) + 0 * 1
y = 1 * (-8) + 0 * 4 + 1 * 2 + 0 * 1
z = 0 * (-8) + 1 * 4 + 1 * 2 + 0 * 1

## 3. Range of Two's Complement ##

import numpy as np
print(np.binary_repr(-2147483648, width=32))
print(np.binary_repr(2147483647, width=32))

## 4. Why Two's Complement ##

import sys
x = 2147483647 # maximum value for 32-bit integers
num_bytes = sys.getsizeof(x)
num_mb = 1000000000 * num_bytes / 1000000

## 6. Memory Consumption of Textual Data ##

import sys
s = "你"
size_s = sys.getsizeof(s)
size_ss = sys.getsizeof(s + s)

## 7. Python Internal String Representation ##

import sys
message = "I really like learning about Python! 🐍\n Me too! 😀😀\n I can't wait to see what we will learn in the next course 🙃\n"
message_latin_bytes = message.encode(encoding='Latin-1', errors='ignore')
cleaned_message = message_latin_bytes.decode(encoding='Latin-1')
message_size = sys.getsizeof(message)
cleaned_message_size = sys.getsizeof(cleaned_message)

## 8. Disk Consumption of Textual Data ##

import os
messages = "I really like learning about Python! 🐍\n Me too! 😀😀\n I can't wait to see what we will learn in the next course 🙃\n"
with open('utf8.txt', mode='w', encoding='utf8') as file:
    file.write(messages)    
size_utf8 = os.path.getsize('utf8.txt')

with open('utf32.txt', mode='w', encoding='utf32') as file:
    file.write(messages)
size_utf32 = os.path.getsize('utf32.txt')

## 9. Estimating the Disk Requirements ##

num_days_in_a_year = 356
num_years = 20
bytes_per_char = 32 / 8
num_transactions = 1000000
username_size = 20
product_name_size = 50
total_days = num_years * num_days_in_a_year
bytes_per_transaction = bytes_per_char * (2 * username_size + product_name_size)
bytes_per_day = bytes_per_transaction * num_transactions
total_bytes = total_days * bytes_per_day
bytes_in_gb = 10 ** 9

num_gb = total_bytes / bytes_in_gb