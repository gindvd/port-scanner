import sys
import socket
import threading

from datetime import datetime


def scan_port(target: str, port: int) -> int:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open on host: {target}")
        
        s.close()
    
    except OSError as e:
        print(f"Socket error scanning port {port}: \n{e}")
    
    except TimeoutError as e:
        print(f"Port {port} timed out: \n{e}")
    
    except Exception as e:
        print(f"An unexpected error occurred on port {port}: \n{e}")


def threaded_scanner(target: str) -> None:
    try:
        target_ip = socket.gethostbyname(target)
    except:
        print(f"Unable to resolve target {target} by hostname")
        sys.exit(1)

    try:
        threads = []

        # Creates separate thread for all 65535 ports
        for port in range(1, 65536):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        # Join all threads when all complete
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("Scan terminated by the user")
        sys.exit(0)
    
    except OSError as e:
        print(f"Socket error occurred scanning {target}: \n{e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error occurred: \n{e}")
        sys.exit(1)


def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    
    else:
        print("Invalid number arguments")
        print("Usage: python3 portscanner.py <target>")
        sys.exit(1)
    
    print("-" * 50)
    print(f"Scanning the target: {target}")

    start_time = datetime.now()
    print(f"Start time: {start_time}")
    print("-" * 50)
    
    threaded_scanner(target)

    end_time = datetime.now()
    print("\nScan completed!")
    print(f"Time finished: {end_time}")

    print(f"Time to complete: {end_time - start_time}")


if __name__ == "__main__":
    main()
    