import json


data = {
    "farmers": [],
    "consumers": []
}


def add_data(data_type):
    name = input(f"Enter {data_type} name: ")
    needs = input(f"Enter {data_type}'s needs: ")

    entry = {"name": name, "needs": needs}
    data[data_type].append(entry)

    print(f"{data_type.capitalize()} data added successfully!")


def sort_data(data_type):
    if not data[data_type]:
        print(f"No {data_type} data available.")
        return

 
    sorted_data = sorted(data[data_type], key=lambda x: x["name"])

    print(f"Sorted {data_type} data:")
    for entry in sorted_data:
        print(f"Name: {entry['name']}, Needs: {entry['needs']}")

while True:
    print("\nOptions:")
    print("1. Add Farmer")
    print("2. Add Consumer")
    print("3. Sort Farmers")
    print("4. Sort Consumers")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_data("farmers")
    elif choice == "2":
        add_data("consumers")
    elif choice == "3":
        sort_data("farmers")
    elif choice == "4":
        sort_data("consumers")
    elif choice == "5":
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
