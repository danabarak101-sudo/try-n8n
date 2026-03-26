import subprocess
import argparse
import sys

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiple(num1, num2):
    return num1 * num2

def args():
    # הגדרת ה-Parser לקבלת הפרמטרים מה-n8n
    parser = argparse.ArgumentParser(description="Run automation tests")
    
    parser.add_argument("-m", "--mname", required=True, help="Machine name")
    parser.add_argument("-v", "--mver", required=True, help="Version")
    parser.add_argument("-u", "--muser", required=True, help="Username")
    parser.add_argument("-p", "--mpass", required=True, help="Password")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = args()
    command_str = (
            f"python -m pytest test_func.py -vs "
            f"--mname {args.machine_name} "
            f"--mver {args.version} "
            f"--muser {args.user} "
            f"--mpass {args.password}"
        )
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
