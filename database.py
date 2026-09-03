import sqlite3

DB_NAME = "job_tracker.db"


def get_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DB_NAME)


def create_table():
    """Create the job applications table."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            job_role TEXT NOT NULL,
            location TEXT,
            application_date TEXT NOT NULL,
            status TEXT NOT NULL,
            salary TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_application(company, job_role, location,
                    application_date, status, salary):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO job_applications
        (company, job_role, location, application_date, status, salary)

        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        company,
        job_role,
        location,
        application_date,
        status,
        salary
    ))

    connection.commit()
    connection.close()


def get_all_applications():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM job_applications
        ORDER BY application_date DESC
    """)

    applications = cursor.fetchall()

    connection.close()

    return applications


def update_status(application_id, new_status):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE job_applications
        SET status = ?
        WHERE id = ?
    """, (
        new_status,
        application_id
    ))

    connection.commit()
    connection.close()


def delete_application(application_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM job_applications
        WHERE id = ?
    """, (application_id,))

    connection.commit()
    connection.close()
