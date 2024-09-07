prevents pycdc decompilation by polluting with unsupported operations (prob gonna get fixed on accident in the near future (prob still gonna be doable because theres alot of unsupported operations in pycdc)) 

input
```py
def main():
    print('hello', end="")
    if 1==1:
        print(' world')
    else:
        pass

main()
```

pycdc output
```py
# Source Generated with Decompyle++
# File: main.cpython-312.pyc (Python 3.12)

raise TypeError
# WARNING: Decompyle incomplete
```

nopycdc output
```py
try:
    raise TypeError
except* TypeError:
    ...
try:
    raise TypeError
except* TypeError:
    ...
try:
    raise TypeError
except* TypeError:
    ...
try:
    raise TypeError
except* TypeError:
    ...
try:
    raise TypeError
except* TypeError:
    ...
match 0:
    case 1:
        print()
    case _:
        ...
match 0:
    case 1:
        print()
    case _:
        ...
match 0:
    case 1:
        print()
    case _:
        ...
match 0:
    case 1:
        print()
    case _:
        ...
match 0:
    case 1:
        print()
    case _:
        ...
try:
    raise TypeError
except* TypeError:
    match 0:
        case 1:
            print()
        case _:
            ...
    ...
    match 0:
        case 1:
            print()
        case _:
            ...

def main():
    match 0:
        case 1:
            print()
        case _:
            ...
    print('hello', end='')
    if 1 == 1:
        match 0:
            case 1:
                print()
            case _:
                ...
        print(' world')
        match 0:
            case 1:
                print()
            case _:
                ...
    else:
        pass
    match 0:
        case 1:
            print()
        case _:
            ...
main()
try:
    raise TypeError
except* TypeError:
    match 0:
        case 1:
            print()
        case _:
            ...
    ...
    match 0:
        case 1:
            print()
        case _:
            ...
```
