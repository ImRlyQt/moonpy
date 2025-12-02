import datetime

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

# przykład użycia:
print(moon_phase())

