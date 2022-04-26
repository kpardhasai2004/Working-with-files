z=open("C:/Users/Hi/Desktop/Reading files/places.txt","r")
# By using this you can access the file and read ("r") anything inside it .
print(z.readable())
#True
print(z.readline())
#Great Wall of China
print(z.readlines())
#['Great Wall of China\n', 'ChichÃ©n ItzÃ¡ El Castillo\n', 'Petra\n', 'Machu Picchu\n', 'Christ the Redeemer\n', 'Colosseum\n', 'Taj Mahal']
print(z.readlines()[0])
#Great Wall of China

print(z.readlines()[1])
#ChichÃ©n ItzÃ¡ El Castillo

print(z.readlines()[2])
#Petra

print(z.readlines()[3])
#Machu Picchu

print(z.readlines()[4])
#Christ the Redeemer

print(z.readlines()[5])
#Colosseum

print(z.readlines()[6])
#Taj Mahal
z.close()
#Use print(z.readline()[]) individually otherwise you may see IndexError
