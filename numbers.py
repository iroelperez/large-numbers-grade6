import random

simpleNumbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                 "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

largeNumbers = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion",
                "octillion", "nonillion", "decillion"]


def split_thousands(n):
    result = list()
    while n >= 1000:
        r = n % 1000
        n = n // 1000
        result.append(r)
    else:
        result.append(n)
    return result


def spell_tens(n):
    if n < 20:
        return simpleNumbers[n]
    else:
        if n % 10 == 0:
            return tens[n // 10]
        else:
            return "{}-{}".format(tens[n // 10], simpleNumbers[n % 10])


def spell_hundreds(n):
    if n < 20:
        return simpleNumbers[n]
    else:
        if n < 100:
            return spell_tens(n)
        else:
            if n == 100:
                return "one hundred"
            else:
                return "{} hundred {}".format(simpleNumbers[n // 100], spell_tens(n % 100))


def spell_group(index, group):
    return "{} {}".format(spell_hundreds(group), largeNumbers[index])


def spell_group_tuple(t):
    (index, group) = t
    return spell_group(index, group)


def valid_group(t):
    (index, group) = t
    return group > 0


def spell_positive_number(n):
    groups = split_thousands(n)
    if len(groups) == 1:
        return spell_hundreds(n)
    else:
        return " ".join(list(reversed(list(map(spell_group_tuple,
                                               list(filter(valid_group, list(enumerate(groups)))))))))


def spell_signed(n, f):
    if n < 0:
        return "minus {}".format(f(-n))
    else:
        return f(n)


def spell_number(n):
    return spell_signed(n, spell_positive_number)


#print(spell_number(1))
#print(spell_number(-5))
#print(spell_number(-879931))
#print(spell_number(99))
#print(spell_number(125398000199001))
#print(spell_number(125000678))
#print(spell_number(100000000000000000780090000001))


def random_fn(n):
    return random.randrange(50, 10000000000)


lst = list(map(random_fn, range(1, 25)))

print("------------")

for n in lst:
    print("{}".format(n))

print("------------")

for n in lst:
    print("{} => {}".format(n, spell_number(n)))

