import csv
import secrets
import subprocess
from pathlib import Path

# SAFETY SWITCH:
# True = Simulates the Linux commands safely (works on Windows, Mac, and Linux)
# False = Actually runs /sbin/useradd on a real Linux machine (requires sudo)
DRY_RUN = True

# Dynamically set paths relative to this script's directory
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "users_in.csv"
OUTPUT_FILE = BASE_DIR / "data" / "users_out.csv"

# Verify the input file exists before running
if not INPUT_FILE.exists():
    print(f"Error: Could not find {INPUT_FILE}")
    print("Please make sure 'data/users_in.csv' is set up before running.")
    exit(1)

with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file_input, \
     open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file_output:

    reader = csv.DictReader(file_input)
    writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
    writer.writeheader()

    for user in reader:
        # Generate a random 16-character password
        user["password"] = secrets.token_hex(8)

        # Build the Linux useradd command
        useradd_cmd = [
            "/sbin/useradd",
            "-c", user["real_name"],
            "-m",
            "-G", "users",
            "-p", user["password"],
            user["username"]
        ]

        if DRY_RUN:
            print(f"[SIMULATION] Would run: {' '.join(useradd_cmd)}")
        else:
            subprocess.run(useradd_cmd, check=True)
            print(f"[CREATED] User account created for {user['username']}")

        # Write the updated row (with password) to users_out.csv
        writer.writerow(user)

print(f"\nDone! Check your generated passwords in: {OUTPUT_FILE}")
