# Ce programme convertit des montants entre CAD - XOF - USD
def convdev(amount=0):
    dic_taux = {
        'CAD-XOF':400,
        'CAD-USD':0.71,
        'USD-XOF':570,
        'XOF-CAD':0.0025,
         'USD-CAD':1.408, 
         'XOF-USD':0.00175
    }

    choix = int(input("Veuillez faire votre choix de conversion"
    "(1:CAD-XOF , 2:CAD-USD , 3:USD-XOF , 4:XOF-CAD, 5:USD-CAD , 6:XOF-USD ): "))

    if choix == 1 :
        amountconv = dic_taux['CAD-XOF']*amount
        print(amount  ," CAD vaut ", amountconv, "XOF")
        
    elif choix == 2:
        amountconv = dic_taux['CAD-USD']*amount
        print(amount  ," CAD vaut ", amountconv, "USD")
        
    elif choix == 3:
        amountconv = dic_taux['USD-XOF']*amount
        print(amount  ," USD vaut ", amountconv, "XOF")
        
    elif choix == 4:
        amountconv = dic_taux['XOF-CAD']*amount
        print(amount  ," XOF vaut ", amountconv, "CAD")
    
    elif choix == 5:
        amountconv = dic_taux['USD-CAD']*amount
        print(amount  ," USD vaut ", amountconv, "CAD")
        
    elif choix == 6:
        amountconv = dic_taux['XOF-USD']*amount
        print(amount  ," XOF vaut ", amountconv, "USD")
    
    else:
        print()
        print("Choix incorrecte.Veuillez reessayer!")
        convdev(amount)
    

amount = float(input("Veuillez saisir le montant a convertir..."))
convdev(amount)