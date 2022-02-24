def max_product(list):
    max1=max([list[0], list[1], list[2]])
    max2=sorted([list[0], list[1], list[2]])[1]
    max3=min([list[0], list[1], list[2]])

    min1=max3
    min2=max2
    min3=max1

    for i in range(3, len(list)):
        if list[i] > max1:
            max3=max2
            max2=max1
            max1=list[i]
        elif list[i] > max2: # x < max1
            max3=max2
            max2=list[i]
        elif list[i] > max3:
            max3=list[i]

        if list[i] < min1:
            min3=min2
            min2=min1
            min1=list[i]
        elif list[i] < min2:
            min3=min2
            min2=list[i]
        elif list[i] < min3:
            min3=list[i]
  #  print(max1, max2, max3, min3, min2, min1)

    if (max2 < 0 and max1 >= 0) or (max3 < 0 and max2 >= 0):
        return(min1,min2,max1)
    elif (min3 < 0 and max3 >= 0) or (min2 < 0 and min3 >= 0):
        if max3==0 or (-min1/max3 >=max2/-min2):
            return(min1,min2,max1)
        else:
            return(max3,max2,max1)
    else:
        return(max3,max2,max1)

x = list(map(int, input().split()))

print(' '.join(map(str, max_product(x))))
