
#!/usr/bin/env python3
import subprocess
import time

def kill_process(process_name):
    """
    Kill all processes whose name contains the provided process_name.
    """
    try:
        print(f"Attempting to kill all processes containing '{process_name}'...")
        subprocess.run(["pkill", "-f", process_name], check=True)
        print(f"Processes matching '{process_name}' have been killed.")
    except subprocess.CalledProcessError:
        # pkill returns non-zero if no process was killed; we can safely ignore that.
        print(f"No active processes found for '{process_name}' or an error occurred.")

def main():
    # List of process names to kill. You can add more if needed.
    processes_to_kill = ["gzclient", "gzserver"]

    for proc in processes_to_kill:
        kill_process(proc)
        # Short delay between kills to ensure processes shut down cleanly
        time.sleep(1)

    print("All Gazebo-related processes have been terminated.")

if __name__ == "__main__":
    main()

