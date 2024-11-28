import time

def send_command(command):
    print(f"Sending command: {command}")
    # Replace this with the actual GPIO control for the Flipper Zero.

send_command("start_deauth_attack")
time.sleep(10)  # Run for 10 seconds
send_command("stop_deauth_attack")
print("Deauth attack complete!")
