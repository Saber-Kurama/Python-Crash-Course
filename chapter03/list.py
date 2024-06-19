saber_list = [1];
print(saber_list);
saber_list[0]= 2;
print(saber_list);

saber_list.append(3);
print(saber_list);

saber_list.insert(1,4);
print(saber_list);

saber_list = [1,2,3,4,5,6,7,8,9,100, 30];
del saber_list[3];
print(saber_list);

del_num = saber_list.pop(3);
print(del_num);
print(saber_list);

saber_list.remove(8);
print(saber_list);

saber_list.reverse();
print(saber_list);

sorted_list_1 = sorted(saber_list);
print(sorted_list_1);
print(saber_list);
saber_list.sort();
print(saber_list);

print(len(saber_list));
