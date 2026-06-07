"""gradebook.reports — build a printable report from grade records."""

from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    total = len(records)
    subjects = sorted(subjects_offered(records))
    averages = average_per_student(records)
    # students in alphabetical order
    student_names = sorted(averages.keys())
    top_name, top_avg = top_scorer(records)
    passing = passing_students(records, threshold=60.0)

    lines: list[str] = []
    lines.append("=== Gradebook Report ===")
    lines.append(f"Total records: {total}")
    lines.append(f"Subjects offered: {', '.join(subjects)}")
    lines.append("")
    lines.append("Averages:")
    # Align the names by padding to longest name length
    if student_names:
      width = max(len(n) for n in student_names)
    else:
      width = 0
    for name in student_names:
      avg = averages.get(name, 0.0)
      lines.append(f"  {name.ljust(width)} : {avg:.2f}")

    lines.append("")
    if top_name:
      lines.append(f"Top scorer: {top_name} ({top_avg:.2f})")
    else:
      lines.append("Top scorer: N/A")

    lines.append(f"Passing students (>= 60.0): {', '.join(passing)}")

    return "\n".join(lines)
