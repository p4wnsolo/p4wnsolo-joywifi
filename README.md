# p4wnsolo-joywifi
Use OLED Joystick to input WiFi password on P4wnP1

## Connect P4wnP1 to WiFi without p4wnsolo-joywifi
Need to connect to WiFi via command line / Web GUI after booting up P4wnP1 for the first time?

Here's how:

1.  Open the Terminal
2.  Enter this command:  `P4wnP1_cli wifi set sta -s WiFiNetworkName -k MyPassword`
3.  Wait a few seconds (about 5 seconds for RPi 0 W) and try `ping -c2 google.com`


## Install Luma.OLED
`sudo pip3 install luma luma.oled`

## Install numpy
`sudo pip3 install numpy`

## Install Pillow
`sudo apt-get update`

`apt-get install libjpeg-dev zlib1g-dev`

`pip3 install Pillow`

## Enable SPI
https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/

## Possible Errors:
I ran into the following error(s) the first time I tried to install luma.core on a fresh P4wnP1 install:
 
`main.RequiredDependencyException: jpeg`

`  Failed building wheel for pillow`

`The headers or library files could not be found for jpeg,`

`  a required dependency when compiling Pillow from source.`

I re-ran the command to install luma and it gave me the same pillow / jpeg error:

`Failed building wheel for pillow`

### Error Fix for Python: The imagingft C module is not installed

`sudo apt-get install libfreetype6-dev`

`sudo -s`

`pip3 uninstall Pillow`

`pip3 install --no-cache-dir Pillow`

## Working folder (for dev):

root@kali:~/BeBoXGui-dev/p4wnsolo-dev/p4wnsolo-joyterm#

## Images & Process Example

First, we scan for WiFi networks:

![First, we scan for WiFi networks:](/images/p4wnsolo-joywifi-scanning.jpg "Scan for WiFi")

If you saved the last-connected WiFi network, it asks to reconnect (if the network is found again

![Ask to reconnect WiFi:](/images/p4wnsolo-joywifi-ask-to-reconnect.jpg "Ask to reconnect")

Reconnecting to WiFi..

![Reconnecting](/images/p4wnsolo-joywifi-reconnecting.jpg "Reconnecting to WiFi")

If you don't Reconnect, then we select a network using the OLED Joystick:

![Select WiFi](/images/p4wnsolo-joywifi-wifi-networks.jpg "Select WiFi")

Here's the "Input WiFi password" screen:

![Enter WiFi password](/images/p4wnsolo-joywifi-password-input.jpg "Enter WiFi password")

And here's what it looks like if you press the Backspace key (KEY2):

![Backspace Key for OLED text entry](/images/p4wnsolo-joywifi-backspace.jpg "Backspace Key for OLED text entry")

The script shows your IP address after it connects to WiFi:

![IP Address display](/images/p4wnsolo-joywifi-connected-ip-address.jpg "IP Address display")

It also checks your Internet connection by pinging Google:

![Pinging Google](/images/p4wnsolo-joywifi-link-quality.jpg "Pinging Google")

We can save our WiFi SSID & password (unsafely in a txt file - be careful):

![Save WiFi](/images/p4wnsolo-joywifi-save-network.jpg "Save WiFi")

Finally, the script displays the p4wnsolo Dashboard (Demo):

![Show dashboard](/images/p4wnsolo-joywifi-dashdemo.jpg "Show dashboard")


## Resources Used:
* [ThisPointer.com](https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/) - Get last X characters of a string in Python using negative indexing.  Used to enable "long input strings", where there are more characters in the text input string than the screen can handle.
