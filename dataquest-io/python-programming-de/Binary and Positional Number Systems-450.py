## 1. The Bit ##

print(2 ** 32)

## 2. The Decimal Number System ##

weight_digit_2 = 10 ** 2
value_digit_2 = 2 * weight_digit_2
weight_digit_5 = 10 ** 3
value_digit_5 = 5 * weight_digit_5

## 3. The Binary Number System ##

decimal_1 = 1 * (2 ** 4) + 1 * (2 ** 3) + 0 * (2 ** 2) + 0 * (2 ** 1) + 1 * (2 ** 0)
decimal_2 =                1 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 0 * (2 ** 0)
print(decimal_1, decimal_2)

## 4. Bits and the Binary Number System ##

bin_1 = bin(12345)
bin_2 = bin(1337)
print(bin_1)
print(bin_2)

## 5. Other Number Bases ##

base_8_to_10  = int('435', 8)
base_7_to_10 = int('10', 7)

## 6. Special Cases ##

hex_3501  = hex(3501)
decimal_F = int('F', 16)

## 7. Hexadecimal ##

red_hex = hex(213)
green_hex = hex(111)
blue_hex = hex(56)

## 8. Octal ##

octal_999 = oct(999)
original = int(octal_999, 8)