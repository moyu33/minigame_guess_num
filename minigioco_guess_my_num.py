#importazione moduli random & time
import random
import time

#inizializzazione variabili
tentativi_rimasti = 3
scelte_effettuate = []

#ciclo per gestire scelta user
while True:    
    try:
        scelta_user = int(input("Scegli un numero tra 1 e 10: "))
        if scelta_user < 1 or scelta_user > 10:
            print("Per favore inserisci un valore valido tra 1 e 10.") 
            continue
        break
    except ValueError:
        print("Per favore inserisci un valore numerico valido.")
        continue 

#ciclo per gestire scelta computer
while tentativi_rimasti > 0:        
    print("Sta pensando...")
    time.sleep(4)
    scelta_computer = random.choice(range(0, 11)) 

    scelte_effettuate.append(scelta_computer)
    
#ciclo per evitare che il computer scelga numeri scelti in precedenza
    while scelta_computer in scelte_effettuate:
            scelta_computer = random.choice(range(0, 11)) 

    print("La scelta del computer è stata {}.".format(scelta_computer))

#chiusura gioco computer indovina
    if scelta_user == scelta_computer:
        print("Il computer ha indovinato!")
        print("Game Over!")
        break
    else:
        tentativi_rimasti -= 1
        print("Il computer non ha indovinato, gli rimangono {} tentativi.".format(tentativi_rimasti))

#chiusura gioco computer esaurisce tenativi
if tentativi_rimasti == 0:
    print("Al computer rimangono {} tentativi. L'umano vince.".format(tentativi_rimasti))
    print("Game Over!")

input("Press Enter to exit...")