import network
import utime
from network.config import SSID, PASSWORD

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        print(".", end="")
        utime.sleep(1)
    print("\nConnected to Wi-Fi:", wlan.ifconfig())
    return wlan