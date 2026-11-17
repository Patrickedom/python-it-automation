# Linux Bulk User Provisioning

A Python automation script that streamlines employee onboarding by reading new hire records from a CSV file, generating secure random passwords, creating Linux system accounts, and exporting the credentials.

## Overview

Manually creating Linux system accounts and assigning temporary passwords is slow and error-prone. This script automates the entire workflow using Python's built-in `csv`, `secrets`, `subprocess`, and `pathlib` modules, complete with a safe `DRY_RUN` simulation mode for cross-platform testing.

## Features

* **Cross-Platform Path Detection:** Uses `pathlib.Path.home()` to dynamically locate your Desktop and project directory without hardcoded usernames.
* **Safe Simulation Mode (`DRY_RUN`):** Allows you to preview `/sbin/useradd` commands safely on Windows, macOS, or Linux without touching real system accounts.
* **Secure Password Generation:** Uses Python's cryptographic `secrets` module to generate unique 16-character hexadecimal passwords.
* **Input Validation:** Verifies that your input CSV exists before executing and prints clear troubleshooting instructions if missing.

## Project Structure

```text
Desktop/linux_provisioning/
├── create_users.py
├── README.md
└── data/
    ├── users_in.csv      (Place your input records here)
    └── users_out.csv     (Generated automatically after running)
