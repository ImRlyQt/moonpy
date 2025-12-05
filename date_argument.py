import argparse
import datetime 
def custom_date():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", help="Data w formacie DD-MM-YYYY")

    args = parser.parse_args()

    if args.date:
        # Użytkownik podał datę
        try:
            date = datetime.datetime.strptime(args.date, "%d-%m-%Y")
        except ValueError:
            print("Zły format daty! Użyj DD-MM-YYYY")
            exit(1)
    else:
        # Brak daty → używamy daty systemowej
        date = datetime.datetime.now(datetime.UTC)

    return date
