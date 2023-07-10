# Enter your code here. Read input from STDIN. Print output to STDOUT
lines = int(input())
texts = []
for i in range(lines):
    text = input()
    texts.append(text)

for text in texts:
    even_chars = [char for i, char in enumerate(text) if i % 2 == 0]
    odd_chars = [char for i, char in enumerate(text) if i % 2]
    print("".join(even_chars) + " " + "".join(odd_chars))
