#---------------------------------------------------------------list------------------------------------------------------------------------------------------------------------------------------------------------------------#
"""insert takes two arguments with the help of this we can put out value according to ourself"""
# l=[1,2,3,4,5,6]
# l.insert(0,8)
# print(l)

"""append is basically used for add our value in last of our list as same as.extend and append methods basically used for add elements"""
# l=['1','2','3','4','5']
# k= ['6','7']
# l.append(k)    #add same as input in first list
# l.extend(k)    #add only elements in first list
# print(l)
# l.append(['5'])
# print(l)

"""pop and remove basically used for delete elements from our list but  there is difference in remove and pop, basically pop always take indexing and without taking argument it delete last items in our list
but remove works for specific items"""
# l=[1,2,3,4,5,6,7]
# l.pop()
# l.pop(4)
# l.remove(7)
# print(l)

"""sort and reverse methods used for arrange our list in specific order like assending order also in alphabetic order, reverse basically used for turn our list"""
# l=[5,3,6,4,7,2,8,1]
# l=['j','r','a','z','t']
# l.sort()
# l.reverse()
# print(l)

"""with the help of index method we can easily track any elements indexing for using purpose"""
# l=['ram', 1, 7.5,]
# k=l.index(7.5)
# print(k)

"""in a looping method if we are used enumerate methods we can access our valur and also it's index """
# l=['ram','sita','lakhsman','bharat','satrughan']
# for index, i in enumerate(l):
#     print(index,i)

"""we can used join methods for itrate our elements by using (,) commas and (-) dash also."""
# l=['ram','sita','lakhsman','bharat','satrughan']
# # k="-".join(l)
# k=','.join(l)
# print(k)

#--------------------------------------------------------------------------------------------------------tuple----------------------------------------------------------------------------------------------------#
"""Tuple is exactly same as List except that it is immutable. i.e once we creates Tuple object,we cannot perform any changes in that object."""
# t=10,20,30,40
# print(t)
# print(type(t))

"""in tuple we can access our items by using index (positive and negative)"""
# l=(10,20,30,40,50)
# print(l[2])

"""Once we creates tuple,we cannot change its content. Hence tuple objects are immutable."""
# t=(10,20,30,40,50)
# t[0]=60
# print(t)

"""in this tuple we can use mathematical operation like string"""
# t=(10,20,30,40)
# u=(50,60,70,80)
# v=u+t
# print(v)

"""in tuple we can use somr other methods like 'count()', 'len()', 'index()', 'sorted()','min()','max()',cmp()"""
# t=(5,3,4,1,2)
# k=t.count(2)
# print(len(t))
# print(t.index(4))
# s=sorted(t)
# print(s)

"""cmp(), methods used for comparision , if first index is greater and second is less, than it gives +1 , when second it greatest and or first is less than it gives -1, and when they are same it gives 0"""
# t1=(10,20,30)
# t2=(40,50,60)
# print(cmp(t1,t2))

#-----------------------------------------------------------------------------------set----------------------------------------------------------------------------------------------------------------#
"""inersection methods we can find common elemnts in our both sets"""
# s={1,2,3,4,5,6}
# d={1,2,3,7,8,9}
# print(s.intersection(d))

"""if we used defference methods for it gives different items from two sets"""
# s={1,2,3,4,5,6}
# d={1,2,3,7,8,9}
# print(s.difference(d))
# print(d.difference(s))

"""if we used union methods it gives me whole sets in one sets"""
# s={1,2,3,4,5,6}
# d={1,2,3,7,8,9}
# print(s.union(d))

#----------------------------------------------------------------------dictionary-----------------------------------------------------------------------------------------------#
"""basically dict is based on (unorder) and (key value) pair also used (round brackets({})),"""
