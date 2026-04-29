def bissextile(y):
    if y%4 == 0:
        if y%100 == 0:
            if y%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def jours(m,y):
    if m == 2:
        if bissextile(y)==True:
            return 29
        else:
            return 28
    elif m in [4,6,9,11]:
        return 30
    else:
        return 31

#On suppose date une liste de 3 elements. date = [year;month;day]
def date_v(date):
    y = int(date[0])
    m = int(date[1])
    print(type(m))
    d = int(date[2])
    if m>=1:
        if m<13:
            if jours(m,y) >= d:
                return True
    return False

def calendrier():
    y = input('Donnez une année ')
    m = input('Donnez un mois ')
    d = input('Donnez un jour ')
    date = [y,m,d]
    if date_v(date) == True:
        print('date valide')
    else:
        print('date non valide')

calendrier()