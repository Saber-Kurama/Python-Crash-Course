cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

print(1 == "1") 
print(1 == True) 
print(0 == False) 

for car in cars:
    if car == "bmw":
        print(car.upper())
    elif car == "subaru":
        print(car.title())
    else:
        print(car.upper())