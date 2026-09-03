from database import (
    create_table,
    add_application,
    get_all_applications,
    update_status,
    delete_application
)

from analytics import show_analytics


def add_new_application():

    print("\n--- Add Job Application ---")

    company = input("Company Name: ")
    job_role = input("Job Role: ")
    location = input("Location: ")
    application_date = input("Application Date (YYYY-MM-DD): ")

    print("\nApplication Status:")
    print("1. Applied")
    print("2. Interview")
    print("3. Rejected")
    print("4. Selected")

    status_choice = input("Enter choice (1-4): ")

    status_options = {
        "1": "Applied",
        "2": "Interview",
        "3": "Rejected",
        "4": "Selected"
    }

    status = status_options.get(
        status_choice,
        "Applied"
    )

    salary = input(
        "Expected Salary (optional): "
    )

    add_application(
        company,
        job_role,
        location,
        application_date,
        status,
        salary
    )

    print("\nApplication added successfully!")


def view_applications():

    applications = get_all_applications()

    print("\n========== JOB APPLICATIONS ==========\n")

    if not applications:
        print("No job applications found.")
        return

    for application in applications:

        print(
            f"""
ID: {application[0]}
Company: {application[1]}
Job Role: {application[2]}
Location: {application[3]}
Application Date: {application[4]}
Status: {application[5]}
Expected Salary: {application[6]}
-----------------------------------
"""
        )


def change_application_status():

    application_id = input(
        "\nEnter Application ID: "
    )

    print("\nSelect New Status:")
    print("1. Applied")
    print("2. Interview")
    print("3. Rejected")
    print("4. Selected")

    choice = input("Enter choice (1-4): ")

    status_options = {
        "1": "Applied",
        "2": "Interview",
        "3": "Rejected",
        "4": "Selected"
    }

    new_status = status_options.get(
        choice,
        "Applied"
    )

    update_status(
        application_id,
        new_status
    )

    print("\nStatus updated successfully!")


def remove_application():

    application_id = input(
        "\nEnter Application ID to delete: "
    )

    delete_application(application_id)

    print("\nApplication deleted successfully!")


def main():

    create_table()

    while True:

        print("\n===================================")
        print(" JOB APPLICATION TRACKER SYSTEM")
        print("===================================")

        print("1. Add Job Application")
        print("2. View All Applications")
        print("3. Update Application Status")
        print("4. Delete Application")
        print("5. View Analytics")
        print("6. Exit")

        choice = input(
            "\nEnter your choice (1-6): "
        )

        if choice == "1":
            add_new_application()

        elif choice == "2":
            view_applications()

        elif choice == "3":
            change_application_status()

        elif choice == "4":
            remove_application()

        elif choice == "5":
            show_analytics()

        elif choice == "6":

            print(
                "\nThank you for using "
                "Job Application Tracker!"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please try again."
            )


if __name__ == "__main__":
    main()
