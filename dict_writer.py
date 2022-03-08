import csv

# Read the CSV file as a list of lists
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Write the CSV file quoting each field
    with open('new_names.csv', 'w') as new_file:
      fieldnames = ['first_name', 'last_name']
      csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

      csv_writer.writeheader()

      for line in csv_reader:
        del line['email']
        csv_writer.writerow(line)