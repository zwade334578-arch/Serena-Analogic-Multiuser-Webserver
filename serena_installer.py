import os
import subprocess

INSTALL_SCRIPT = """
# Serena Analogic Multiuser Webserver Installer

This script will automate the installation process of the Serena Analogic Multiuser Webserver along with GitHub integration on Termux.

## Prerequisites:
1. Python 3
2. Git
3. Node.js
4. npm

## Steps:
1. Update package lists.
2. Install necessary packages.
3. Clone the repository.
4. Install Python dependencies.
5. Install Node.js dependencies.
6. Provide instructions to the user.
"""

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')

# Step 1: Update package lists
print("Updating package lists...")
stdout, stderr = run_command("pkg update -y")
print(stdout)
if stderr:
    print(stderr)

# Step 2: Install necessary packages
packages = ['python', 'git', 'nodejs', 'npm']
print("Installing necessary packages...")
for package in packages:
    stdout, stderr = run_command(f"pkg install -y {package}")
    print(stdout)
    if stderr:
        print(stderr)

# Step 3: Clone the repository
repo_url = "https://github.com/your_username/Serena-Analogic-Multiuser-Webserver.git"
print(f"Cloning the repository from {repo_url}...")
stdout, stderr = run_command(f"git clone {repo_url}")
print(stdout)
if stderr:
    print(stderr)

# Step 4: Install Python dependencies
print("Installing Python dependencies...")
stdout, stderr = run_command("pip install -r Serena-Analogic-Multiuser-Webserver/requirements.txt")
print(stdout)
if stderr:
    print(stderr)

# Step 5: Install Node.js dependencies
print("Installing Node.js dependencies...")
stdout, stderr = run_command("npm install --prefix Serena-Analogic-Multiuser-Webserver")
print(stdout)
if stderr:
    print(stderr)

# Step 6: Provide instructions to the user
print("Installation completed successfully!")
print("To start the server, navigate to the Serena-Analogic-Multiuser-Webserver directory and run 'python server.py'.")
