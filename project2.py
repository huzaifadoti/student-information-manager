import sys

studentdetail = {
    "student1": {"Name": "Ali", "Grade": 70, "Department": "Software"},
    "student2": {"Name": "Sara", "Grade": 80, "Department": "AI"},
    "student3": {"Name": "Bilal", "Grade": 70, "Department": "Media"}
}


def searchbar(data):
    while True:
        user_input = input(
            "enter any detail to search student or enter exit to exit: "
        ).strip().lower()

        if user_input == "exit":
            return

        found = False

        for value in data.values():

            name = str(value.get("Name", "")).lower()
            grade = str(value.get("Grade", "")).lower()
            dept = str(value.get("Department", "")).lower()

            if (
                user_input in name
                or user_input == grade
                or user_input in dept
            ):

                found = True

                print(
                    f"name: {value.get('Name')} | "
                    f"grade: {value.get('Grade')} | "
                    f"department: {value.get('Department')}"
                )

        if not found:
            print("student not found!")


def update(data):

    user_input = input(
        "enter student name to update details or enter exit to exit: "
    ).strip().lower()

    if user_input == "exit":
        return

    found = False

    for key, value in data.items():

        if user_input in value["Name"].lower():

            found = True

            print(f"found: {value}")

            field = input(
                "what do you want to update? (name, grade, department): "
            ).strip().lower()

            match = next(
                (k for k in data[key] if k.lower() == field),
                None
            )

            if match is None:
                print("invalid field!")
                return

            new_value = input(
                f"enter new value for {field}: "
            ).strip()

            if field == "grade":

                try:
                    new_value = int(new_value)

                except ValueError:
                    print("grade should be in numbers!")
                    return

            data[key][match] = new_value

            print(f"updated successfully!\nupdated record: {data[key]}")
            return

    if not found:
        print("student not found!")


while True:

    user_choice = input(
        "\nenter one of the following:\n"
        "search - search student details\n"
        "update - update student details\n"
        "exit - close program\n\n"
    ).strip().lower()

    if user_choice == "exit":
        sys.exit()

    elif user_choice == "search":
        searchbar(studentdetail)

    elif user_choice == "update":
        update(studentdetail)

    else:
        print("invalid input! try again.")