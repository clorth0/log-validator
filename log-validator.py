import re
from datetime import datetime

# Example regex for syslog timestamp - modify as per your syslog format
timestamp_regex = r'\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}'  # Example: 'Jan  1 00:00:00'
hostname_regex = r'your-hostname-regex'  # Define the regex for hostname
tag_regex = r'your-tag-regex'  # Define the regex for the tag
message_regex = r'your-message-regex'  # Define the regex for the message content

def is_valid_timestamp(timestamp):
    try:
        datetime.strptime(timestamp, '%b %d %H:%M:%S')
        return True
    except ValueError:
        return False

def is_valid_hostname(hostname):
    return bool(re.match(hostname_regex, hostname))

def is_valid_tag(tag):
    return bool(re.match(tag_regex, tag))

def is_valid_message(message):
    return bool(re.match(message_regex, message))

def parse_syslog_entry(entry):
    # Example syslog format: <Priority>Timestamp Hostname Tag: Message
    parts = entry.split(' ', 4)
    if len(parts) < 5:
        return None, 'Incomplete entry'

    priority, timestamp, hostname, tag, message = parts
    return {
        'priority': priority,
        'timestamp': timestamp,
        'hostname': hostname,
        'tag': tag.rstrip(':'),
        'message': message
    }, None

def validate_syslog_entry(entry):
    fields, error = parse_syslog_entry(entry)
    if error:
        return False, error

    errors = []
    if not is_valid_timestamp(fields['timestamp']):
        errors.append('Invalid timestamp')

    if not is_valid_hostname(fields['hostname']):
        errors.append('Invalid hostname')

    if not is_valid_tag(fields['tag']):
        errors.append('Invalid tag')

    if not is_valid_message(fields['message']):
        errors.append('Invalid message')

    return len(errors) == 0, ', '.join(errors)

def main(log_file_path):
    with open(log_file_path, 'r') as file:
        for line in file:
            entry = line.strip()
            is_valid, error = validate_syslog_entry(entry)
            if not is_valid:
                print(f"Invalid entry: {entry}\nError: {error}")

if __name__ == "__main__":
    log_file_path = 'path_to_your_syslog_file.log'
    main(log_file_path)
