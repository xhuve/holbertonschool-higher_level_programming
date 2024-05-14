#!/usr/bin/python3

def add_tuple(tuple_a, tuple_b):
    first = list(tuple_a)
    second = list(tuple_b)
    if not first:
        first.append(0)
        first.append(0)
    elif len(first) < 2:
        first.append(0)

    if not second:
        second.append(0)
        second.append(0)
    elif len(second) < 2:
        second.append(0)

    return (first[0] + second[0], first[1] + second[1])

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))