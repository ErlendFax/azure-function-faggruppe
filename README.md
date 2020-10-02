# Azure Function Faggruppemøte 6. okt. 2020

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

1. Legg finalized_model.sav i root folder. (Dette er egentlig en modell trent på Titanic dataen, men lat som det er heftige "customer predictions")
2. Legg til scikit-learn i requirements.txt
3. Skriv om __ init __ .py slik at man kan ta inn "klasse", "alder", og "kjonn", last inn finalized_model.sav, og kjør en prediksjon. 
