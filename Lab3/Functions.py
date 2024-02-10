
def my_function():
  print("Hello from a function")
my_function()
def my_function(fname, lname):
  print(fname)
my_function("Artoty", "Shakrat")
def my_function(x):
  return x + 5
print(my_function(4))
print(my_function(8))
print(my_function(45))
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")