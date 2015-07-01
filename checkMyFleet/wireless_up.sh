#! /bin/bash
ifconfig wlan0
iwconfig wlan0 essid GVT-F866 key 4603000479
dhclient wlan0