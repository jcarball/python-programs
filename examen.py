i=2
while i >= 0:
    print("*")
    i-=2
for n in range(-1, 1):
    print("%")
z=10
y=0
x=z > y or z==y

lst=[3,1, -1]
lst[-1] = lst[-2]
print(lst)

vals = [0,1,2]
vals[0], vals[1] = vals[1], vals[2]
print(vals)

nums=[]
vals = nums
vals.append(1)
print(nums)
print(vals)

nums=[]
vals = nums[:]
vals.append(1)
print(nums)
print(vals)

lst = [0 for i in range(1, 3)]
print(lst)

lst = [0,1,2,3]
x=1
for elem in lst:
    x*=elem
print(x)