# Progetto PCTO 

# PCTO2021: Approccio serverless al processamento di dati provenienti da sensori 

## Obiettivi del progetto
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
> 
## Architettura (componenti software/hardware e loro interazione)
> Elenco architettature utilizzate:
> * Postgrees
> * Python
> * Lambda

### Elenco dei tool che utilizzate (non deve essere un tutorial, piuttosto usate link esterni)
> * Visual Studio code https://code.visualstudio.com/
> * DBeaver https://dbeaver.io/
> * AWS https://aws.amazon.com/it/
> * GitHub https://github.com/
>
## Simulazione in Python dei dati necessari all'applicazione
> Per il programma di simulazione si creano randomicamente tre temperature ambientali (1 per campo), la prima è compresa tra -2 e 15 gradi, la seconda e la terza aggiungono una variazione alla prima. Con la funzione "Schedule" si richiama ogni minuto la funzione "nodes_identifier" il cui scopo è quello di individuare il numero dei sensori e il campo di appartenenza. Il risultato di questa funzione viene inviato a un'altra funzione che simula i dati per ogni singolo sensore e vengono tradotti in dizionari. Infine questo dizionario viene trasformato in formato Json che verrà successivamente inviato all'API.
> 
> *Funzione schedule* 
> 
>     schedule.every(1).minutes.do(nodes_identifier)   
>    
>     while True:
>     
>     schedule.run_pending()
>     
> *Query per la visualizzazione dei sensori*
> 
>     query = "select id, field from sensor_status"
>     
> *Conversione da dizionazio a Json e invio all'API*
> 
>     json_data = json.dumps(data)
>     headers = {'content-type': 'application/json'}
>     x = requests.post("https://k1lcrvj5x8.execute-api.us-east-1.amazonaws.com/dev/field/stats", json_data, headers) 
## Struttura del database: schema ER e schema logico, eventuali vincoli di integrità referenziale
> In informatica, nell'ambito della progettazione dei database, il modello entity-relationship (detto anche schema E-R;in italiano)    
> è un modello teorico per la rappresentazione concettuale e grafica dei dati.  
> Tale diagramma e' composto da :  <br/>
> *Entita'*
> 
>       Classi di oggetti (fatti, cose, persone, ...) che hanno proprietà comuni ed esistenza autonoma ai
>       
>       fini dell'applicazione di interesse;  <br/> 
> *Associazioni*
> 
>       Relazioni, che rappresentano un legame tra due o più entità tramite chiavi primarie o esterne;  <br/>    
> 
> *Attributi* 
> 
>       che vanno a definire il livello di dettaglio con cui vogliamo rappresentare un' entita'.  <br/>  
>         
>       Lo schema logico non fa altro che prendere il concetto di schema E-R e rappresentarlo in modo grafico. 
>          
>Nel Database che abbiamo sviluppato il modello E-R sviluppato si presenta come tale:    
>   
>     Sensor_status(**id**, localitazion, field)    
>     Sensor_values(**sensor_id**, *fk_id*, vwc, gt, et, eu)  
>   
> In questo schema possiamo notare la relazione che sussiste tra le due entita' :  
>   
> La prima entita' dotata di attributi quali :  
> id : Chiave primaria ed id del sensore  
> localization : Coordinate del sensore  
> field : Campo in cui e' posizionato il sensore  
>   
> ![modelloersus](/assets/images/modello_er.PNG)
>  
> La seconta entita' e' dotati di attributi quali :  
> sensor id : chiave primaria della seconda entita', visualizza sempre l'id del sensore  
> fk_id : chiave esterna della seconda entita', legata alla chiave primaria di sensor_status  
> vwc : volumetric water content, contenuto volumetrico dell'acqua  
> gt : ground temperature, temperatura del terreno in cui e' presente il sensore  
> et : enviromental temperature, temperatura ambiente  
> eu : enviromental umidity, umidita' ambiente.  
>
## Lamba function per il data injection e per l’elaborazione dei dati nel database
> Sono presenti nel nostro progetto 3 lambda function, ognuna con una funzione specifica:
> * database_insert, la prima delle 3, che ha il compito di riconvertire il json ricevuto in dizionario, e inserire i singoli campi all'interno della tabella sensor_values del database;
> * database_nodes che, ricevendo il campo da un progranmma in python, seleziona da sensor_status l'id di ogni singolo sensore, e li manda indietro al programma;
> * stats_retriever, che, dopo aver ricevuto gli id dal programma, calcola con una query il minimo, massimo e media di ogni singolo elemento, ovvero vwc, gt, et e eu.
## Stato di avanzamento del progetto e sviluppi futuri
> * Simulazione dati: *terminato.*
> * Sviluppo API: *terminato.*
> * Sviluppo LAMBDA function: *terminato.*
> * Creazione database: *terminato.*
> * Visualizzazione dei dati nel database: *terminato.*
> * Implementazione di Amazon Alexa: *non terminato.*
## Considerazioni finali

## Il gruppo di lavoro
> Principi Simone: Referente gruppo, Creazione API Gateway e Codifica funzioni Lambda per l'inserimento dei dati nel database
> Maroni Michele: Creazione Database e Formattazione del ReadME
> Silveri Gianmaria: Simulazione dei dati e Invio all'API.

## Suddivisione delle ore di lavoro
> * 01/02/2021-06/02/2021: periodo di formazione su linguaggio Python e sul funzionamento del Cloud.
> * 08/02/2021-13/02/2021: 

## NOTA BENE:
I file inseriti sono solamente delle versioni in development, e non rappresentano in alcun modo il prodotto finale.

## Suddivisione compiti
> Principi Simone: Referente gruppo, Creazione API Gateway e Codifica funzioni Lambda per l'inserimento dei dati nel database
> Maroni Michele: Creazione Database e Formattazione del ReadME
> Silveri Gianmaria: Simulazione dei dati e Invio all'API.
