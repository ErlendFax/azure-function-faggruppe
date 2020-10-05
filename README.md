# Azure Function Faggruppemøte 6. okt. 2020

Man skal __ikke__ klone dette repoet! (╯°□°）╯︵ ┻━┻

_Fokuser på READMEen, og ikke så mye på repoet. Det er noen unødvendige filer og folders i repoet, disse genereres automatisk i stegene 1-5 og kan overses. Hvis man står fast på steg nr. 8 kan man ta en titt på __ init __ .py._

### Mål for faggruppemøtet:

1. Lage sin egen Azure Function med VS code sin "Azure Function" extension, og deretter se den dukke opp i Portal (https://portal.azure.com/#home).
2. Gjøre Azure Function'en "smart", lage funksjonalitet som mottar inputs og returnerer en prediksjon.

### Oppsett:

Følg denne: https://docs.microsoft.com/en-us/azure/developer/python/tutorial-vs-code-serverless-python-01#visual-studio-code-python-and-the-azure-functions-extension
Her skal man lage en Azure bruker, laste ned VS Code, og installere Azure Function Core Tools. 

### Lag en Azure Function:

1. I VS code, trykk på Azure extension knappen og logg inn i Azure.
2. Lag nytt Azure Function Project.
3. Lag en HTTP Trigger med ditt navn i seg, f.eks: HttpTriggerCustomerPredictionErlend, velg Anonymous (den er åpen, men det er enklest). 
4. Fortsatt i VS code: Deploy to Auzre, Create new Function App in Azure, vent ...
5. Når den er ferdig finner man den i Azure portal. Finn URLen og prøv den. 

Hvis det trengs: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions


### Lag en "smart" Azure Function:

6. Legg finalized_model.sav i root folder. Denne filen finner du her i repoet. (Dette er egentlig en modell trent på Titanic dataen, men lat som det er heftige "bank customer predictions") 💳💸🏧
7. Legg til _scikit-learn_ i requirements.txt
8. Skriv om __ init __ .py slik at man kan ta inn "klasse" (1, 2, eller 3), "alder", og "kjonn" (0 eller 1), last inn finalized_model.sav, og kjør en prediksjon. 
