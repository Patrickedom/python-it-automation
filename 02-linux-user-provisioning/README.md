# Linux Bulk User Provisioning

A Python automation script that streamlines employee onboarding by reading new hire records from a CSV file, generating cryptographically secure random passwords, creating Linux system accounts, and exporting the credentials to a new CSV file.

## Overview

Manually creating hundreds of Linux accounts and assigning temporary passwords is slow and error-prone. This script automates the entire workflow using Python's built-in `csv`, `secrets`, `subprocess`, and `pathlib` modules. It also includes a built-in `DRY_RUN` mode so you can safely test password generation and preview terminal commands on any operating system without modifying real system accounts.

## Features

* **Cross-Platform Path Detection:** Uses `pathlib.Path.home()` to locate the project folder dynamically without hardcoded usernames.
* **Input File Validation:** Checks that `users_in.csv` exists before executing and provides a clear error message if missing.
* **Safe Simulation Mode (`DRY_RUN`):** Previews `/sbin/useradd` commands and generates `users_out.csv` safely on Windows, macOS, or Linux.
* **Secure Password Generation:** Creates unique 16-character hexadecimal passwords using the `secrets` module.
* **System Account Creation:** Executes `/sbin/useradd` with home directory creation (`-m`), full name comments (`-c`), and default group assignment (`-G users`) when run in production mode.

## Prerequisites

* **Python Version:** Python 3.6 or higher (uses standard library only; no external packages required).
* **For Live Execution (`DRY_RUN = False`):**
  * Linux OS (requires access to `/sbin/useradd`).
  * Root or `sudo` privileges to create system user accounts.

## Project Structure

```text
Desktop/linux_provisioning/
├── create_users.py
├── README.md
└── data/
    ├── users_in.csv
    └── users_out.csv  (generated after running)
