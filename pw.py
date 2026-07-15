import random

#DEFINIZIONE DELLE STRUTTURE DATI

#lista dei prodotti, 2 frutti e 2 ortaggi, così da avere un processo produttivo per i frutti e uno per gli ortaggi
prodotti = ["Fragole", "Pesche", "Spinaci", "Peperoni"]

#dizionario che indica il tempo raccoltà per ogni unità impostato in base al tempo di lavorazione ipotetico
# ( a mano e meccanico) diverso per ogni prodotto così da avere dati diversificati
tempo_raccolta_unità = {
      "Fragole":0.8,
      "Pesche" : 0.6,
      "Spinaci": 0.4,
      "Peperoni": 0.3,
   }

#dizionario che indica le capacità massime raccoglibili in una giornata impostate a un valore fisso (in Kg)
# scelto da me  
capacità_max_giornaliera = {
    "Fragole": 150,
    "Pesche" : 300,
    "Spinaci": 600,
    "Peperoni": 600,
}

# liste per differenziare frutti e ortaggi così da facilitarne l'utilizzo nelle funzioni dei processi di produzione
frutta = ["Fragole", "Pesche"]
ortaggi = ["Spinaci", "Peperoni"]

#DEFINIZIONE DELLE FUNZIONI

#Funzione per generare le quantità dei prodotti in modo casuale 
#Restituisce un dizionario che contiene i valori generati casualmente compresi nel range 
def quantità_casuale():
    return {
     "Fragole": random.randint (100, 300),
     "Pesche": random.randint ( 200, 500),
     "Spinaci": random.randint (300, 800),
     "Peperoni": random.randint (400, 900),
    }

#funzione per simulare la sequenza produttiva dei frutti
def produzione_Frutta():
    return [
        "Semina",
        "Raccolta Manuale",
        "Selezione qualita",
        "Stoccaggio"
        ]
   
#funzione per simulare la sequenza produttiva degli ortaggi 
def produzione_Ortaggi():
    return  [
        "Semina",
        "Raccolta Meccanica",
        "Selezione qualita",
        "Confezionamento"]
  
#funzione per definire in base al prodotto quale sequenza produttiva gli è associata
#nel caso di un frutto (fragola o pesca) verrà stampato il contenuto della funzione produzione_frutta
# nel caso di un ortaggio( spinaci o peperoni) verrà stampato il contenuto della funzione produzione_ortaggi
def Processo_Di_Produzione(nome_prodotto):
    if nome_prodotto in frutta:
     return produzione_Frutta()
     
    elif nome_prodotto in ortaggi:
     return produzione_Ortaggi()
      
    else: 
     return "prodotto selezionato non valido"
 
#Memorizzale quantità casuali generate per tutti i prodotti
#i valori ottenuti verranno usati dalle funzioni successive 
lotto_produzione = quantità_casuale()

#funzione per calcolare il tempo di produzione di un singolo prodotto  
def calcola_tempo_prodotto(nome_prodotto, lotto_produzione):
    tempo_unità = tempo_raccolta_unità[nome_prodotto]
    tempo_prodotto = lotto_produzione * tempo_unità
    return tempo_prodotto  

#funzione per calcolare il tempo totale delle produzioni di tutti i prodotti
def calcola_tempo_complessivo():
    tempo_complessivo = 0

    for prodotto in prodotti:
        tempo_prodotto = calcola_tempo_prodotto(prodotto, lotto_produzione[prodotto])
        tempo_complessivo += tempo_prodotto

    return tempo_complessivo

#funzione per convertire il tempo espresso in minuti, in ore
def minuti_in_ore(minuti):
    return minuti / 60

#funzione che calcola il numero totale di giorni necessari
#per completare la produzione di tutti i prodotti
def calcola_giorni_di_produzione_prodotto (nome_prodotto, quantita):
   capacità = capacità_max_giornaliera[nome_prodotto]
   giorni = quantita/capacità
   return giorni 

#funzione che calcola quanti giorni di lavoro complessivi servono per soddisfare le quantità massime necessarie per ogni prodotto
def calcola_giorni_di_produzione_complessivi():
    giorni_complessivi = 0

    for prodotto in prodotti:
        giorni = calcola_giorni_di_produzione_prodotto(prodotto, lotto_produzione[prodotto])
        giorni_complessivi += giorni

    return giorni_complessivi

# PARTE PRINCIPALE DEL PROGRAMMA



 #ciclo principale della simulazione dove viene eseguito il for
#per ogni prodotto vengono calcolati tempi, giorni di produzione e vengono visualizzati tutti i dati della simulazione
#elabora tutti i dati che ho creato per poter stampare e simulare il processo produttivo     
for prodotto in prodotti:
   tempo_prodotto = calcola_tempo_prodotto(prodotto, lotto_produzione[prodotto])
   giorni = calcola_giorni_di_produzione_prodotto(prodotto, lotto_produzione[prodotto])

   print ("Prodotto: ", prodotto)
   print ("Tempo di raccolta per unita: ", tempo_raccolta_unità[prodotto])
   print("Tempo Di Produzione:", round(tempo_prodotto, 2), "minuti", ", Conversione in Ore:", round(minuti_in_ore(tempo_prodotto), 1), "ore" ) 
   print ("Quantita: ", lotto_produzione[prodotto], "Kg")
   print ("Capacita prodotto al giorno: ", capacità_max_giornaliera[prodotto], "Kg/giorno")
   print ("Processo di produzione: ",Processo_Di_Produzione(prodotto))
   print("Giorni necessari:", round(giorni, 1), "Giorni")
   print ("   ")
  
#output finale sul tempo comlessivo del processo di produzione di tutti i prodotti
print("Giorni complessivi di produzione:", round(calcola_giorni_di_produzione_complessivi(),1),"Giorni")   
print("Tempo complessivo di produzione di tutti i prodotti:", round(calcola_tempo_complessivo(), 2), "minuti")
print("Tempo complessivo di produzione di tutti i prodotti:", round(minuti_in_ore(calcola_tempo_complessivo()), 1), "ore")


