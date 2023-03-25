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
