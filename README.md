# Progetto PCTO 

## Tema 1
> Creare un software in python che possa simulare dei nodi dove ogni nodo
> misura:
> - contenuto volumetrico di acqua (valori compresi tra 0 ed 1)
>
> - Temperatura del suolo (-40, + 120°C)
>
> - Temperature ambientale (-40, + 120°C)
>
> - Umidità Ambientale (0-100%)
>
> Ogni nodo invia anche i dati del tempo di acquisizione e della posizione
> geografica di acquisizione (latitudine e longitudine), un id unico che lo
> identifica ed anche il nome del campo in cui il nodo è situato
>
> Ogni nodo invia i dati ogni x minuti all’API gateway
>
> I dati devono essere «credibili»

## Sviluppo
> Come prima cosa si è creato un database denominato "lavoro PTCO".
> Successivamente si sono create 2 tabelle (sensor_status, sensor_value) le quali contengono i seguenti campi:
> 1. sensor_status
> * Id: (serial) Chiave autoincrementata.
> * Localization: (geometry) Latitudine e longitudine della posizione del sensore.
> * Field: (int) Numero del campo in cui si trova il sensore.
> 
> 2. sensor_values
> * Id: (serial) Chiave autoincrementata, questa volta si riferisce all'Id dei valori
> * VWC: (float) Contenuto volumetrico dell'acqua.
> * GT: (float) Temperatura del terreno.
> * ET: (float) Temperatura dell'ambiente.
> * EU: (numeric) Umidità ambientale.
> * Acquisition: (timestamp) orario di acquisizione del dato.
> * FK_Id: (serial) chiave esterna collegata alla chiave Id di sensor_status: viene importata questa chiave esterna poichè la relazione tra le tabelle è 1 a N.
> 
>La tabella sensor_status si occupa della posizione del sensore e in quale campo è situato, questa tabella è stata creata per evitare la ridondanza dei dati di posizione inseriti all'interno della tabella ogni volta che si rilevava il dato.
>
>La tabella sensor_value si occupa, invece, dell'immagazzinamento dei dati tecnici relativi ai valori misurati

## NOTA BENE:
I file inseriti sono solamente delle versioni in development, e non rappresentano in alcun modo il prodotto finale.

## Suddivisione compiti
> Principi Simone: Referente gruppo, Creazione API Gateway e Codifica funzioni Lambda per l'inserimento dei dati nel database
> Maroni Michele: Creazione Database e Formattazione del ReadME
> Silveri Gianmaria: Simulazione dei dati e Invio all'API.
