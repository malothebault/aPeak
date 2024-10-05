def get_date_int(hour):
    if 23 < hour <= 8:
        return 0
    elif 8 < hour <= 11:
        return 1
    elif 11 < hour <= 14:
        return 2
    elif 14 < hour <= 17:
        return 3
    elif 17 < hour <= 20:
        return 4 
    elif 20 < hour <= 23:
        return 5 

def get_url(spot: int = 0):
    if spot == 0:
        return "https://www.surf-sentinel.com/surf-report/france/ille-et-vilaine/saint-malo/le-sillon"
    elif spot == 1:
        return "https://www.surf-sentinel.com/surf-report/france/finistere/plomeur/la-torche"