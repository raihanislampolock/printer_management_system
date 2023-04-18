import json
import psycopg2
import hp_230
import hp_508_printer
import Brother
import schedule
import time


def insert_printer_details(printer_details):
    # Set up database connection
    conn = psycopg2.connect(
        host="20.198.153.150",
        database="raihan_local",
        user="consult",
        password="consult1234"
    )

    # Insert printer details into the database
    cursor = conn.cursor()

    for location, details in printer_details.items():
        ip = details['ip']
        details = json.dumps(details['percentage'])
        # black = details
        # cyan = details
        # magenta = details
        # yellow = details

        cursor.execute(
            "INSERT INTO printer_details (location, ip, details) VALUES (%s, %s, %s)",
            (location, ip, details)
        )

    # Commit changes and close the database connection
    conn.commit()
    cursor.close()
    conn.close()


hp_508 = hp_508_printer.printer_508_details()
hp_230 = hp_230.printer_230_details()
Brother = Brother.printer_brother_details()

insert_printer_details(hp_508)
insert_printer_details(hp_230)
insert_printer_details(Brother)
