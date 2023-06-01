def from_base10(n,b):
    if b < 2:
        raise ValueError("Base must be >= 2")
    if n < 0:
        raise ValueError("Number must be >= 0")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)

    return digits

print(from_base10(10, 2))

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("Digit_map is not long enought to encode this!")

    return ''.join(digit_map[d] for d in digits)

print(encode([15, 15], '0123456789ABCDEF'))

def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError("Invalid base: base must be between 2 and 36")
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)

    if sign == -1:
        encoding = '-' + encoding
    return encoding

#for checking
e = rebase_from10(314, 2)
print(e)
print(int(e, base=2))


