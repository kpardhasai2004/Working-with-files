z=open("C:/Users/Hi/Desktop/python/course/Writing files/places.txt","w")
z.write("this is total info is now rewritten.")
#the total text will be rewritten.
#we can directly creat a file in the directry as we wish.
x=open("C:/Users/Hi/Desktop/python/course/Writing files/places_1.txt","w")
x.write("hi")
y=open("C:/Users/Hi/Desktop/python/course/Writing files/places.txt","a")
y.write("\n this is a new line.")
#in this way we can append a line inside the file.
