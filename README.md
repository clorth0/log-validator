# Log File Validator

This Python script is designed to validate log files according to specific format and content requirements as it relates to M21-31 requirements. It checks each log entry for proper formatting, presence of required data fields, and correct data formats.

## Requirements

- Python 3.x

## Setup

No additional libraries are required to run this script. It uses standard Python libraries.

## Usage

Place your log file in the same directory as the script, or provide the path to the log file when running the script.

Run the script with:
```bash
python log_file_validator.py
```

## Features

The script validates the following fields in each log entry:

1. Properly formatted and accurate timestamp
2. Status code for the event type
3. Device identifier (e.g., MAC address)
4. Session / Transaction ID
5. Autonomous System Number (ASN)
6. Source IP (IPv4 and IPv6)
7. Destination IP (IPv4 and IPv6)
8. Status Code
9. Response Time
10. Additional headers (e.g., HTTP headers)
11. Username and/or UserID
12. Command executed
13. Data formatted as key-value pairs
14. Unique event identifier for event correlation

Each field is validated using regular expressions and specific validation logic defined in the script.

## Customization

You can customize the script by modifying the regular expressions and validation logic to match your specific log file format and requirements.

## Note

This script is a template and might require adjustments to fit the specific format and requirements of your log files. Ensure to replace placeholder regex patterns with the ones that match your log file's format.
