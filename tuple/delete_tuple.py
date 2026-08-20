# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple created:", my_tuple)

# Delete it completely
del my_tuple

try:
    print("Trying to print deleted tuple:")
    print(my_tuple)
except NameError:
    print("Success: Tuple has been completely deleted.")
