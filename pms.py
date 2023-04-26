import json
import psycopg2
import hp_230
import hp_508_printer
import Brother
import canon_337
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
        # print(details)
        ip = details['ip']
        status = details['status']
        device_status = details['device_status']
        details = json.dumps(details['percentage'])

        cursor.execute(
            "INSERT INTO printer_details (location, ip, details, device_status, status) VALUES (%s, %s, %s, %s, %s)",
            (location, ip, details, device_status, status)
        )

    # Commit changes and close the database connection
    conn.commit()
    cursor.close()
    conn.close()


hp_508 = hp_508_printer.printer_508_details()
hp_230 = hp_230.printer_230_details()
Brother = Brother.printer_brother_details()
canon_337 = canon_337.get_cartridge_info()

insert_printer_details(hp_508)
insert_printer_details(hp_230)
insert_printer_details(Brother)
insert_printer_details(canon_337)