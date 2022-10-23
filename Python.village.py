f = open("Input")
text = f.read()
f.close()
print(text)

# open file with - with function

with open("Input") as f:
    text = f.read()
    print(text)


with open("Input") as f:
    text = f.read()
    x = text[line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]

print(x)

# ^ this was not working because of readline instead of readlines

# Working with files

with open("Input", "r") as f:
    x = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]


with open("output", "w") as y:
    z = y.writelines(x)

# count words in a string

text = "We tried list and we tried dicts also we tried Zen"

wcdic = {}
for word in text.split(''):
    if word in wcdic:
        wcdic[word] += 1

    else:
        wcdic[word] = 1

for key, valve in wcdic.items():
    print(key, valve)