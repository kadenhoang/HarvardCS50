itemlist = []

while True:
    try:
    # ask user for input
        item = input().upper().strip()
    # put it in a list
        itemlist.append(item)

    except EOFError:
        break

#use a a loop with range to get the index and print
for i in range(len(sorted(itemlist))):
    print(i ,itemlist[i])
