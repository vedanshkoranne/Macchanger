
import subprocess
interface = raw_input("enter your interface (wlan0 or eth0 ) ")
new_mac = raw_input("Enter new MAC address > ")


subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig  " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig  " + interface + " up", shell=True)



print("||||||| ||   ||  ||      || |||||| |||||||     |     |||    || |||||| ||   ||")
print("||   ||  |   |    ||    ||  |      |||  ||    | |    || ||  || ||     ||   ||")
print("|||||     | |       ||  ||   |||||| |||  ||   || ||   ||  || || |||||| |||||||")
print("||   ||    |        ||||    |      |||  ||  ||---||  ||   | ||     || ||   ||")
print("|||||||    |         ||     |||||| ||||||| ||     || ||    ||| |||||| ||   ||")

print("           Current MAC address = " + new_mac + (" of ") + interface )
