import datetime
import math

def moon_phase():
    """
    Zwraca nazwę obecnej fazy Księżyca.
    Algorytm Conwaya – szybki i wystarczająco dokładny.
    """
    now = datetime.datetime.now(datetime.UTC)
    year = now.year
    month = now.month
    day = now.day

    if month < 3:
        year -= 1
        month += 12

    # obliczenia wg Conwaya
    k1 = int(365.25 * (year + 4712))
    k2 = int(30.6 * (month + 1))
    k3 = int(((year // 100) + 49) * 0.75) - 38

    jd = k1 + k2 + day + 59  # julian day
    jd -= k3  # korekta

    moon = (jd - 2451550.1) / 29.530588853
    moon -= int(moon)
    age = moon * 29.530588853  # wiek księżyca w dniach

    # fazy
    if age < 1.84566:
        return "Nów 🌑"
    elif age < 5.53699:
        return "Sierp przybywający 🌒"
    elif age < 9.22831:
        return "Pierwsza kwadra 🌓"
    elif age < 12.91963:
        return "Garbaty przybywający 🌔"
    elif age < 16.61096:
        return "Pełnia 🌕"
    elif age < 20.30228:
        return "Garbaty ubywający 🌖"
    elif age < 23.99361:
        return "Ostatnia kwadra 🌗"
    elif age < 27.68493:
        return "Sierp ubywający 🌘"
    else:
        return "Nów 🌑"

def moon_phase_precise():
    """
    Zwraca aktualną fazę Księżyca z wysoką dokładnością.
    Algorytm oparty na epoce J2000.
    """

    now = datetime.datetime.now(datetime.UTC)

    # Julian Date
    def julian_date(dt):
        return (dt.timestamp() / 86400.0) + 2440587.5

    jd = julian_date(now)

    # Dni od epoki J2000
    days = jd - 2451549.5

    # Średnia anomalia Słońca
    sun_mean_anom = math.radians((357.5291 + 0.98560028 * days) % 360)

    # Średnia długość Księżyca
    moon_mean_long = math.radians((218.316 + 13.176396 * days) % 360)

    # Średnia anomalia Księżyca
    moon_mean_anom = math.radians((134.963 + 13.064993 * days) % 360)

    # Elongacja
    elong = math.radians((297.850 + 12.190749 * days) % 360)

    # Faza księżyca (0 = nów, 0.5 = pełnia)
    phase = (1 - math.cos(moon_mean_anom - sun_mean_anom)) / 2

    # Dobór nazwy
    if phase < 0.03:
        return "Nów 🌑"
    elif phase < 0.23:
        return "Sierp przybywający 🌒"
    elif phase < 0.27:
        return "Pierwsza kwadra 🌓"
    elif phase < 0.48:
        return "Garbaty przybywający 🌔"
    elif phase < 0.52:
        return "Pełnia 🌕"
    elif phase < 0.73:
        return "Garbaty ubywający 🌖"
    elif phase < 0.77:
        return "Ostatnia kwadra 🌗"
    elif phase < 0.97:
        return "Sierp ubywający 🌘"
    else:
        return "Nów 🌑"


print(moon_phase_precise())


# przykład użycia:
print(moon_phase())

