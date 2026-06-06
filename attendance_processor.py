class AttendanceProcessor:

    def generate_summary(self, records):

        summary = {}

        for record in records:

            student = record.student_name.strip()
            term = record.term.strip().title()
            status = record.status.strip().title()

            if student not in summary:
                summary[student] = {
                    "Midterm": {
                        "Present": 0,
                        "Absent": 0,
                        "Late": 0,
                        "Excused": 0
                    },
                    "Final": {
                        "Present": 0,
                        "Absent": 0,
                        "Late": 0,
                        "Excused": 0
                    }
                }

            summary[student][term][status] += 1

            print("Student:", record.student_name)
            print("Term:", record.term)
            print("Status:", record.status)
            print("\n")

        return summary