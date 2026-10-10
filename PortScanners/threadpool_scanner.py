import sys
import socket

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime 


def scan_port(port: int, target: str) -> None:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"TCP port {port} is open on host: {target}")
        
        s.close()
        
    except OSError as e:
        print(f"Socket error scanning port {port}:\n{e}")
    
    except TimeoutError as e:
        print(f"Port {port} timed out:\n{e}")
    
    except Exception as e:
        print(f"An unexpected error occurred on port {port}:\n{e}\n")


def threaded_scanner(target: str) -> None:
    try:
        target_ip = socket.gethostbyname(target)
    except:
        print(f"Unable to resolve target {target} by hostname")
        sys.exit(1)
    
    start_time = datetime.now()
    
    print("-" * 50)
    print(f"Scanning the target: {target_ip}")
    print(f"Start time: {start_time}")
    print("-" * 50)
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(scan_port, port, target_ip) 
            for port in range(1, 65536)
        ]
    
    end_time = datetime.now()

    print("\nScan completed!")
    print(f"Time finished: {end_time}")

    print(f"Time to complete: {end_time - start_time}")


def main() -> None:
    if len(sys.argv) == 2:
        target = sys.argv[1]
    
    else:
        print("invalid number arguments")
        print("Usage: python portscanner.py <target>")
        sys.exit(1)
    
    threaded_scanner(target)


if __name__ == "__main__":
    main()