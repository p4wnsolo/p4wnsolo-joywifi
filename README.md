# p4wnsolo-joywifi
Use OLED Joystick to input WiFi password on P4wnP1

## Connect P4wnP1 to WiFi without p4wnsolo-joywifi
Need to connect to WiFi via command line / Web GUI after booting up P4wnP1 for the first time?
Here's how:
1.  Open the Terminal
2.  Enter this command:  <code>P4wnP1_cli wifi set sta -s WiFiNetworkName -k MyPassword</code>
3.  Wait a few seconds (about 5 seconds for RPi 0 W) and try <code>ping -c2 google.com</code>


## Install Luma.OLED
<code>sudo pip3 install luma luma.oled</code>

## Install numpy
<code>sudo pip3 install numpy</code>

## Install Pillow
<code>sudo apt-get update</code>
<code>apt-get install libjpeg-dev zlib1g-dev</code>
<code>pip3 install Pillow</code>

## Enable SPI
https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/



Possible Errors:
I ran into the following error(s) the first time I tried to install luma.core on a fresh P4wnP1 install:
  \__main__.RequiredDependencyException: jpeg
  Failed building wheel for pillow
The headers or library files could not be found for jpeg,
  a required dependency when compiling Pillow from source.

I re-ran the command to install luma and it gave me the same pillow / jpeg error:
<code>  Failed building wheel for pillow  </code>

### Error Fix for Python: The _imagingft C module is not installed
sudo apt-get install libfreetype6-dev
sudo -s
pip3 uninstall Pillow
pip3 install --no-cache-dir Pillow


Working folder (for dev):
root@kali:~/BeBoXGui-dev/p4wnsolo-dev/p4wnsolo-joyterm#

First, we scan for WiFi networks:
<img src="/images/p4wnsolo-joywifi-scanning.jpg">

If you saved the last-connected WiFi network, it asks to reconnect (if the network is found again):
<img src="/images/p4wnsolo-joywifi-ask-to-reconnect.jpg">

Reconnecting to WiFi..
<img src="/images/p4wnsolo-joywifi-reconnecting.jpg">

If you don't Reconnect, then we select a network using the OLED Joystick:
<img src="/images/p4wnsolo-joywifi-wifi-networks.jpg">

Here's the "Input WiFi password" screen:
<img src="/images/p4wnsolo-joywifi-password-input.jpg">

And here's what it looks like if you press the Backspace key (KEY2):
<img src="/images/p4wnsolo-joywifi-backspace.jpg">

The script shows your IP address after it connects to WiFi:
<img src="/images/p4wnsolo-joywifi-connected-ip-address.jpg">

It also checks your Internet connection by pinging Google:
<img src="/images/p4wnsolo-joywifi-link-quality.jpg">

We can save our WiFi SSID & password (unsafely in a txt file - be careful):
<img src="/images/p4wnsolo-joywifi-save-network.jpg">

Finally, the script displays the p4wnsolo Dashboard (Demo):
<img src="/images/p4wnsolo-joywifi-dashdemo.jpg">
