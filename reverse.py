input = list(map(str, input()))
input = list(dict.fromkeys(input))
input.reverse()
print("".join(input))