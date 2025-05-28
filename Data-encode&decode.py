user_input = input("Enter data to encode and decode: ")

chars = sorted(set(user_input))

stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}

encode = lambda s: [stoi[i] for i in s]
decode = lambda l: "".join([itos[i] for i in l])

encoded = encode(user_input)
decoded = decode(encoded)

print("Encoded:", encoded)
print("Decoded:", decoded)