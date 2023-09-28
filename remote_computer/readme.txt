Remote Computer is defined as the computer decoding HID outside of the AUV craft.
Python Program will take a HID (either Controller or Joystick) and convert it to a thrust command.
These are then processed in two ways: Display, and Serial output.
The Serial Output is to connect to a Raspberry Pi within the AUV.
This connection will contain a command requesting for specific motor thrusts.
Uses Python 3.10 (64-bit) via Visual Studio 2022