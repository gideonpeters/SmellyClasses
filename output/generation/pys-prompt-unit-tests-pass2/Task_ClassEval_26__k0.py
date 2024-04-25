import csv
import os

class CSVProcessor:
    def read_csv(self, file_path):
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            title = next(csv_reader)
            data = [row for row in csv_reader]
        return title, data

    def write_csv(self, data, file_path):
        with open(file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        return 1

    def process_csv_data(self, index, file_path):
        title, data = self.read_csv(file_path)
        processed_data = [row[index].upper() for row in data]
        process_file_path = file_path.replace('.csv', '_process.csv')
        self.write_csv([title, processed_data], process_file_path)
        return 1
