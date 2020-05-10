from CircleAreaComputations.Circle import Circle

objlst = []
objlst.append(Circle(2.8))
objlst.append(Circle(5.4))
objlst.append(Circle(3.6))
objlst.append(Circle(51.4))
objlst.append(Circle(8.1))
objlst.append(Circle(0.12))
objlst.append(Circle(99.12))
objlst.append(Circle(1))

totalArea = 0
for i in objlst:
    i.find_area()
    print(i.radius, i.area)
    totalArea = totalArea + i.area

print("Total Area :", totalArea)

# sort objects based on area
objlst.sort(key=lambda x: x.area, reverse=True)

print("Biggest Circle Area is :", objlst[0].area)
print("Smallest Circle Area is :", objlst[len(objlst) - 1].area)
