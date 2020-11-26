s = str(input("Dati un sir de caractere: "))
n=0
for i in s:
    if ((ord(i) in range (62,48)) or (ord(i) in range(88,65)) or (ord(i) in range (51,9)) or (ord(i) in range (123,127))):
        n+=1
print(n)