def geet_user():
    print("Hello World"); 
    return "Hello World"

geet_user()

def get_user_name(name):
    """显示问候语 (文档字符串)"""
    name = name.title()
    print(f"Hello {name}")

name = "saber"
get_user_name(name);

print(get_user_name.__doc__)
print(name)


get_user_name(name= "saber");

def get_dog_name(name="kaka"):
    """显示小狗的名字"""
    print(f"Dog name is {name}")

    
