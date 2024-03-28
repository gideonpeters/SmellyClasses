import csv
import os

class CSVProcessor:
    """
    This is a class for processing CSV files, including reading and writing CSV data, as well as processing specific operations and saving as a new CSV file.
    """

    def read_csv(self, file_name):
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            title = next(csv_reader)
            data = [row for row in csv_reader]
        return title, data

    def write_csv(self, data, file_name):
        with open(file_name, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for row in data:
                csv_writer.writerow(row)
        return 1

    def process_csv_data(self, N, save_file_name):
        with open(save_file_name, 'w', newline='') as save_file:
            with open(save_file_name, 'r') as file:
                csv_reader = csv.reader(file)
                csv_writer = csv.writer(save_file)
                for row in csv_reader:
                    if len(row) > N:
                        row[N] = row[N].upper()
                    csv_writer.writerow(row)
        return 1
