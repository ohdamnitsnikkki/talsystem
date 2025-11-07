# Skapa lista till de binära elementen

binar_lista = []

# Tar in tre tal från användaren
tal1 = int(input("Ange första talet: "))
tal2 = int(input("Ange andra talet: "))
tal3 = int(input("Ange tredje talet: "))

# Omvandlar varje tal till binärt tal och lägger till i listan

binar_lista.append(bin(tal1))
binar_lista.append(bin(tal2))
binar_lista.append(bin(tal3))

print("De binära talen är: ", binar_lista)