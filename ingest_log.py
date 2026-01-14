import csv
from datetime import datetime

FILE_NAME = "ingest_log.csv"

def add_entry():
    title = input("Naziv materijala: ")
    media_type = input("Tip (audio/video): ")
    format_ = input("Format (npr. WAV, MP4): ")
    status = input("Status (OK / Needs review): ")
    note = input("Napomena: ")

    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, title, media_type, format_, status, note])

    print("Zapis spremljen.")

def show_log():
    try:
        with open(FILE_NAME, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Evidencija još ne postoji.")

def main():
    print("1 - Novi unos")
    print("2 - Pregled evidencije")

    choice = input("Odaberi opciju: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        show_log()
    else:
        print("Nepoznata opcija.")

if __name__ == "__main__":
    main()
