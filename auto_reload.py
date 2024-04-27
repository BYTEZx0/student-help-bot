import subprocess

def kill_process():
    try:
        # Find and kill process by name
        subprocess.run('taskkill /f /im python.exe /fi "WINDOWTITLE eq main.py"', shell=True, check=True)
        print("Process killed successfully.")
    except subprocess.CalledProcessError:
        print("Process not found.")
    except Exception as e:
        print(f"Error: {e}")

kill_process()
