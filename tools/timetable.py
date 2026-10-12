
TIMETABLE = [
    {"day": "Monday", "time": "09:00", "subject": "Mathematics", "room": "Room 101"},
    {"day": "Monday", "time": "10:00", "subject": "Programming", "room": "Lab 1"},
    {"day": "Tuesday", "time": "09:00", "subject": "Physics", "room": "Room 102"},
    {"day": "Tuesday", "time": "11:00", "subject": "Mathematics", "room": "Room 101"},
    {"day": "Wednesday", "time": "10:00", "subject": "Programming", "room": "Lab 1"},
    {"day": "Thursday", "time": "09:00", "subject": "Physics", "room": "Room 102"},
    {"day": "Friday", "time": "10:00", "subject": "Mathematics", "room": "Room 101"},
]


def get_classes_by_day(day):
    day = day.strip().capitalize()
    classes = [item for item in TIMETABLE if item["day"] == day]

    if not classes:
        return f"No classes found for {day}."

    result = [f"Classes on {day}:"]

    for item in classes:
        result.append(
            f'{item["time"]} - {item["subject"]} ({item["room"]})'
        )

    return "\n".join(result)


def get_subject_counts():
    counts = {}

    for item in TIMETABLE:
        subject = item["subject"]
        counts[subject] = counts.get(subject, 0) + 1

    result = ["Weekly subject-wise lecture count:"]

    for subject, count in sorted(counts.items()):
        result.append(f"{subject}: {count} lecture(s)")

    return "\n".join(result)


def get_total_classes(day=None):
    if day:
        day = day.strip().capitalize()
        count = sum(1 for item in TIMETABLE if item["day"] == day)
        return f"{day} has {count} class(es)."

    return f"Total classes in the timetable: {len(TIMETABLE)}"


def get_next_class(subject):
    subject = subject.strip().lower()

    matches = [
        item for item in TIMETABLE
        if subject in item["subject"].lower()
    ]

    if not matches:
        return f"No classes found for subject: {subject}."

    result = [f"Scheduled classes for {subject}:"]

    for item in matches:
        result.append(
            f'{item["day"]} at {item["time"]} - '
            f'{item["subject"]} ({item["room"]})'
        )

    return "\n".join(result)
