# commento singola linea

"""
commento 
multi
linea
"""

dichiarazioneDiUnaVariabileNumerica = 1 # sì, non ci sono terminatori di linea
dichiarazioneDiUnaStringa = "si possono anche usare gli apostrofi 'le virgolette possono includere apostrofi ma non viceversa'"
dichiarazioneDiUnArray = []

dichiarazioneDiUnArray += 1
dichiarazioneDiUnArray.append(2) # --> 3
dichiarazioneDiUnArray[1] # --> secondo elemento: 2
dichiarazioneDiUnArray[-1] # --> ultimo elemento: 2
del dichiarazioneDiUnArray[0] # --> rimuovo il primo elemento: [2]
# gli array in python sono una sorta di linked list, e infatti il nome più corretto sarebbe lista

import time # importazione librerie
from time import daylight # importazione di una singola funzione da una libreria/programma

def nomeFunzione(argomento):

    return str(argomento) # converto l'argomento in stringa

print("questo è un argomento: " + nomeFunzione(100)) # le stinghe si possono concatenare con un +
print("questo è un argomento: {}".format(nomeFunzione(100))) # altro modo per formattare le stringhe

# LOOPS

# while:
while """condizione""":
    # codice

# for con iteratore da 0 a 9
for i in range(10):
    # codice

# for con iteratore da 1 a 10
for i in range(1, 11):
    # codice

# for con iteratore da 1 a 10 con incrementi di 2
for i in range(1, 11, 2):
    # codice

# for each con iteratore da 'c' a 'o'
parola = "ciao"
for lettera in parola:
    # codice

# IF

eta = 17 # senza l'accento
if eta >= 18:
    print("maggiorenne")
elif eta < 18 and eta >= 0:
    print("minorenne")
else:
    print("ti mancano " + str(int(eta) * -1) + " anni per nascere")

# INPUT DA UTENTE

domanda = "inserisci il numero di biglietti: "
numeroDiBiglietti = input(domanda)

try:
    numeroDiBiglietti = int(numeroDiBiglietti)
except ValueError: # se la funzione int non riesce a convertire il valore di input
    print("errore")
else:
    print("stampa di " + numeroDiBiglietti + " bigletti in corso ...")


# CLASSI

class Lavoratori:

	# variabili globali
	dominio = ''
	numeroLavoratori = 0

	# funzione principale
	def __init__(self, nome, cognome, anni):
		
		# variabili comuni a tutti i metodi
		self.nome = nome
		self.cognome = cognome
		self.anni = anni

		Lavoratori.numeroLavoratori += 1

	# metodi secondari
	def mail(self):

		return self.nome + '.' + self.cognome + self.dominio

	@classmethod
	def cambioDominio(cls, dominio):
		# al posto dell'instance prende in automatico la classe
		cls.dominio = dominio

	@staticmethod	
	def potenza(base, esponente):
		# static = non dipende da variabili di classi o instance
		return base ** esponente

id_1 = Lavoratori('Mario', 'Rossi', 40) 
id_2 = Lavoratori('Alberto', 'Pini', 30)
id_3 = Lavoratori('Giuseppe', 'Rigano', 20)

# è come fare: Lavoratore(id_1, 'Mario', 'Rossi', 40)

print('\n\n')

Lavoratori.cambioDominio('@gmail.com')

print(id_1.mail())	# id_1 viene passato a mail come 'self'
print(id_2.mail())	
print(id_3.mail())	# finiranno con @gmail.com

print('\n')

print('Il numero di lavoratori è ' + str(Lavoratori.numeroLavoratori))

print('\n')

dueAllaTerza = Lavoratori.potenza(2, 3)

print('due elevato a tre (2^3) fa ' + str(dueAllaTerza))

print('\n\n')
