The ESP32 possesses the capability to filter and capture WiFi traffic, allowing it to identify and collect AP beacons transmitted by nearby WiFi Access Points.

Upon capturing a packet, the application verifies the presence of the beacon byte. This functionality operates similarly to Beacon Sniff, but it also includes access points with distinctive BSSIDs in the list of targets for WiFi attacks.
if ((snifferPacket->payload[0] == 0x80) && (display_obj.display_buffer->size() == 0))
