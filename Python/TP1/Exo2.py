def mesImpots(revenu):
    Taux=[[158123,0.45],[73517,0.41],[25710,0.3],[10084,0.11]]
    impot = 0
    for i in range(len(Taux)):
        if revenu>Taux[i][0]:
            impot = impot + (revenu - Taux[i][0]-1) * Taux[i][1]
            revenu = revenu-(revenu-Taux[i][0])
        print('Test impot = ', impot, '  Test revenu = ', revenu)
    print('Le montant de vos impots est de ', impot,'€')

revenus = input("Combien gagnez vous annuellement? ")
revenu = int(revenus)

mesImpots(revenu)
