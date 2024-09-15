#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

# check if CPU used is less than 80%
def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    return usage < 80

# check if available memory is less than 20%
def check_memory_usage():
    usage = psutil.virtual_memory().available
    print(usage)
    total = usage / (1024.0 ** 2)
    print(total)
    return total > 20

# check if memory available is less than 100MB
def check_disk_usage(disk):
    disk_usage = shutil.disk_usage(disk)
    free = disk_usage.free / disk_usage.total * 100
    return free > 100

# hostname "localhost" cannot be resolved to "127.0.0.1"
def check_hostname():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address != "127.0.0.1"

message = "Please check your system and resolve the issue as soon as possible."

if not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    emails.generate_email(subject=subject, body=message)

