temp = [7,5,6,3,4,1,2,9,11]
test = []
for i in range(len(temp)):
    if not test:
        test.append(i)
    else:
        while test and temp[i] > temp[test[len(test)-1]]:
            temp[test.pop()] = temp[i]
        test.append(i)
print temp