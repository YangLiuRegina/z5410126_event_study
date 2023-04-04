# Downloads Qantas share price beginning 1 January 2020
import datetime

import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)


a= 1+2
print(a)
print(type(a))

b= 2/1
print(b)
print(type(b))

a= 2
b= 3**a
c= 3**2
print(b)

print(1/3==0.33)

a=3
a=a+3
print(a)

a2=6
a2=a2+8
print(a2)

tic = "QAN.AX"

i= 1
test = i == 1
print(test)

x= 0.2 + 0.2
print(x)

print (x==0.4)

x = 1
print(type(x))
xstr= "1"
print(type(xstr))
test = x ==xstr
print(test)
print(type(test))

print(3+2)
a = '3'+'2'
print(type(a))

print('3'*3)

x = str('abc')
xup = str.upper(x)
print(xup)

a = True
b = 5
print("The value of a is {} and the value of b is {}".format(a , b))


x = str(5)
print(x)

Height = 30.5
Width = 33
Length = 56
Volume_Box = Height * Width * Length
print(f"the volume of the box is (Volume_Box) cubic centimeters")

lst = ["a", "b", "c", "d", "e", "f"]
print(lst[1:4])

lst = [1, "string", True, None, True]
print(f"Original lst is{lst}")
lst.remove(True)
print(f"lst after removing the first True is {lst}")

line = 'From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain = line.split()[1].split('@')[1]
print(domain)

line = 'From nickname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'

domain = line.split()[1].split('@')[1]

print(domain)

date = datetime.date(2023,2,28)
mins = 30.0

print("The exam's date is {} you will have {} minutes".format(mins,date))