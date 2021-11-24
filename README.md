# babbo_natale_segreto
Progetto Open Source per "babbo natale segreto" pivacy friendly.

Siete un gruppo di amici numeroso e volete farvi dei regali di Natale senza spendere troppo? Questo software fa per voi!
Sostituisce la versione "cartacea", il che è molto comodo nel caso in cui non vi sia modo di trovare un momento in cui si è tutti presenti prima delle festività, ed evita fastidiosi problemi di privacy derivanti dall'uso di siti esterni con dubbie doppie finalità.

Questo software è una versione acerba, ma funzionale di "Babbo Natale Segreto".

Occorrente:
1 file .csv (opzionale)
1 mail

Nel file .csv andranno inseriti i nomi dei partecipanti con le relative mail associate. Il formato è il seguente:
```
Nome,Mail
p1,mailp1
...,...
```

Avere un file .csv è opzionale: se volete basta creare direttamente all'interno del file una lista di tuple contenente i dati, es.:
```
[('Persona1', 'mailPersona1'), ('Persona2', 'mailPersona2'), ...]
```
Nella prima parte di codice, dopo aver letto il file csv e creato le strutture dati d'appoggio, il programma farà un'estrazione casuale, in modo che a cascuna persona, definita "Babbo", ne venga associata un'altra, definita "Bimbo".

Nella seconda parte di codice, si inseriscono i dati che predispongono l'invio di mail tramite un account di posta elettronica.
N.B.: è stato usato dotenv al fine di evitare l'esposizione di dati sensibili. Vi basta sostituire con i relativi dati richiesti.

Verrà, dunque, inviata dall'account scelto una mail a tutti i partecipanti con un messaggio personalizzato, in cui si specificherà a chi dovrà essere fatto il regalo.

Enjoy!



