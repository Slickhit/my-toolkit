#!/bin/bash

# This script captures the output of a command at 5-minute intervals and sends a notification email

# Define the command to run and capture the output
command="ls -la /path/to/directory"

# Capture the output of the command in a variable
output=$($command)

# Send an email notification with the captured output
echo "$output" | mail -s "Command Output Notification" guzman77@live.com
