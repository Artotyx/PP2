#Syntax
print("Hello")

#Python Indentation
if 7>4:
    print ("7 is more than 4")
if 4 > 3 :
    print ("4 is greater than 3")

#Variables

carname = "Volvo"
x="Hi"
print(x)
y=3
y="Sally"
print(y)
X = str(3)    # x will be '3'
Y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(X,' ', Y,' ', z)
a = 5
b = "John"
print(type(a))
print(type(b))
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#Data types 
x = "Hello World"
print(type(x)) #str
x = 20.5
print(type(x)) #float
x = ["apple", "banana", "cherry"]
print(type(x)) #list
x = ("apple", "banana", "cherry")
print(type(x)) #tuple
x = {"name" : "John", "age" : 36}
print(type(x)) #dict
x = True
print(type(x)) #bool
#numbers 
x = 1    
y = 2.8  
z = 1j  
print(type(x)) # int
print(type(y)) # float
print(type(z))  # complex

x = 1.10 #float
y = 1.0
z = -35.59

x = 35e3 #float
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

x = 3+5j #complex
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

x=1
y=1.3
z=1j

a=float(x)
print(a)

b=int(y)
print(b)

c=complex(x)
c=complex(y)
print(c)

import random
print(random.randrange(1, 7))

x = 5
x = float(x)
x = 5.5
x = int(x)
x = 5
x = complex(x)

#casting
x=float(1)
z=int(3.4)
f=str("s1")
i=str(3.44)
print(z)

#string
print('a')
print("as")
w="jsjsjsjj"
print(w)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
a="Python"
print(a[3])
for ra in "banana":
   print(ra)

a="qwerttybdndjd"
print(len(a))
w="akjsdjdjd dkdkdk ndnndl ns !"
print ("sdjdjd dk" in w)
if "ndnndl" in w:
   print("YES")
print ("dkdkdk" not in w)
if "ajajggg" not in w:
   print("NO")

#string: slicing
b = "Artoty {}"
print(b[2:5])
print(b[:5])
print(b[2:])
print (b[-4:-2])
print(b.upper())
print(b.lower())
print(b.strip())
print(b)
print(b.replace("t","U"))
print(b.split("o"))
age = 21
print(b.format(age))
gpa=3.5
age=21
txt = "age: {}, gpa: {}"
print(txt.format(age, gpa))
q="our group is \"TEAM\" <3"
q="our \n group is \"TEAM\" <3"
q="our group\\ is \"TEAM\" <3"
q="our group \r is \"TEAM\"<3"
q="our group is\t \"TEAM\" <3"
q="our\b group\b is \"TEAM\" <3"
q="our group is \"TEAM\" \f <3"
q="our group is\110 \"TEAM\" <3"
q="our group is \"TEAM\"\x48 <3"
print(q)
u= "pandas"
print(u.capitalize())
t="ywuueb jdjdj jdjd"
x=t.capitalize()
print(x)
y="FISH"
print(y.casefold())
zz="banana"
print(zz.center(50,"U"))
print(zz.encode())
print(zz.endswith("u"))
d="O\t R A\t N G E"
print(d.expandtabs(20))
q="our team"
we=q.find("team")
print(we)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
txt = "Hello, welcome to my world."

x = txt.index("e")

print(x)
txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)

txt = "Hello, welcome to my world."

print(txt.find("q"))
# print(txt.index("q"))
txt = "Company12"
# txt = "Company 12"
x = txt.isalnum()

print(x)
txt = "CompanyX"
# txt = "Company10"

x = txt.isalpha()

print(x)
txt = "Company123"

x = txt.isascii()

print(x)

txt = "1234"

x = txt.isdecimal()

print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

txt = "50800"

x = txt.isdigit()

print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())
txt = "Demo"

x = txt.isidentifier()

print(x)
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)

txt = "   "

x = txt.isspace()

print(x)

txt = "   "

x = txt.isspace()

print(x)

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

txt = "banana"

x = txt.ljust(20, "O")

print(x)

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z))

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

x = "Hello World"
print(
len(x)
)
txt = "Hello World"
x = txt[0]
print (x)

txt = "Hello World"
x = txt[2:5]
print(x)

txt = " Hello World "
x = txt.strip()
print(x)
txt = "Hello World"
txt = txt.upper()
print(txt)

txt = "Hello World"
txt = txt.lower()
print(txt)

txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
