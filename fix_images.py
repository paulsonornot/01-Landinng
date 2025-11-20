import shutil
import os
import sys

# Setup paths
source_dir = "/Users/paulsonornot/.gemini/antigravity/brain/fc9315c3-f577-462b-929f-500d7d35011e"
dest_dir = "/Volumes/Data/Курсы/AI/Programming/01 Landinng/images"
log_file = "/Volumes/Data/Курсы/AI/Programming/01 Landinng/copy_debug_log.txt"

def log(msg):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)

try:
    # Clear previous log
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("Starting copy process...\n")

    log(f"CWD: {os.getcwd()}")
    log(f"Source: {source_dir}")
    log(f"Dest: {dest_dir}")

    # Check source
    if not os.path.exists(source_dir):
        log("ERROR: Source directory does not exist!")
        sys.exit(1)
    
    files = os.listdir(source_dir)
    png_files = [f for f in files if f.endswith('.png')]
    log(f"Found {len(png_files)} PNG files in source.")

    # Check/Create dest
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
            log("Created destination directory.")
        except Exception as e:
            log(f"ERROR creating directory: {e}")
            sys.exit(1)
    else:
        log("Destination directory exists.")

    # Copy files
    for f in png_files:
        src = os.path.join(source_dir, f)
        dst = os.path.join(dest_dir, f)
        try:
            shutil.copy2(src, dst)
            if os.path.exists(dst):
                log(f"SUCCESS: Copied {f} (Size: {os.path.getsize(dst)} bytes)")
            else:
                log(f"FAILURE: File {f} not found after copy!")
        except Exception as e:
            log(f"ERROR copying {f}: {e}")

    log("Copy process finished.")

except Exception as e:
    # Fallback logging if main log fails
    print(f"CRITICAL ERROR: {e}")
