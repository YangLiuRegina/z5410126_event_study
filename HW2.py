#question 1
import datetime

# question 2
str = ' some text '
print(' some text '.strip('some text'))

# question 3
w = "What"
i = "IS"
c = "CamelCase"
print('{} {} {}'.format(w,i.lower(),c))

class Test:
    def __init__(self):
        self.a = None
        self.b = None
obj = Test()
obj.x = 1
obj.y = 2
obj.y = obj.x
obj.x = obj.y
print(obj.x)

asx_value = 7111.4
date = datetime.date(2021,1,25)
units = 1
currency = "AUD"
print(f'The closing value of {units} unit of the All Ordinaries on {date} was {asx_value} {currency}.')

# Downloads Qantas share price beginning 1 January 2020
import yfinance
_tic = "QAN.AX"
start = '2020-01-01'
df = yfinance.download(_tic, start, None)
print(df)
df.to_csv('qan_stk_prc.csv')

# Downloads Qantas share price beginning 1 January 2020
import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')


lst = ['a','b','c','d','e','f','g','h','i','j']
print(f'The slice from index 3 through 10 is {lst[3:10]}')
print(f'The slice from index 3 through 11 is {lst[3:11]}')
print(f'The slice from index 3 through x is {lst[3:]}')
print(f'The slice from index 2 through 10 is {lst[2:10]}')
print(f'The slice from index 2 through 11 is {lst[2:11]}')
print(f'The slice from index 2 through x is {lst[2:]}')

t = ['a','b','c','d','e','f','g','h','i','j']
print(f'The slice from index -8 through 10 is {t[2:12]}')

lst = ['a','b','c','d','e','f','g','h','i','j']
print(f'The slice from index 2 through x is {lst[-8:-5]}')

t = ['a','b','c','d','e','f','g','h','i','j']
print(f'The slice from index is {t[:-5]}')


(b,s,i) = True, 'string',1
print(f"'b'is {b} and 's' is {s} and 'i'is {i}")

dic0 = {'a':1, 'b':2, 'c':3}
dic1 = dic0.update({'a':0,'d':4})
print(dic0['a'])

dic = {('a','b'):1, 'c':2,}
print(dic)

lst_a = ['a']
lst_b = ['b', lst_a]
lst_c = ['b',['a']]
print(lst_c)

# Use the provided list_a and list_b as your starting point.
# Then, perform the following steps:
#
# 1. Create a new list called sol (for solution) consisting of a slice
#    from list_a from the second element through to the word 'it'
# 2. Remove the value 'bad' from sol
# 3. Add a value 'including' so that it is the last value in sol
# 4. Add a value 'good' so that it is the third value in sol
# 5. Add all elements from list_b to the end of sol

list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
print(f'list_sol {list_a[2:7]}')
list_sol = ['has', 'bad', 'words', 'in', 'it']
list_sol.remove('bad')
print(list_sol)
list_sol.append('including')
print(list_sol)
list_sol.insert(2,'good')
print(list_sol)
list_sol.append(list_b)
print(list_sol)

# Use the set f_suburbs as given as your starting point. Then,
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that the suburbs listed below are in your set
#         Fairfield
#         Fairfield East
#         Fairfield Heights
#         Fairfield West
#         Fairlight
#         Fiddletown
#         Five Dock
#         Flemington
#         Forest Glen
#         Forest Lodge
#         Forestville
#         Freemans Reach
#         Frenchs Forest
#         Freshwater

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs.remove("Randwick")
f_suburbs.remove("Kensington")
print(f"After remove all suburbs that don't start wiht a F{f_suburbs}")
f_suburbs.add("Fairfield")
f_suburbs.add("Fairfield East")
f_suburbs.add("Fairfield Heights")
f_suburbs.add("Fairfield West")
f_suburbs.add("Fairlight")
f_suburbs.add("Fiddletown")
f_suburbs.add("Five Dock")
f_suburbs.add("Flemington")
f_suburbs.add("Forest Glen")
f_suburbs.add("Forest Lodge")
f_suburbs.add("Forestville")
f_suburbs.add("Freemans Reach")
f_suburbs.add("Frenchs Forest")
f_suburbs.add(" Freshwater")
print(f"After adding objects, f_suburbs is {f_suburbs}")

# The Fibonacci sequence is 0, 1, 1, 2, 3, 5, ... where each
# subsequent number is equal to the the preceeding two.
# This means the next elements in the list above would be 8 (5 + 3)
# and 13 (8 + 5)
#
# The 9th element in the sequence is 21. Let's call this the `current` value.
# The 8th element in the sequence is 13. Let's call this the `last` Value.
#
# Using PARALLEL ASSIGNMENT/TUPLE UNPACKING, perform the following operations
# in a single statement
#   1. replace the value of `current` with the value of the 10th
#       element in the sequence (so the sum of the 8th and 9th element)
#   2. replace the value of `last` with the value of the 9th element

# Leave this here
current = 21 # at this point, the 9th element of the sequence
last = 13 # at this point, the 8th element of the sequence
# Now, use parallel assignment to replace the value of `current` and `last`
# (put your answer below)
def getNum(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a
print(getNum(9))

tup = (0,1,1,2,3,5,8,13,21,34)



# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs,
# with the mapping going from suburb keys to population values.

# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:
#
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.


f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop('Randwick')
f_suburbs.pop('Kensington')
print(f"After popping all suburbs that don't start with a F, f_suburbs is now{f_suburbs}")
f_suburbs["Fairfield"]=18081
f_suburbs["Fairfield East"]=5273
f_suburbs["Fairfield Heights"]=7517
f_suburbs["Fairfield West"]=11575
f_suburbs["Fairlight"]=5840
f_suburbs["Fiddletown"]=233
f_suburbs["Five Dock"]=9356
f_suburbs["Flemington"]=None
f_suburbs["Forest Glen"]=None
f_suburbs["Forest Lodge"]=4583
f_suburbs["Forestville"]=8329
f_suburbs["Freemans Reach"]=1973
f_suburbs["Frenchs Forest"]=13473
f_suburbs["Freshwater"]=8866
print(f"f_suburbs now has objects {f_suburbs}")

tup = (1, 2, ('a', 'b'))
dic = {tup: 'value'}
print(dic)

current = 21
last = 13
current,last = (current+last,current)
print(current,last)

lst1 = ['a']
print(f'This is lst1: {lst1}')

lst2 = ['b', lst1]
print(f'This is lst2: {lst2}')

lst2[1].append('c')
print(lst1)
