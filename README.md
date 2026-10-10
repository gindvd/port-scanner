# Port Scanners
**Scans all ports to specified IP address for any open TCP ports**

## Usage
python scanner.py <target IP>

or

python threadpool_scanner.py <target IP>

## Description
Two separate port scanners to check all ports on a specified IP
to check for any open TCP ports

Both scanners function the same but use different built-in modules for 
threading. This was done to learn both modules.

Scanner.py uses the threading module while threadpool_scanner.py uses 
the concurrent.futures modules ThreadPoolExecutor

Both take an IPv4 address and scan through all 65535 ports for any 
allowed TCP connections

## Warning
Please DO NOT use on public IP addresses. Only ue on your local home 
network for finding open ports on your personal devices.