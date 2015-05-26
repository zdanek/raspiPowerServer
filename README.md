# raspiPowerServer
simple serwer that allows to shutdown or reboot Raspberry Pi via http

run with
```
sudo python server.py &
```

you can define own port with third argument
```
sudo python server.py PORT &
```

default port is 7000

now call
```
http://raspberry.address:7000/
http://raspberry.address:7000/reboot
http://raspberry.address:7000/power/off
```


