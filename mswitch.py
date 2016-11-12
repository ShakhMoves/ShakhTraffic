# In The Name Of God
# ========================================
# [] File Name : mswitch.py
#
# [] Creation Date : 13-11-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from mininet.node import OVSSwitch


class MultiSwitch(OVSSwitch):
    "Custom Switch() subclass that connects to different controllers"
    def start(self, controllers):
        return OVSSwitch.start(self, controllers)
