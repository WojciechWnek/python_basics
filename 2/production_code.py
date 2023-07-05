code = input("Pass whole code: ")

country = code[:3]
product = code[4:9]
batch = code[10:]

print("country: ", country)
print("Product: ", product)
print("Batch: ", batch)