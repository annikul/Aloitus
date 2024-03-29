# TOOLS FOR DATE AND TIME CALCULATIONS
# ====================================

# LIBARARIES AND MODULES
import datetime # Python's internal date-time library

def datediff(d1, d2):  # muuttuja on datediff voi olla minkä niminen vain, sekä on parametrejä d1 ja d2 voi olla mitä vain
    """Calculates the  difference between two dates in days  (tämä on ohje mitä docstring tekee)

    Args:       # Tämä on docstring
        d1 (str): A date in ISO format YYYY-MM-DD   # str = voi olla vain teksti. 10-12 on tekstiä viivan takia.
        d2 (str): A date in ISO format YYYY-MM-DD

    Returns: 
        int: absolute difference in days  (Tämä on mitä docstring palauttaa)
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")  # eka pvä. Pitää olla 2 datetime eka on moduulista toka on tähä tarkotettu
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")   # toka pvä
    difference = abs((d2 - d1).days)    # abs = jos menee negatiiviseksi abs muuttaa sen positiiviseksi. Muuttaa eron päiviksi. Voisi muuttaa myös vuosiksi, kuukausiksi
    return difference

def timediff(t1, t2):
    """Calculates the  difference between two time values  (tämä on ohje mitä docstring tekee)

    Args:
        t1 (str): time value in format HH:MM:SS
        t2 (str): time value in format HH:MM:SS

    Returns:
        float: time difference in hours  (Tämä on mitä docstring palauttaa) # float on liukuluku arvo
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")

    # Function calcultates a timedelta which support only seconds or microseconds
    seconds = abs((t2 - t1).seconds)
    hours = seconds / 3600 # minute 60 seconds, hour 60 minutes
    return hours

def datediff2(d1, d2, unit):
    """Returns difference between 2 dates in chosen unit (day, month or year)

    Args:
        d1 (str): 1 st date in ISO format (YYYY-mm-dd)
        d2 (str): 2 nd date in ISO format (YYYY-mm-dd)
        unit (str): unit to return

    Returns:
        float: difference between dates in desired units
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")   
    difference = abs((d2 - d1).days) # Timedelta in days
    units = {'day':1, 'year': 365}  # Dictionary for unit dividers # units = muuttuja, meidän sanakirja. Jos vastaus on day jaetaan 1 jos vuosi jaetaan 365    
    divider = units[unit]           # Choose by unit argument # units sanakirja josta haetaan unit.
    value = difference / divider    # arvo mikä palautetaan
    return value

def timediff2(t1, t2, unit):
    """Calculates the  difference between two time values in chosen unit (day, minute or second)(tämä on ohje mitä docstring tekee)

    Args:
        t1 (str): time value in format HH:MM:SS
        t2 (str): time value in format HH:MM:SS
        unit (str: unit to return 

    Returns:
        float: time difference in chosen units  (Tämä on mitä docstring palauttaa)
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    units = {'hour': 3600, 'minute': 60, 'second': 1}
    seconds = abs((t2- t1).seconds)
    divider = units[unit] # Choose divider according to unit argument
    value = seconds / divider
    return value

if __name__ == '__main__': # Kehityksen aikaisia kokeiluja / toimivuuden varmistamisia. (Että funktiot toimii) Nämä testit voi poistaa

    # Let's test date difference
    date1 = '2023-03-21'
    date2 = '2023-03-17'

    ero = datediff2(date1, date2, 'day')
    print('ero oli', ero, 'päivää')

    # Let's test time difference
    time1 = '10:00:00'
    time2 = '15:25:00'
    ero = timediff2(time1, time2, 'minute')
    print('ero oli', ero, 'minuuttia')
   

   # Esimerkki  docstring käytöstä kun laitat vain datediff() menet () kohdalle se kertoo mitä tehdä
   # datediff('1987-01-01','2023-04-14') 
