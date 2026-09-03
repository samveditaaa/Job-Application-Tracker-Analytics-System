import sqlite3
import matplotlib.pyplot as plt

DB_NAME = "job_tracker.db"


def get_analytics_data():
    """Retrieve job application data for analysis."""

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM job_applications
        GROUP BY status
    """)

    status_data = cursor.fetchall()

    cursor.execute("""
        SELECT job_role, COUNT(*)
        FROM job_applications
        GROUP BY job_role
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)

    top_role = cursor.fetchone()

    cursor.execute("""
        SELECT COUNT(*)
        FROM job_applications
    """)

    total_applications = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM job_applications
        WHERE status = 'Interview'
    """)

    interview_count = cursor.fetchone()[0]

    connection.close()

    return (
        status_data,
        top_role,
        total_applications,
        interview_count
    )


def show_analytics():

    (
        status_data,
        top_role,
        total_applications,
        interview_count
    ) = get_analytics_data()


    print("\n========== JOB APPLICATION ANALYTICS ==========\n")

    print(f"Total Applications: {total_applications}")

    if top_role:
        print(
            f"Most Applied Job Role: "
            f"{top_role[0]} ({top_role[1]} applications)"
        )

    else:
        print("Most Applied Job Role: No data available")


    if total_applications > 0:

        interview_rate = (
            interview_count / total_applications
        ) * 100

        print(
            f"Interview Conversion Rate: "
            f"{interview_rate:.2f}%"
        )

    else:
        print("Interview Conversion Rate: 0%")


    print("\nApplications by Status:")

    for status, count in status_data:
        print(f"{status}: {count}")


    if status_data:

        labels = [
            row[0] for row in status_data
        ]

        values = [
            row[1] for row in status_data
        ]


        plt.figure(figsize=(8, 5))

        plt.bar(labels, values)

        plt.title(
            "Job Applications by Status"
        )

        plt.xlabel("Application Status")

        plt.ylabel("Number of Applications")

        plt.show()
