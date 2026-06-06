from csv_reader import CSVReader
from attendance_processor import AttendanceProcessor
from report_generator import ReportGenerator

def main():

    filename = input("Enter CSV filename: ")

    reader = CSVReader()
    records = reader.read_csv(filename)

    print(records[0].student_name)
    print(records[0].term)
    print(records[0].status)

    processor = AttendanceProcessor()
    summary = processor.generate_summary(records)

    report = ReportGenerator()
    report.display_report(summary)

if __name__ == "__main__":
    main()