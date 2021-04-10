# Cleaner code
age = 22
if age >= 18:
    message = "Elegible"
else:
    message = "Not elegible"
print(message + " -First way")

# Ternary Operator
message = "Elegible" if age >= 18 else "Not Elegible"
print(message + " -Better way")
