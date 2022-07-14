l1=[1,8,7,2,21,21,15]
print(l1)

l1_sorted = l1.sort()
print(l1_sorted)

'''a function can work in either of two ways 
1. it can return the value for example here sorted l1 list might get stored in l1_sorted
2. it can sort the actual list 

HERE THE 1st IS NOT APPLICABLE 
WHEN WE WRIGHT l1.sort() - l1 ITSELF GET SORTED '''

l1.sort() #sorts the list
print(l1)

l1.reverse() #reverse the list
print(l1)

l1.append(9) #adds at the end of the list
print(l1)

l1.insert(0,120) #adds 120 at index 0
print(l1)

l1.pop(2)
print(l1) #deletes item in the index position 2 of the list

l1.remove(21) #will remove all the 21s from the list
print(l1)