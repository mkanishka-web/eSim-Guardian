

import platform
import psutil
import socket
import shutil


def scan_system():

    system_info = {}

    # Operating System Details
    system_info["Operating System"] = platform.system()
    system_info["OS Version"] = platform.version()
    system_info["Architecture"] = platform.machine()

    # Processor Details
    system_info["Processor"] = platform.processor()
    system_info["CPU Cores"] = psutil.cpu_count(logical=False)
    system_info["Logical CPUs"] = psutil.cpu_count(logical=True)
    system_info["CPU Usage"] = str(psutil.cpu_percent(interval=1)) + "%"

    # Memory Details
    memory = psutil.virtual_memory()
    system_info["Total RAM"] = str(round(memory.total / (1024 ** 3), 2)) + " GB"
    system_info["Used RAM"] = str(round(memory.used / (1024 ** 3), 2)) + " GB"
    system_info["RAM Usage"] = str(memory.percent) + "%"

    # Disk Details
    disk = shutil.disk_usage("/")
    system_info["Total Disk"] = str(round(disk.total / (1024 ** 3), 2)) + " GB"
    system_info["Free Disk"] = str(round(disk.free / (1024 ** 3), 2)) + " GB"

    # Network Details
    system_info["Computer Name"] = socket.gethostname()
    system_info["Python Version"] = platform.python_version()

    # Display Information
    print("\n================================")
    print("       SYSTEM INFORMATION")
    print("================================")

    for key, value in system_info.items():
        print(f"{key}: {value}")

    return system_info
