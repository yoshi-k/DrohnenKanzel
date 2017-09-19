#!/usr/bin/python
#
# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2014 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA  02110-1301, USA.

"""
Simple example that connects to the first Crazyflie found, ramps up/down
the motors and disconnects.
"""
 

#Dies ist ein Test

print("Start of the example")
import time
import sys
from threading import Thread
import logging
# sys.path.append(r"C:\Users\Hermann Kulbartz\Desktop\bitcraze\crazyflie-clients-python-2015.09\crazyflie-clients-python-2015.09\lib")
import cflib  # noqa
from cflib.crazyflie import Crazyflie  # noqa

logging.basicConfig(level=logging.ERROR)


class MotorRampExample():
    """Example that connects to a Crazyflie and ramps the motors up/down and
    than disconnects"""

    def __init__(self, link_uri):
        """ Initialize and run the example with the specified link_uri """

        self._cf = Crazyflie()

        self._cf.connected.add_callback(self._connected)
        self._cf.disconnected.add_callback(self._disconnected)
        self._cf.connection_failed.add_callback(self._connection_failed)
        self._cf.connection_lost.add_callback(self._connection_lost)
        self._cf.open_link(link_uri)
        global gl_link_uri
        gl_link_uri = link_uri
        time.sleep(0.5)
        print("Connecting to %s" % link_uri, "Crazyflie_test zeile 59")
#        self._ramp_motors()
#
        thrust = 500
     
        print("In MotorRampExample() thrust %i" % thrust)
        self.up_motors(thrust)
#        self.motors()

    def _connected(self, link_uri):
        """ This callback is called form the Crazyflie API when a Crazyflie
        has been connected and the TOCs have been downloaded."""

        # Start a separate thread to do the motor test.
        # Do not hijack the calling thread!
        print ("In connected zeile 74")
#        Thread(target=self._ramp_motors).start()


    def _connection_failed(self, link_uri, msg):
        """Callback when connection initial connection fails (i.e no Crazyflie
        at the specified address)"""
        print("Connection to %s failed: %s" % (link_uri, msg))

    def _connection_lost(self, link_uri, msg):
        """Callback when disconnected after a connection has been made (i.e
        Crazyflie moves out of range)"""
        print("Connection to %s lost: %s" % (link_uri, msg))

    def _disconnected(self, link_uri):
        """Callback when the Crazyflie is disconnected (called in all cases)"""
        print("Disconnected from %s" % link_uri, "Crazyflie_test zeile 92")

    def _ramp_motors(self):
        thrust_mult = 1
        thrust_step = 500
        thrust = 20000
        pitch = 0
        roll = 0
        yawrate = 0

        # Unlock startup thrust protection
        self._cf.commander.send_setpoint(0, 0, 0, 0)

        while thrust >= 10000:
            self._cf.commander.send_setpoint(roll, pitch, yawrate, thrust)
            time.sleep(0.5)
            if thrust >= 40000:
                thrust_mult = -1
            thrust += thrust_step * thrust_mult
            print(thrust)
        self._cf.commander.send_setpoint(0, 0, 0, 0)
        time.sleep(0.5)
        
        
    def up_motors(self, thrust):
        pitch = 0
        roll = 0
        yawrate = 0
#        self._cf = Crazyflie()
#        thrust = self.thrust        
#        thrust = 20000
        self._cf.commander.send_setpoint(0, 0, 0, 0)

#        thrust = self.thrust
        print("Aus Crazyflie_test Zeile 126", thrust)
        print(type(thrust))
        pitch = 0
        roll = 0
        yawrate = 0
        self._cf.commander.send_setpoint(roll, pitch, yawrate, thrust)
