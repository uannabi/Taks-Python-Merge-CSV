import argparse
import pandas as pd

def merge_csv_files(files, output_file_path):
    # read the first file and use it as the initial merged data frame
    merged_df = pd.read_csv(files[0], delimiter=',', encoding='utf-8')
    for file in files[1:]:
        # read each additional file and merge on the ID column
        df = pd.read_csv(file, delimiter=',', encoding='utf-8')
        merged_df = pd.merge(merged_df, df, on='ID')
    # write the merged data frame to the output file
    merged_df.to_csv(output_file_path, index=False)

if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('files', type=str, nargs='+', help='Input files to merge')
    parser.add_argument('-o', '--output', type=str, help='Output file path', required=True)
    args = parser.parse_args()

    # call the merge_csv_files function with input and output file paths
    merge_csv_files(args.files, args.output)

