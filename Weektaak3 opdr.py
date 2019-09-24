
##Weektaak 3 opdracht

#Concludeer of de sequentie een DNA sequentie is of een eiwitsequentie
seq = str(input("Please enter a DNA or a protein sequence here. "))

aantal_G = int(seq.count("G"))
aantal_C = int(seq.count("C"))
aantal_T = int(seq.count("T"))
aantal_A = int(seq.count("A"))

gtac = aantal_G + aantal_C + aantal_T + aantal_A
total = int(seq.count("") - 1)

if gtac == total:
    print("This could be a DNA sequence. ")

else:
    print("This could be a protein sequence. ")

#Print de lengte van de sequentie
print(str("The length of the sequence is ") + str(total))

#Vergelijkt de lengte van de Eiwitsequentie met de bijbehorende mRNA sequentie
if gtac != total:
    mrna = input("Please enter the mRNA sequence that fits the protein sequence ")
    total_mrna = mrna.count("") - 1
    print(str("The protein sequence has a length of ") + str(total) + str(", and the mRNA sequence has a length of ") + str(total_mrna) + str("."))
    
#Tel het aantal aminozuren D, E, R en K in de eiwitsequentie
    aantal_D = int(seq.count("D"))
    aantal_E = int(seq.count("E"))
    aantal_R = int(seq.count("R"))
    aantal_K = int(seq.count("K"))
    totaal_amino = aantal_D + aantal_E + aantal_R + aantal_K
    print(str("The Amino acids (D, E, R and K) in the protein sequence are with an amount of ") + str(totaal_amino))

#Het % DERK t. o. v. het totaal aminozuren
    derk = int(100 / (total / totaal_amino))
    print(str("The percentage DERK amino acids is ") + str(derk) + str("%"))

#Het verschil tussen de RK positieve lading en de DE negatieve lading
    rk = aantal_R + aantal_K
    de = aantal_D + aantal_E
    dif = rk - de
    print(str("The sequence has a + or - energy of ") + str(dif))




