#        while thrust >= 10000:
#            self._cf.commander.send_setpoint(roll, pitch, yawrate, thrust)
#        thrust = 40000
#        self._cf.commander.send_setpoint(roll, pitch, yawrate, thrust)
#        time.sleep(0.5)
#        self._cf.commander.send_setpoint(0, 0, 0, 0)
#        thrust = 40000
#        self._cf.commander.send_setpoint(roll, pitch, yawrate, thrust)
#        time.sleep(3.)
#        thrust=43000
#        pitch=0.
#        thrust = 4500
        for i in range(5):
            print("Ramp up %3i"%pitch, thrust)
            self._cf.commander.send_setpoint(0, -30, 0, thrust)
            pitch += 50
            time.sleep(1)
            print("Ramp down")
            self._cf.commander.send_setpoint(0, 0, 0, thrust)
            time.sleep(1)
            # Make sure that the last packet leaves before the link is closed
            # since the message queue is not flushed before closing
        time.sleep(0.1)
        self._cf.close_link()
#        print("Schliesse Link")
        time.sleep(0.1)
        
    def motorsroll(self, roll):
        print("Zeile 162 roll = ", roll)
        nthrust = 0
        npitch = 0
        nroll = 0
        nyawrate = 0
        self._cf.commander.send_setpoint(nroll, npitch, nyawrate, nthrust)
        time.sleep(0.1)
        self._cf.commander.send_setpoint(roll, 0, 0, 0)
        time.sleep(0.1)

    def motorspitch(self, pitch):
        print("Zeile 173 pitch = ", pitch)
        nthrust = 0
        npitch = 0
        nroll = 0
        nyawrate = 0
        self._cf.commander.send_setpoint(nroll, npitch, nyawrate, nthrust)
        time.sleep(0.1)
        self._cf.commander.send_setpoint(0, pitch, 0, 0)
        time.sleep(0.1)
        
    def motorsyawrate(self, yawrate):
        nthrust = 0
        npitch = 0
        nroll = 0
        nyawrate = 0
        self._cf.commander.send_setpoint(nroll, npitch, nyawrate, nthrust)
        time.sleep(0.1)
        self._cf.commander.send_setpoint(0, 0, yawrate, 0)
        time.sleep(0.5)        
        
    def motorsthrust(self, thrust):
#        nthrust = 0
#        npitch = 0
#        nroll = 0
#        nyawrate = 0
#        thrust_mult = 1
#        self._cf.commander.send_setpoint(nroll, npitch, nyawrate, nthrust)
#        time.sleep(0.1)
        self._cf.commander.send_setpoint(0, 0, 0, thrust)
#        while thrust >= 10000:
#            self._cf.commander.send_setpoint(0, 0, 0, thrust)
#            time.sleep(0.5)
#            if thrust >= 20000:
#                thrust_mult = -1
#            thrust += 3000 * thrust_mult
#            print(thrust)
        print("thrust = ", thrust)
        time.sleep(0.5)
        
    def Close(self):
        time.sleep(0.1)
        self._cf.close_link()
        print("Schliesse Link")
        time.sleep(0.1)

    def Open(self):
        ScanCfly()        
        time.sleep(0.1)
        self._cf.open_link(gl_link_uri)
        print("Öffne     Link")
        time.sleep(0.1)        
        
def ScanCfly():
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)
    # Scan for Crazyflies and use the first one found
    print("(2) Scanning interfaces for Crazyflies...")
    available = cflib.crtp.scan_interfaces()
    print("(2) Crazyflies found:")
    l = 1
    for i in available:
        print(l, i[0])
        l += 1
        
    if len(available) > 0:
        le = MotorRampExample(available[0][0])
        print(l, "(2) After le", le)
        print()
    else:
        print("(2) No Crazyflies found, cannot run example")
    
#    return le

if __name__ == '__main__':
    print('Name = main')


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    print('test')
    cflib.crtp.init_drivers(enable_debug_driver=False)
    # Scan for Crazyflies and use the first one found
    print("(1) Scanning interfaces for Crazyflies...")
    available = cflib.crtp.scan_interfaces()
    print("(1) Crazyflies found:")
    for i in available:
        print(i[0])

    if len(available) > 0:
        le = MotorRampExample(available[0][0])
        print("(1) After le", le)
    else:
        print("(1) No Crazyflies found, cannot run example")




