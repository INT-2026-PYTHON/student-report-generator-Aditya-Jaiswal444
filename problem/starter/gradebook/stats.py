"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    scores: dict[str, list[float]] = {}
    for r in records:
        name = r.get("name")
        score = r.get("score")
        if name is None or score is None:
            continue
        scores.setdefault(name, []).append(float(score))

    averages: dict[str, float] = {}
    for name, vals in scores.items():
        avg = sum(vals) / len(vals) if vals else 0.0
        averages[name] = round(avg, 2)
    return averages


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    return {r.get("subject") for r in records if r.get("subject") is not None}


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    averages = average_per_student(records)
    if not averages:
        return ("", 0.0)
    name, avg = max(averages.items(), key=lambda kv: kv[1])
    return (name, round(avg, 2))


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    averages = average_per_student(records)
    passing = [name for name, avg in averages.items() if avg >= threshold]
    return sorted(passing)
