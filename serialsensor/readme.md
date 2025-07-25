For this to work the sensor must be hooked up by USB and needs to have the right script loaded to it.
The Port (COM6) can differ on other machines.

Using an ESP32 and the DHT Sensor one can measure some values and save them in a file
to generate some simple testdata.

TODO:
1. make testdata-file appendable (check if headers in first line are already there -> also shows if there is already some data: no headers = no data)
2. generate test data
3. mix test data with randomly occurring anomalies
4. train model on data (Isolation Forest?) -> possible guide: https://www.tensorflow.org/tutorials/generative/autoencoder#third_example_anomaly_detection
5. load model in program that streams serial data (formatted!!!)
6. let model predict with every read from serial (maybe just all 10 sec?)


Guide:
DHT Code:
https://randomnerdtutorials.com/esp32-dht11-dht22-temperature-humidity-sensor-arduino-ide/
Arduino settings:
https://42project.net/hello-world-erstes-projekt-mit-dem-esp8266-nodemcu-v3-und-der-arduino-ide-getting-started/
Boot button to upload code:
https://www.reddit.com/r/esp8266/comments/1ghqlkw/a_fatal_esptoolpy_error_occurred_failed_to/
https://randomnerdtutorials.com/how-to-install-esp8266-board-arduino-ide/
Install Driver if no CP210x Universal (COM6):
https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads
Pin Definitions Espressif ESP WROOM 32D:
https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf