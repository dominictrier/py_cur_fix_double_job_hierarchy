# fix_job_hierarchy.py

A simple script to flatten a two-level folder hierarchy.

## What it does
- Moves all subfolders of a given folder up one level (to the parent directory).
- Removes the original folder after moving its subfolders.
- If there are no subfolders, the script touches (updates the modification time of) the folder.

## Usage
Requires Python 3.6 or newer.

```sh
python src/fix_job_hierarchy.py /path/to/your_folder
```

## Example
**Before:**
```
/path/to/your_folder/
  subfolder1/
  subfolder2/
```

**After:**
```
/path/to/subfolder1/
/path/to/subfolder2/
``` 