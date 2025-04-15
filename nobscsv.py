# This routine gets the number of lines in a large .csv file without loading it completely.
#
#    Evens SALIES, v1. 12/2024

import pandas as pd

# The chunksize argument specifies the number of rows to read at a time when processing the file in chunks.
def count_lines_in_csv(file_path):
    line_count = 0
    chunk_size = 1000000
    for chunk in pd.read_csv(file_path, chunksize = chunk_size, dtype = str):
        line_count += len(chunk)
        print(f"We reached", line_count)
    return line_count

# Replace the path with the path to your file
line_count = count_lines_in_csv('pathtocsvfilehere.csv')
print(f"The CSV file contains {line_count} lines.")
