## 2. Comparing Object-Oriented to Functional ##

## Display
def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

example_lines = read('example_log.txt')
lines_count = count(example_lines)

## 4. The Lambda Expression ##

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
lines = read('example_log.txt')
sorted_lines = sorted(lines, key=lambda x: x.split(' ')[5])
print(sorted_lines)

## 5. The Map Function ##

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
print(ip_addresses)

## 6. The Filter Function ##

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))
print(filtered_ips)

## 7. The Reduce Function ##

from functools import reduce

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))
count_all = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, lines)
count_filtered = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, filtered_ips)
ratio = count_filtered / count_all

print(ratio)

## 8. Rewriting with List Comprehension ##

lines = read('example_log.txt')
# Rewrite ip_addresses, and filtered_ips.
# list(map(lambda x: x.split()[0], lines))
# list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))
count_all = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, lines)
count_filtered = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, filtered_ips)
ratio = count_filtered / count_all
print(ratio)
lines = read('example_log.txt')
ip_addresses = [line.split()[0] for line in lines]
filtered_ips = [
    ip.split('.')[0]
    for ip in ip_addresses if int(ip.split('.')[0]) <= 20
]
count_all = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, lines)
count_filtered = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, filtered_ips)
ratio = count_filtered / count_all
print(ratio)

## 9. Writing Function Partials ##

from functools import partial

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

# reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, lines)
# reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, filtered_ips)
ratio = count_filtered / count_all
print(ratio)
from functools import partial

count = partial(
    reduce,
    lambda x, _: 2 if isinstance(x, str) else x + 1
)

lines = read('example_log.txt')
ip_addresses = [line.split()[0] for line in lines]
filtered_ips = [
    ip.split('.')[0]
    for ip in ip_addresses if int(ip.split('.')[0]) <= 20
]
count_all = count(lines)
count_filtered =  count(filtered_ips)
ratio = count_filtered / count_all
print(ratio)

## 10. Using Functional Composition ##

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

ratio = count_filtered / count_all
extract_ips = partial(
    map,
    lambda x: x.split()[0]
)
filter_ips = partial(
    filter,
    lambda x: int(x.split('.')[0]) <= 20
)
count = partial(
    reduce,
    lambda x, _: 2 if isinstance(x, str) else x + 1
)

composed = compose(
    extract_ips,
    filter_ips,
    count
)
counted = composed(lines)