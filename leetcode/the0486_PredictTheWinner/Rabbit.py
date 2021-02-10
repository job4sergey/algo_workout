sz = 5

# j - i + 1 = l
# j = l + i - 1

for l in range(1, sz+1):
    for i in range(0, sz - l + 1):
        print("(%s, %s)" % (i, l + i - 1), end=';')
    print()
