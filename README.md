Cybersecurity Toolkit Repository

This repository contains a collection of scripts and tools for various cybersecurity tasks. The goal is to make the user's life easier by providing quick access to preferred tools and automating common tasks. The repository will continue to grow as new scripts are added over time.
Contents

    Nmap GUI
    Make Shell Scripts Executable
    Command Output Email Notification
    Install Visual Studio Code and Python 3

Nmap GUI

This Python application uses the Tkinter library to create a simple graphical user interface (GUI) for running Nmap scans. The user can input a target IP address or domain, start the scan, and view the results in the form of a report.
Key Functions

    run_scan(target): Performs an Nmap scan on the provided target and returns the result in CSV format.
    start_scan(): Called when the "Start Scan" button is clicked; retrieves the target and starts a new thread to run the scan and add the report.
    run_scan_and_add_report(target): Calls run_scan() and stores the resulting report in the reports dictionary; adds a button to the GUI to display the report.
    show_report(target): Called when the target-specific button is clicked; displays the corresponding report in a text widget.

Make Shell Scripts Executable

This bash script makes all shell scripts (*.sh files) in a specified directory executable. It changes the current working directory to the target directory, loops through all the files with a .sh extension, and sets the executable flag for each file using chmod +x.
Command Output Email Notification

This bash script runs a specified command (e.g., ls -la /path/to/directory) every 5 minutes, captures its output, and sends the output via email. It utilizes a while true loop to execute the command indefinitely at 5-minute intervals.
Install Visual Studio Code and Python 3

This bash script downloads and installs Visual Studio Code and Python 3 on a Ubuntu-based Linux system. The script performs the following steps:

    Import Microsoft's GPG key to verify the authenticity of the Visual Studio Code package.
    Add the Visual Studio Code repository to the system's package sources.
    Update the package index to include the newly added repository.
    Install Visual Studio Code using the apt-get package manager.
    Install Python 3 and the associated pip package manager using the apt-get package manager.

Note: This script requires administrator privileges to execute, so you should run it with sudo or as the root user.
Contributing

Feel free to contribute to this repository by submitting pull requests with additional scripts or improvements to existing ones. Your contributions will help the toolkit grow and become more versatile for users.
