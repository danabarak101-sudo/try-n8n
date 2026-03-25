import subprocess
import argparse
import sys

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiple(num1, num2):
    return num1 * num2

def parse_args():
    # הגדרת ה-Parser לקבלת הפרמטרים מה-n8n
    parser = argparse.ArgumentParser(description="Run automation tests")
    
    parser.add_argument("-m", "--machine", required=True, help="Machine name")
    parser.add_argument("-v", "--version", required=True, help="Version")
    parser.add_argument("-u", "--user", required=True, help="Username")
    parser.add_argument("-p", "--password", required=True, help="Password")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    command_str = f"python3 -m test_func.py -m {args.machine} -v {args.version} --user {args.user} --p {args.password}"
    
    print(f"Executing command: {command_str}")
    
    result = subprocess.run(
        args=command_str, 
        shell=True, 
        capture_output=True, 
        text=True
    )
    
    # הדפסת התוצאות (שייקראו על ידי ה-Worker ב-n8n)
    if result.returncode == 0:
        print("Success:")
        print(result.stdout)
    else:
        print("Error:")
        print(result.stderr)
