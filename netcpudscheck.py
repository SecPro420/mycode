#!/usr/bin/env/ python3
import socket
import psutil
from tqdm import tqdm
import time

def scan_ports(target, start_port, end_port):
    open_ports = []
    total_ports = end_port - start_port + 1

    for port in tqdm(range(start_port, end_port + 1), desc="Scanning Ports", unit="port", dynamic_ncols=True):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

def show_open_ports(target):
    print(f"Scanning open ports on {target}...")
    open_ports = scan_ports(target, 1, 1024)  # Scan ports 1 to 1024 for illustration
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found.")

def show_system_resources():
    print("\nScanning system resources...")

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Disk Usage
    disk_partitions = psutil.disk_partitions(all=False)
    for partition in disk_partitions:
        print(f"\nDisk Usage for {partition.device}:")
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Total: {usage.total} bytes")
        print(f"Used: {usage.used} bytes")
        print(f"Free: {usage.free} bytes")
        print(f"Usage Percentage: {usage.percent}%")

    # Inodes Usage (on Unix systems)
    try:
        inodes_usage = psutil.disk_usage('/').inode_usage
        print("\nInodes Usage:")
        print(f"Total Inodes: {inodes_usage.total}")
        print(f"Used Inodes: {inodes_usage.used}")
        print(f"Free Inodes: {inodes_usage.free}")
        print(f"Inodes Usage Percentage: {inodes_usage.percent}%")
    except AttributeError:
        print("\nInodes Usage not available on this system.")

    # Process with highest memory usage
    processes = sorted(psutil.process_iter(['pid', 'name', 'memory_info']), key=lambda x: x.info['memory_info'].rss, reverse=True)
    print("\nTop 5 processes by memory usage:")
    for process in processes[:5]:
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, Memory Usage: {process.info['memory_info'].rss} bytes")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")

    # Network scanning
    show_open_ports(target_ip)

    # System monitoring
    show_system_resources()

