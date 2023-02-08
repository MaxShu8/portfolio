import string

alfabet = list(string.ascii_lowercase)
print(alfabet)

figure = [i+1 for i in range(len(alfabet))]
print(figure)

across_list = {}

# first example
for i in range(len(alfabet)):
    across_list[figure[i]] = alfabet[i]
print(across_list)

# second example
for i in range(len(alfabet)):
    across_list = dict(zip(figure, alfabet))
print(across_list)
