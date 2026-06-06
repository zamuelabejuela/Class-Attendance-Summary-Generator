import csv
from attendance_record import AttendanceRecord

class CSVReader:

    def read_csv(self, filename):
        records = []

        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    record = AttendanceRecord(
                        row["StudentName"],
                        row["Date"],
                        row["Term"],
                        row["Status"]
                    )

                    records.append(record)

            return records

        except FileNotFoundError:
            print("CSV file not found.")
            return []