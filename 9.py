list1=[5,10,15,20,25,30]
list2=list1
id(list1)==id(list2)


list2=list1.copy()
id(list1)==id(list2)

#True False


#This code does the following:

#1. list1 = [5, 10, 15, 20, 25, 30]: Initializes a list named list1 with the values [5, 10, 15, 20, 25, 30].

#2. list2 = list1: Assigns list2 the reference to the same list as list1. They are now aliases, pointing to the same object in memory. So, id(list1) == id(list2) will be True.

#3. list2 = list1.copy(): Creates a new list list2 with the same elements as list1 using the copy() method. Now, list2 is a separate list in memory, and id(list1) == id(list2) will be False.