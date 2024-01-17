#!/usr/bin/env/ python3
import subprocess

def check_system_info():
    try:
        uname_output = subprocess.check_output(["uname", "-a"], universal_newlines=True)
        cpu_info = subprocess.check_output(["lscpu"], universal_newlines=True)
        hardware_info = subprocess.check_output(["lshw", "-short"], universal_newlines=True)
        return f"\nCurrent Kernel:\n{uname_output}\n\nCPU Info:\n{cpu_info}\n\nHardware Info:\n{hardware_info}"
    except Exception as e:
        return f"Error checking system info: {e}"

def check_disk_info():
    try:
        df_output = subprocess.check_output(["df", "-h"], universal_newlines=True)
        return f"\nDisk Usage Info:\n{df_output}"
    except Exception as e:
        return f"Error checking disk info: {e}"

def check_inode_usage():
    try:
        result = subprocess.check_output(["df", "-i"], universal_newlines=True)
        return f"\nInode Usage Info:\n{result}"
    except Exception as e:
        return f"Error checking inode usage: {e}"

def check_logged_in_users():
    try:
        result = subprocess.check_output(["who", "-a"], universal_newlines=True)
        return f"\nLogged-in Users Info:\n{result}"
    except Exception as e:
        return f"Error checking logged-in users: {e}"

def check_ping_connection_status():
    target = input("Enter DNS or IP to ping: ")
    try:
        result = subprocess.check_output(["ping", "-c", "4", target], universal_newlines=True)
        return f"\nPing Connection Status:\n{result}"
    except Exception as e:
        return f"Error checking ping connection status: {e}"

def check_system_updates():
    try:
        subprocess.run(["sudo", "apt", "update"])
        result = subprocess.check_output(["sudo", "apt", "list", "--upgradable"], universal_newlines=True)
        return f"\nSystem Updates Info:\n{result}"
    except Exception as e:
        return f"Error checking system updates: {e}"

def redirect_output_to_file(output, filename, mode='w'):
    try:
        with open(filename, mode) as file:
            file.write(output)
        return f"Output redirected to {filename} successfully!"
    except Exception as e:
        return f"Error redirecting output to file: {e}"

def main():
    while True:
        print("\nOptions:")
        print("1. Check System Info")
        print("2. Check Disk Usage")
        print("3. Check Inode Usage")
        print("4. Check Logged-in Users")
        print("5. Check Ping Connection Status")
        print("6. Check System Updates")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            result = check_system_info()
        elif choice == "2":
            result = check_disk_info()
        elif choice == "3":
            result = check_inode_usage()
        elif choice == "4":
            result = check_logged_in_users()
        elif choice == "5":
            result = check_ping_connection_status()
        elif choice == "6":
            result = check_system_updates()
        elif choice == "7":
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid choice.")
            continue

        print("\nResult:")
        print(result)

        redirect_option = input("Do you want to redirect the output to a file? (yes/no): ")
        if redirect_option.lower() == 'yes':
            filename = input("Enter the filename: ")
            mode = input("Enter 'w' to overwrite or 'a' to append to the file: ")
            redirect_result = redirect_output_to_file(result, filename, mode)
            print(redirect_result)

if __name__ == "__main__":
    main()
def check_ping_connection_status():
    target = input("Enter DNS or IP to ping: ")
    try:
        result = subprocess.check_output(["ping", "-c", "4", target], universal_newlines=True)
        return f"\nPing Connection Status:\n{result}"
    except Exception as e:
        return f"Error checking ping connection status: {e}"

def check_system_updates():
    try:
        subprocess.run(["sudo", "apt", "update"])
        result = subprocess.check_output(["sudo", "apt", "list", "--upgradable"], universal_newlines=True)
        return f"\nSystem Updates Info:\n{result}"
    except Exception as e:
        return f"Error checking system updates: {e}"

def redirect_output_to_file(output, filename, mode='w'):
    try:
        with open(filename, mode) as file:
            file.write(output)
        return f"Output redirected to {filename} successfully!"
    except Exception as e:
        return f"Error redirecting output to file: {e}"

def main():
    while True:
        print("\nOptions:")
        print("1. Check System Info")
        print("2. Check Disk Usage")
        print("3. Check Inode Usage")
        print("4. Check Logged-in Users")
        print("5. Check Ping Connection Status")
        print("6. Check System Updates")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            result = check_system_info()
        elif choice == "2":
            result = check_disk_info()
        elif choice == "3":
            result = check_inode_usage()
        elif choice == "4":
            result = check_logged_in_users()
        elif choice == "5":
            result = check_ping_connection_status()
        elif choice == "6":
            result = check_system_updates()
        elif choice == "7":
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid choice.")
            continue

        print("\nResult:")
        print(result)

        redirect_option = input("Do you want to redirect the output to a file? (yes/no): ")
        if redirect_option.lower() == 'yes':
            filename = input("Enter the filename: ")
            mode = input("Enter 'w' to overwrite or 'a' to append to the file: ")
            redirect_result = redirect_output_to_file(result, filename, mode)
            print(redirect_result)

if __name__ == "__main__":
    main()
def check_ping_connection_status():
    target = input("Enter DNS or IP to ping: ")
    try:
        result = subprocess.check_output(["ping", "-c", "4", target], universal_newlines=True)
        return f"\nPing Connection Status:\n{result}"
    except Exception as e:
        return f"Error checking ping connection status: {e}"

def check_system_updates():
    try:
        subprocess.run(["sudo", "apt", "update"])
        result = subprocess.check_output(["sudo", "apt", "list", "--upgradable"], universal_newlines=True)
        return f"\nSystem Updates Info:\n{result}"
    except Exception as e:
        return f"Error checking system updates: {e}"

def redirect_output_to_file(output, filename, mode='w'):
    try:
        with open(filename, mode) as file:
            file.write(output)
        return f"Output redirected to {filename} successfully!"
    except Exception as e:
        return f"Error redirecting output to file: {e}"

def main():
    while True:
        print("\nOptions:")
        print("1. Check System Info")
        print("2. Check Disk Usage")
        print("3. Check Inode Usage")
        print("4. Check Logged-in Users")
        print("5. Check Ping Connection Status")
        print("6. Check System Updates")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            result = check_system_info()
        elif choice == "2":
            result = check_disk_info()
        elif choice == "3":
            result = check_inode_usage()
        elif choice == "4":
            result = check_logged_in_users()
        elif choice == "5":
            result = check_ping_connection_status()
        elif choice == "6":
            result = check_system_updates()
        elif choice == "7":
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid choice.")
            continue

        print("\nResult:")
        print(result)

        redirect_option = input("Do you want to redirect the output to a file? (yes/no): ")
        if redirect_option.lower() == 'yes':
            filename = input("Enter the filename: ")
            mode = input("Enter 'w' to overwrite or 'a' to append to the file: ")
            redirect_result = redirect_output_to_file(result, filename, mode)
            print(redirect_result)

if __name__ == "__main__":
    main()
