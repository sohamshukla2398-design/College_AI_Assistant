
import sqlite3

DB_NAME = "attendance.db"


def initialize_database():
    conn = sqlite3.connect(DB_NAME)

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)

        # Keep only the oldest record for each student and date
        conn.execute("""
            DELETE FROM attendance
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM attendance
                GROUP BY student_name, date
            )
        """)

        # Prevent future duplicates
        conn.execute("""
            CREATE UNIQUE INDEX IF NOT EXISTS
            unique_student_date
            ON attendance(student_name, date)
        """)

        conn.commit()

    finally:
        conn.close()


def mark_attendance(student_name, date, status):
    status = status.strip().capitalize()

    if status not in ("Present", "Absent"):
        return "Status must be Present or Absent."

    conn = sqlite3.connect(DB_NAME)

    try:
        conn.execute("""
            INSERT INTO attendance (student_name, date, status)
            VALUES (?, ?, ?)
        """, (student_name, date, status))

        conn.commit()
        return f"{student_name}: {status} on {date}"

    except sqlite3.IntegrityError:
        return (
            f"Attendance already exists for {student_name} "
            f"on {date}. Duplicate not added."
        )

    finally:
        conn.close()


def get_attendance_percentage(student_name):
    conn = sqlite3.connect(DB_NAME)

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*),
                   SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END)
            FROM attendance
            WHERE LOWER(student_name) = LOWER(?)
        """, (student_name,))

        total, present = cursor.fetchone()

    finally:
        conn.close()

    if not total:
        return f"No attendance records found for {student_name}."

    percentage = (present / total) * 100

    return (
        f"Student: {student_name}\n"
        f"Classes attended: {present}/{total}\n"
        f"Attendance percentage: {percentage:.2f}%"
    )

def get_attendance_records(student_name):
    conn = sqlite3.connect(DB_NAME)

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT date, status
            FROM attendance
            WHERE LOWER(student_name) = LOWER(?)
            ORDER BY date DESC
        """, (student_name,))

        records = cursor.fetchall()

    finally:
        conn.close()

    if not records:
        return f"No attendance records found for {student_name}."

    result = [f"Attendance records for {student_name}:"]

    for attendance_date, status in records:
        result.append(f"{attendance_date}: {status}")

    return "\n".join(result)


initialize_database()
