import os
import subprocess
import shlex

def create_directory(domain):
    """Create a directory with the given name"""
    if not os.path.exists(domain):
        os.makedirs(domain)

def run_passive_recon(domain):
    """Run passive reconnaissance on the given domain using several tools"""
    tools = ['amass', 'sublist3r', 'aquatone', 'nmap']
    for tool in tools:
        cmd = f'{tool} -d {domain}'
        output_file = f'{domain}/{tool}.txt'
        with open(output_file, 'w') as f:
            subprocess.call(shlex.split(cmd), stdout=f)

def run_nmap(domain):
    """Run nmap on the given domain and create a file for every open port"""
    cmd = f'nmap -T4 -A {domain}'
    output_file = f'{domain}/nmap.txt'
    with open(output_file, 'w') as f:
        subprocess.call(shlex.split(cmd), stdout=f)
    with open(output_file, 'r') as f:
        output = f.read()
        open_ports = [line.split('/')[0] for line in output.split('\n') if '/open/' in line]
        for port in open_ports:
            cmd = f'nmap -p {port} --script vuln {domain}'
            output_file = f'{domain}/port_{port}_vuln.txt'
            with open(output_file, 'w') as f:
                subprocess.call(shlex.split(cmd), stdout=f)

if __name__ == '__main__':
    domain = input("Enter a website name or IP address: ")
    create_directory(domain)
    run_passive_recon(domain)
    run_nmap(domain)
