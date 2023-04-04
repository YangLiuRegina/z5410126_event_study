happy = True
if happy is True:
    print("I am happy")
print("This will print regardless of the value of happy")

happy = None
if happy:
    print("I am happy")

print(1 == True)

var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']
print(var1 == var2)
print(var1 is var2)

print(var3 == var4)
print(var3 is var4)

a = -1
b = True
if a != 0:
   print("a is non-zero")    # only first conditional will be trigger
elif b is True:              # rest of part code will be ignore
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")

 # the input function will always return string

letters = ['a','b','c','d','e']
i = 0
for x in letters:
    print(f"letters[{i} --> {x}")

less_than_test = "That" < "This"
print(f'"That"<"This" yields {less_than_test}')
greater_than_test = "That" > "This"
print(f'"That" > "This" yields {greater_than_test}')

var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']

var1 = 'a'
var2 = 'a'
print(var1 is var2)
print(var1 == var2)

var3 = ['a']
var4 = ['a']
print(var3 is var4)
print(var3 == var4)

a = 1
print (a)

a = 0
b = True
if a != 0:
    print("a is non-zero")
elif b is True:
    print("b is True")
elif a < 0 and b is True:
    print(" a is negative and b is True")
else:
    print("None of the conditions above hold")

# Code Challenge:loops (1)
# Using the provided list l, loop over the elements and print their values.
l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
for list in (l):
    print(list)
# code challenge:loops(2)
#Using the provided list l, loop over the elements.
#However, only print them if they do not begin with the letters "Forest".
#Use an if statement. You may extract letters from a string using a slice.
l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
l.remove("Forest Glen")
l.remove("Forest Lodge")
l.remove("Forestville")
for list in l:
    print(list)
# code challenge: loops 3
# Using the Dictionary provided, print out the town and population for each of the suburbs beginning with f meeting the following criteria:
#
# The suburb's name does not begin with "Forest"
#
# The population data exists. This means that the population is not None. In fact, is not None is how you test for that a value is not None in Python. Smart!
#
# Each line in the output should look like SUBURB_NAME: POPULATION. So, for example, Fairfield would be:
#
# Fairfield: 18081

f_suburbs = dict()
f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866
f_suburbs.pop("Forest Glen")
f_suburbs.pop("Forest Lodge")
f_suburbs.pop("Forestville")
f_suburbs.pop("Flemington")
for SUBURB_NAME,POPULATION in f_suburbs. items():
    print(f'{SUBURB_NAME}: {POPULATION}')
# code challenge : loops (4)
#Look over all integers from 1 to 100, doing the following:
#If the integer is divisible by 3 (but not by 5), write its value and Fizz. e.g., 12: Fizz
#If the integer is divisible by 5 (but not by 3), write its value and Buzz, e.g., 25: Buzz
#If the integer is divisible by 3 and divisible by 5, write its value and FIZZ BUZZ (in caps), e.g. 15: FIZZ BUZZ
#If none of the above apply, simply print the integer value
#To check if an integer j is divisible by 3, for example, use the logical expression j % 3 == 0.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print("{}: Fizz".format(i))
    else:
        if i % 5 == 0 and i % 3 != 0:
            print("{}: Buzz".format(i))
        else:
            if i % 3 == 0 and i % 5 == 0:
                print("{}: FIZZ BUZZ".format(i))
            else:
                print(i)

# code challenge : loop (5)
# Using the provided list l, loop over the elements and print their positional index and value.
# The print format should be POSITIONAL_INDEX: SUBURB. So, Fairfield would look like:
# 0: Fairfield
l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]

i = -1
for x in l:
    i = i + 1
    print(f"{i}: {x}")

first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
for last_name in last_names:
    for first_name in first_names:
        for middle_name in middle_names:
            if middle_name is None:
                print(first_name, last_name)
            else:
                print(first_name, middle_name, last_name)