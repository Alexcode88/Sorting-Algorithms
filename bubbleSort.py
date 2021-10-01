
def bubbleSort( list ):
    for i in range( 0, len(list) - 1, 1 ):
        for j in range( i + 1, len(list), 1 ):
            if list[i] > list[j]:
                aux = list[i]
                list[i] = list[j]
                list[j] = aux
    return list

result = bubbleSort( [10,5,6,1,8,2,3,4,7,9] )
print( result )


