import os
import shutil
import sys
import time


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    job_folder = sys.argv[1]
    if not os.path.isdir(job_folder):
        sys.exit(1)

    contents = os.listdir(job_folder)
    subfolders = [f for f in contents if os.path.isdir(os.path.join(job_folder, f))]

    if not subfolders:
        os.utime(job_folder, None)
        return

    parent_dir = os.path.dirname(job_folder)
    for subfolder in subfolders:
        subfolder_path = os.path.join(job_folder, subfolder)
        new_path = os.path.join(parent_dir, subfolder)
        if os.path.exists(new_path):
            sys.exit(1)
        shutil.move(subfolder_path, parent_dir)

    shutil.rmtree(job_folder)

if __name__ == "__main__":
    main() 