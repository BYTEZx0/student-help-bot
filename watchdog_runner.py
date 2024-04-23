import os
import signal
import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartHandler(FileSystemEventHandler):
    """Handles the event where Python files are modified."""
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"Changes detected in {event.src_path}. Restarting bot...")
            self.restart_bot()

   
    def restart_bot(self):
        # Find and kill existing bot process
        try:
            # Only works on Unix-like systems
            subprocess.run(['pkill', '-f', 'main.py'])
            print("Previous bot process terminated.")
        except Exception as e:
            print(f"Failed to terminate bot process: {e}")

        # Start new bot process
        subprocess.Popen([sys.executable, 'main.py'])
        print("Started new bot process.")
        sys.exit()

def start_observer():
    path = '.'
    event_handler = RestartHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    print("Starting file observer...")
    start_observer()
