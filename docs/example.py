import ksmith

"""
All functions:
- hello
- delay_print
- clear
- get_num
- delay
"""

print('\n_____hello()_____')
# input is a name

# prints output
print(ksmith.hello("Eric"))
# output: "Hello Eric, my name is Kent Smith"

# stores output in variable
hello = ksmith.hello("Kevin")
print(hello + ".")
# output: "Hello Kevin, my name is Kent Smith." 

print('\n_____delay_print()______')
# input is a string
# optional input includes: level(speed), end(ending string)
#                          default: 4    default: ''

ksmith.delay_print("Hello, I am a computer")
# output: "Hello, I am a computer" (each char is printed after 40 milliseconds)

ksmith.delay_print("Hello, I am a computer", level=10)
# ksmith.delay_print("Hello, I am a computer", 10)
# specification: functions can be used as positional arguments, or specify
# output: "Hello, I am a computer" (each char is printed after 100 milliseconds)

ksmith.delay_print("Hello, I am a computer", end='!')
# output: "Hello, I am a computer!" ('!' is added to the end)

# use with all positional arguments:
ksmith.delay_print("Hello, I am a computer", 1, '.')
# output: "Hello, I am a computer." (each char is printed after 10 milliseconds)

print('\n_____clear()_____')
# no input

ksmith.clear()
# output: none (just clears the screen)

print('\n_____get_num()_____')
# input: all optional
# optional input includes: prompt(str),                start(lowest possible value)
#                          default: "Enter a number"   default: "none"

# finish(highest possible value), integer(boolean, requires integer)
# default: "none"                 default: False

# round_up(boolean, specifies if rounding up), round_num(the minimum remainder for rounding up)
# default: False                               default: 0.5

# for all cases below, output: "Output: (number entered)"

print(f"Output: {ksmith.get_num()}")
# specifications: if a number is not entered, "Please enter a number!" will be printed
#                 prompt is "Enter a number: "

print(f"Output: {ksmith.get_num(prompt='Please enter a number')}")
# specification: prompt is "Please enter a number: " )

print(f"Output: {ksmith.get_num(start=0)}")
# specification: if you enter a number less than 0, you will be prompted to try again

print(f"Output: {ksmith.get_num(finish=0)}")
# specification: if you enter a number greater than 0, you will be prompted to try again

print(f"Output: {ksmith.get_num(integer=True)}")
# specification: prompt will only accept integer values, if you enter a float, you will be prompted to try again

print(f"Output: {ksmith.get_num(round_up=True)}")
# specification: the final value will be "rounded up" if the value is greater than or equal to 0.5

print(f"Output: {ksmith.get_num(round_up=True, round_num=0.7)}")
# specification: the final value will be "rounded up" if the value is greater than or equal to 0.7

print(f"Output: {ksmith.get_num('Number', 5, 10, False, True, 0.9)}")
# NOTE: these are all positional arguments
# specifications: prompt is "Number:"
#                 minimum accepted value is 5
#                 maximum accepted value is 10
#                 integer input is not required
#                 rounding up is will happen if the tens the place is greater than or equal to 9

print('\n_____delay()______')
#input is an positive integer
#
#delays next action by the amount of the input
ksmith.delay(15)
print('It delays the next action')