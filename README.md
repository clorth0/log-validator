# Log File Validator

This Python script is designed to validate log files according to specific format and content requirements as it relates to [M21-31 requirements]( https://www.whitehouse.gov/wp-content/uploads/2021/08/M-21-31-Improving-the-Federal-Governments-Investigative-and-Remediation-Capabilities-Related-to-Cybersecurity-Incidents.pdf). It checks each log entry for proper formatting, presence of required data fields, and correct data formats.

## Requirements

- Python 3.x

## Setup

No additional libraries are required to run this script. It uses standard Python libraries.

## Usage

1. Place your syslog file in the same directory as the script, or provide the path to the syslog file when running the script.
2. Define the path for the output file where you want to store the validation results.

Run the script with:
```bash
python syslog_file_validator.py
```

## Features

The script validates the following components in each syslog entry:

1. Timestamp
2. Hostname
3. Tag
4. Message content
5. Priority value (optional, based on your syslog format)

The validation results for each entry are written to a specified output file.

## Customization

1. Modify the regular expressions for timestamp, hostname, tag, and message content to match your specific syslog file format.
2. Set the `log_file_path` to the path of your syslog file.
3. Set the `output_file_path` to your desired output file path where the results will be saved.

## Output

The script writes the validation results to the output file specified. Each entry in the output file corresponds to a syslog entry from the input file, along with any validation errors found.

## Note

This script is a template and might require adjustments to fit the specific format and requirements of your syslog files. Ensure to replace placeholder regex patterns with the ones that match your syslog file's format.
