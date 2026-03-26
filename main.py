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
    parser = argparse.ArgumentParser()
    # כאן אנחנו מגדירים את הדגלים ש-n8n שולח (-m, -v וכו')
    parser.add_argument("-m", "--machine_name", required=True)
    parser.add_argument("-v", "--version", required=True)
    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-p", "--password", required=True)
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
