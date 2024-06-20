for value in range(1, 21):
    print(value)

nums = []
for value in range(1, 100):
    nums.append(value)    
print(nums);

# 通过给 range() 函数指定第三个参数来创建⼀个列 表，其中包含 1〜20 的奇数；再使⽤⼀个 for 循环将这些数打印出 来。
for value in range(1, 20, 2):
    print(value)

squares = [value**2 for value in range(1, 11)]
print(squares)

# 立方
cubes = [value**3 for value in range(1, 11)]
print(cubes)


names = ['alice', 'bob', 'carol', 'dave', 'erin', 'fiona']
splice_names = names[1:3]
print(splice_names)
splice_names = names[4:1]
print(splice_names)
splice_names = names[1:-1]
print(splice_names)
splice_names = names[:3]
print(splice_names)
splice_names = names[2:]
print(splice_names)
names[2] = "saber"
print(names)
print(splice_names)

names = [1, "saner"]
print(names)

point = (1,2)
print(point[0])