from main_utils import to_csv
from class_utils import retrieve_data
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Oscar winners ETL.")
    parser.add_argument('--csv_file_name', type=str, default='oscar_winners', help='The name of the CSV file without extension, e.g. oscarwinners')
    parser.add_argument('--csv_file_path', type=str, default='', help='The path to save CSV file, e.g. C://Documents/csv/. Leave empty so save in the current folder.')
    args = parser.parse_args()
     
    print('collecting and processing data...')
    winners = retrieve_data()
    to_csv(winners, file_name=args.csv_file_name, file_path=args.csv_file_path)
    