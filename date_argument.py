import argparse
import datetime 
def custom_date():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", help="Data w formacie DD-MM-YYYY")

    args = parser.parse_args()

    if args.date:
        try:
            date = datetime.datetime.strptime(args.date, "%d-%m-%Y")
        except ValueError:
            print("Zły format daty! Użyj DD-MM-YYYY")
            exit(1)
    else:
        date = datetime.datetime.now(datetime.UTC)

    return date
