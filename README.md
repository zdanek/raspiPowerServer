# raspiPowerServer
simple serwer that allows to shutdown or reboot Raspberry Pi via http

run with
python server.js

you can define own port with third argument
python server.js PORT

default port is 7000

now call
http://raspberry.address:7000/
http://raspberry.address:7000/reboot
http://raspberry.address:7000/power/off


