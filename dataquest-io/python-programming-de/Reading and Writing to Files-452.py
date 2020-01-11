## 1. Reading Files in Python ##

file = open('dialog.txt')
lines = list(file)
file.close()

## 2. Reading with a Context Manager ##

with open('dialog.txt') as file:
    lines = list(file)

## 3. Reading with the Wrong Encoding ##

import csv
with open('kyoto_restaurants.csv') as file:
    rows = list(csv.reader(file))
    print(len(rows))

## 4. Finding the Right Encoding ##

import chardet
with open('kyoto_restaurants.csv', mode='rb') as file:
    detected_encoding = chardet.detect(file.read())

## 5. Reading with the Right Encoding ##

import csv
with open('kyoto_restaurants.csv', encoding='utf16') as file:
    rows = list(csv.reader(file))
    num_rows = len(rows)
    first_row = rows[1]

## 6. Encoding Identification Workflow ##

import csv
import chardet
with open('kyoto_restaurants.csv', mode='rb') as file:
    raw_bytes = file.read(32)
    encoding_name = chardet.detect(raw_bytes)['encoding']
with open('kyoto_restaurants.csv', encoding=encoding_name) as file:
    rows = list(csv.reader(file))

## 7. Writing to a file ##

with open('my_file.txt', mode='w') as file:
    file.write('first line\n')
    file.write('second line\n')

## 8. Appending to a File ##

with open('append.txt', mode='a') as file:
    file.write('my line\n')
with open('append.txt') as file:
    lines_appended = list(file)
    print(lines_appended)

## 9. Converting the Dataset to UTF-8 ##

import csv
with open('kyoto_restaurants.csv', encoding='UTF-16') as file:
    rows = list(csv.reader(file))
with open('kyoto_restaurants_utf8.csv', mode='w', encoding='UTF-8') as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow(row)