# scapy-probe-requests
A script to transmit probe requests using scapy. The script is the basis to test which content of probe requests is actually required and which can be omitted.

To run it, the adapter used has to be in monitor mode. If you want to monitor the transmitted requests and responses, I suggest you use another Wi-Fi interface and use wireshark or similar network monitoring tools; monitoring responses via scapy and particularly via the same adapter as you sent it from is rather unreliable.
Running the script requires sudo privilege. Run it like so:

sudo python send_pr.py
