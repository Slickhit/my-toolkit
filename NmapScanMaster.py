import tkinter as tk
from tkinter import ttk
import nmap
import threading

def run_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sS -sU -sV -O -A -v')
    return nm.csv()

def start_scan():
    target = target_entry.get()
    if not target:
        return
    target_entry.delete(0, tk.END)
    
    threading.Thread(target=run_scan_and_add_report, args=(target,)).start()

def run_scan_and_add_report(target):
    report = run_scan(target)
    reports[target] = report
    
    button = ttk.Button(report_frame, text=target, command=lambda: show_report(target))
    button.pack()
    scan_progress.set('Scan complete for ' + target)

def show_report(target):
    report_text.delete(1.0, tk.END)
    report_text.insert(tk.END, reports[target])

app = tk.Tk()
app.title('Nmap GUI')

scan_frame = ttk.Frame(app)
scan_frame.pack()

scan_progress = tk.StringVar()
scan_progress.set('Enter target and press Start Scan')

scan_label = ttk.Label(scan_frame, textvariable=scan_progress)
scan_label.pack()

target_entry = ttk.Entry(scan_frame)
target_entry.pack()

start_scan_button = ttk.Button(scan_frame, text='Start Scan', command=start_scan)
start_scan_button.pack()

report_frame = ttk.Frame(app)
report_frame.pack()

report_text = tk.Text(app)
report_text.pack()

reports = {}

app.mainloop()

#The tool is a Python script that takes the input of a website name or IP address, creates a directory for it, runs passive reconnaissance using several tools, runs nmap, creates a file for every open port, and looks up vulnerabilities for each file.

#The script first creates a directory with the name of the domain and then runs passive reconnaissance using several tools such as amass, sublist3r, aquatone, and nmap. It creates a file in the directory with the output of each tool. After that, it runs nmap with aggressive scanning options, creates a file for every open port, and looks up vulnerabilities for each open port using the nmap vuln script. For each open port, it creates a file with the output of the nmap vuln script.

#This tool is useful for performing a comprehensive network audit, port analysis, and vulnerability assessment of a website or IP address. It automates the process of running multiple reconnaissance and vulnerability assessment tools, saving time and effort. The output files can be used to identify potential security risks and vulnerabilities, and to take proactive steps to mitigate them.
