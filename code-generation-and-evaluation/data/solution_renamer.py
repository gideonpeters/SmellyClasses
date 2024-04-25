import os
import shutil

def rename_and_move_files(src_dir, dst_dir, prefix):
    # Ensure the destination directory exists
    os.makedirs(dst_dir, exist_ok=True)

    # Initialize the counter
    index = 0

    # Iterate over all the files in the source directory
    for filename in sorted(os.listdir(src_dir), key=str.lower, reverse=False):
        # Create the new filename by appending the prefix and the counter
        new_filename = prefix + str(index) + '.py'

        # Increment the counter
        index += 1

        # Create the full file paths
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dst_dir, new_filename)

        # # Only move if it's a file
        # if os.path.isfile(src_file):
            # Rename and move the file
        shutil.copy2(src_file, dst_file)

# Usage
src_dir = './benchmark_solution_code'
dst_dir = './new_benchmark_solution_code'
prefix = 'ClassEval_'
rename_and_move_files(src_dir, dst_dir, prefix)