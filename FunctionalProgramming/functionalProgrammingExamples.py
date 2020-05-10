
#square each number
#given
alst=[5,1,3,7]

#list comp : \
blst=[e**2 for e in alst]
print("list comp::",blst)
#Map algo  : \
blst=list(map(lambda x : x*x, alst))
print("map comp::",blst)


print()
#extract only EVEn numbers

print("extract even numbers")
alst=[10,15,20,30,63,51,40]

#list comp    : \
blst=[ e  for e in alst if e%2==0 ]
print("list comp::",blst)


#map algo     : \
blst=list(map(lambda x : x%2==0 , alst))
print("map comp::",blst)
#filter algo  : \
blst=list(filter(lambda x : x%2==0 , alst))
print("filter comp::",blst)


#whenever our expression are BOOLEAN we have
#to use FILTER instead of MAP

