import csv
import random

# Existing CSV file path
existing_csv_file = "C:\\Users\\OS\\Desktop\\Workspace\\hapt\\Housing.csv"

# Function to generate random yes/no values
def random_yes_no():
    return random.choice(["yes", "no"])

# Function to generate more data
def generate_additional_data(num_rows):
    additional_data = []
    for _ in range(num_rows):
        row = [
            random.randint(1000000, 20000000),  # price
            random.randint(5000, 15000),        # area
            random.randint(2, 5),               # bedrooms
            random.randint(1, 4),               # bathrooms
            random.randint(1, 4),               # stories
            random_yes_no(),                    # mainroad
            random_yes_no(),                    # guestroom
            random_yes_no(),                    # basement
            random_yes_no(),                    # hotwaterheating
            random_yes_no(),                    # airconditioning
            random.randint(1, 3),               # parking
            random_yes_no(),                    # prefarea
            random.choice(["furnished", "semi-furnished", "unfurnished"])  # furnishingstatus
        ]
        additional_data.append(row)
    return additional_data

# Function to update existing CSV file with additional data
def update_csv_file(existing_file, additional_data):
    with open(existing_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(additional_data)

# Generate 5 additional rows of data
additional_rows = generate_additional_data(10000)

# Update the existing CSV file with additional data
update_csv_file(existing_csv_file, additional_rows)

print("Additional data successfully added to the existing CSV file.")
