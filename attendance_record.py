class AttendanceRecord:
    VALID_STATUSES = {"present", "absent", "late", "excused"}
    VALID_TERMS    = {"midterm", "final"}
 
    def __init__(self, student_name: str, date: str, term: str, status: str):
        self.student_name = student_name.strip()
        self.date         = date.strip()
        self.term         = term.strip().lower()
        self.status       = status.strip().lower()
 
    def is_valid(self) -> bool:
        return (
            bool(self.student_name)
            and bool(self.date)
            and self.term   in self.VALID_TERMS
            and self.status in self.VALID_STATUSES
        )
 
    def __repr__(self):
        return (
            f"AttendanceRecord(name={self.student_name!r}, "
            f"date={self.date!r}, term={self.term!r}, status={self.status!r})"
        )