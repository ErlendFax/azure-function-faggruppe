# Azure Function Faggruppemøte 6. okt. 2020

Man skal __ikke__ klone dette repoet! (╯°□°）╯︵ ┻━┻

_Fokuser på READMEen, og ikke så mye på repoet. Det er noen unødvendige filer og folders i repoet, disse genereres automatisk i stegene 1-5 og kan overses. Hvis man står fast på steg nr. 8 kan man ta en titt på __ init __ .py._

### Oppsett:

Følg denne: https://docs.microsoft.com/en-us/azure/developer/python/tutorial-vs-code-serverless-python-01#visual-studio-code-python-and-the-azure-functions-extension
Her skal man lage en Azure bruker, laste ned VS Code, og installere Azure Function Core Tools.

### Lag en Azure Function:

Azure Function Core Tools, altså extentionen vi skal bruke er kraftig og vi gjør det meste i den.

1. I VS code, trykk på Azure extention knappen og logg inn i Azure (når du har logget inn skal du se mailen din nederst i VS Code).
2. Lag nytt Azure Function Project.
3. Lag en HTTP Trigger med ditt navn i seg, f.eks: HttpTriggerCustomerPredictionErlend, velg Anonymous (den er åpen, men det er enklest). 
4. Fortsatt i VS code: Deploy to Auzre, Create new Function App in Azure, vent ...
5. Når den er ferdig finner man den i Azure portal. Finn URLen og prøv den. 

Hvis det trengs: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions


### Lag en "smart" Azure Function:

6. Legg finalized_model.sav i root folder. Denne filen finner du her i repoet. (Dette er egentlig en modell trent på Titanic dataen, men lat som det er heftige "bank customer predictions") 💳💸🏧
7. Legg til _scikit-learn_ i requirements.txt
8. Skriv om __ init __ .py slik at man kan ta inn "klasse", "alder", og "kjonn", last inn finalized_model.sav, og kjør en prediksjon. 
