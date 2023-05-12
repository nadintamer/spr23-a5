#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Checks that the program outputs "-1" for an input of "2 - 3"
assert run("2 - 3").output == -1

# Checks that the program outputs "4" for an input of "8 / 2"
assert run("8 / 2").output == 4
###

print("All tests passed!")
