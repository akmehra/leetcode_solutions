def true_or_false(temp):
    x= []

    if len(temp) == 1 and temp[0] == '#':
        return True

    for each in temp:

        if x and x[len(x)-1] == 2:
            x.pop()

        if x and x[len(x)-1] == 1 and each == '#':
            x.pop()
            continue

        if x and x[len(x)-1] == 1 and each != '#':
            x.pop()
            x.append(0)
            continue

        if x and x[len(x)-1] == 0 and each != '#':
            x.pop()
            x.append(1)
            x.append(0)
            continue

        if x and x[len(x)-1] == 0 and each == '#':
            x.pop()
            x.append(1)
            continue

        if each == '#' and len(x) == 0:
            return False

        if each != '#' and len(x) == 0:
            x.append(0)
            continue

    if len(x) == 0 or (len(x) == 1 and x[0]==2):
        return True
    else:
        return False

temp = ['9','3','4','#','#','1','#','#','#','2','#','6','#','#']

a = "9,3,4,#,#,1,#,#,#,2,#,6,#,#"

temp1 = a.split(',')
print temp1

if true_or_false(temp1):
    print "YO"