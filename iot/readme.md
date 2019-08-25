IoT
===

Install Root CA cert
```
$ sh iot/setup.sh
```

Create IoT device and download certs. Copy certs into /iot/.device_cert
You will need to replace some values below depending on the url of your IoT Thing and name of certs

Example script run:
```
$ python iot/test_shadow_client.py -e a3q3e4ibv9kc5q-ats.iot.us-west-2.amazonaws.com -r iot/.device_cert/root-CA.crt -c iot/.device_cert/Test.cert.pem -k iot/.device_cert/Test.private.key
```