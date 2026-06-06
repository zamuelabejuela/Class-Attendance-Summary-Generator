class ReportGenerator:

    def display_report(self, summary):

        print("\nATTENDANCE SUMMARY REPORT")
        print("=" * 60)

        for student, terms in summary.items():

            print(f"\nStudent: {student}")

            for term, counts in terms.items():

                print(f"\n{term}")

                print(f"Present : {counts['Present']}")
                print(f"Absent  : {counts['Absent']}")
                print(f"Late    : {counts['Late']}")
                print(f"Excused : {counts['Excused']}")

        print("\nEnd of Report")