my_set = {1,2,2,3,4,4,4}
print("St :", my_set)
my_set.add(5)
print("Updated Set:", my_set)
set1 = my_set
set2 = {2,4,4,6}
print("\nSet 1",set1)
print("Set 2", set2)
print("Difference")
print(set1.difference(set2))
print("Symmeteric Difference")
print(set1.symmetric_difference(set2))
setc1 = {"green","blue"}
setc2 = {"blue", "yellow"}
print("original sets:")
print(setc1)
print(setc2)
setc = setc1.union(setc2)
print("\nUnion of above sets:")
print(setc)
setc1 = {"green", "blue"}

setc2 = {"blue", "yellow"}

print("Original sets:")

print(setc1)

print(setc2)

setc = setc1.union(setc2)

print("\nUnion of above sets:")

print(setc)

setx = {"green", "blue"}

sety = {"blue", "yellow"}

print("Original set elements:")

print(setx)

print(sety)

print("\nIntersection of two said sets:")

setz = setx.intersection(sety)

print(setz)


t = (1, 2, 3)
t2 = 1, 2, 3
t3 = (5,)
t4 = ()
print(t[0])
print(t[-1])       
print(t[0:2])      

t = (1, 2, 3)
t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)    
print(t1 * 2)     

t = (1, 2, 3, 2, 4)

print(len(t))      
print(max(t))      
print(min(t))      
print(sum(t))     

t = (1, 2, 3, 2, 4)

print(t.count(2))   
print(t.index(3))   

t = (1, 2, 3)

print(2 in t)   
print(5 not in t)  

for i in t:
    print(i)

t = (10, 20, 30)

a, b, c = t

print(a)  
print(b)   
print(c) 

t = (1, (2, 3), (4, 5))

print(t[1])
print(t[1][0])
t = (1, 2, 3)
t = (1, 2, 3)
print(sorted(t))  
print(any(t))      
print(all(t))     
l = list(t)
t2 = tuple(l)
d = {(1, 2): "point"}
x = (1)
print(type(x))  

x = (1,)
print(type(x))   