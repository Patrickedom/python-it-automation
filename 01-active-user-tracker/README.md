# Active User Tracker

A Python script that tracks active user sessions across multiple machines based on chronological login and logout events.

## Overview

This project simulates a system administration utility from the Google IT Automation with Python certificate. It sorts a list of event objects chronologically, maintains a record of active users per machine using Python sets, and prints out a clean status report.

## Features

* **Chronological Sorting:** Uses a custom helper function (`get_event_date`) to sort events by timestamp before processing.
* **State Management:** Tracks active users with sets (`.add()` for logins, `.remove()` for logouts) to handle multiple active sessions seamlessly.
* **Filtered Reporting:** Automatically skips machines with zero active users when generating the final report.

## Usage

Run the script directly from your terminal:

```bash
python3 user_tracker.py
