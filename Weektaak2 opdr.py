



#Weektaak opdracht

#De code moet het GC% kunnen meten van een genetische sequentie


seq = str(input("What is the genetic sequence? "))

aantal_totaal = (seq.count("") - 1)
aantal_g = seq.count("G")
aantal_c = seq.count("C")

gc = float(((aantal_g + aantal_c) / aantal_totaal) * 100)

print(format(gc , '.1f') + str("%"))















