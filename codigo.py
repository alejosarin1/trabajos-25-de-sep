# Determinar si es un triangulo obtuso,recto o agudo

# input


print("\n\n")
print("Determinar si es un triangulo obtuso,recto o agudo")
a = int(input("\ndigite el lado a: "))
b = int(input("\ndigite el lado b : "))
c = int(input("\ndigite el lado a : "))
while (a+b<c):
    
    print("NO ES UN TRIANGULO")
    a = int(input("\ndigite el lado a: "))
    b = int(input("\ndigite el lado b : "))
    c = int(input("\ndigite el lado a : "))
    
    

q= int(input("\ndigite el angulo A : "))
w= int(input("\ndigite el angulo B : "))
e= int(input("\ndigite el angulo C : "))



if e+w+q==180:
    print("NO ES UN TRIANGULO")
else:
    if (e ==w,q):
        print("\n El triangulo es recto")
    elif(q,w,e>90):
        print("ES UN TRIANGULO OBTUSO")
    elif((q,w,e<90)):
        print("ES UN TRIANGULO AGUDO")
    
        
    

    



