# Experiment No. 9
# File Handling and I/O - CSV to JSON

import csv
import json


def csv_to_json(csv_file, json_file):

    data = []

    # Open the CSV file
    with open(csv_file, "r") as file:
        csv_reader = csv.DictReader(file)

        # Convert each row into a dictionary
        for row in csv_reader:
            data.append(row)

    # Write the data into JSON file
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)

    print("CSV data successfully converted to JSON.")


# File names
input_file = "input.csv"
output_file = "output.json"

# Convert CSV to JSON
csv_to_json(input_file, output_file)

# Display the JSON data
print("\nData written to output.json:")
with open(output_file, "r") as file:
    print(file.read())
