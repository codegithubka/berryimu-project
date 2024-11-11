Main functionality
Reading IMU data on Pico W
- BerryIMU sensor measures accelaration and rotation in 3D
- The Pico W reads this data from the IMU using I2C communication
- IMU data reflects movements of the sensor

Sending Data Over Wifi using TCP:
- Pico conects to wifi and uses TCP to send data
- Pico W is acting as a TCP client; collects data from IMU, opens connection to RPi4 and sends data over Wifi
- IMU data is transmitted to RPi4 in real-time

Receiving data on RPi 4:
- Rpi4 listes fro connection as a TCP server
- Data arrives in a structured form
RPi4 can use this data for applications to send feedback that reacts to the senor's movement

