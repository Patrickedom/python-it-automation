# Active User Tracker

A Python utility that parses system login and logout event logs to identify which users are currently logged into specific machines.

## Overview
System logs often arrive out of chronological order. This script ingests raw Event records, sorts them by timestamp, tracks session states using dictionaries and sets, and generates a clean report of active users while filtering out idle machines.

## Features
* **Chronological Sorting:** Orders unsorted login/logout records by timestamp before processing.
* **Duplicate Prevention:** Uses Python set() structures to ensure each active user is recorded once per machine.
* **Clean Reporting:** Skips machines with zero active users to keep output concise.

## Prerequisites
* Python 3.6 or higher (uses standard library only, no external packages required).

## Usage
1. Navigate to the project folder:
   cd 01-active-user-tracker

2. Run the script:
   python3 user_tracker.py

## Example Output
Given the sample events defined in user_tracker.py, the script outputs:

{'webserver.local': {'lane'}, 'myworkstation.local': set(), 'mailserver.local': {'chris'}}
webserver.local: lane
mailserver.local: chris

