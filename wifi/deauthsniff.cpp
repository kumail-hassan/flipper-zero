//The ESP32 has the capability to filter and capture WiFi traffic, allowing it to detect and collect deauths and disassociations sent by WiFi clients and APs in the vicinity against any network or client.
//Upon capturing a packet, it undergoes inspection to identify the presence of a deauth or disassociation byte.

if ((snifferPacket->payload[0] == 0xA0 || snifferPacket->payload[0] == 0xC0 ) && (display_obj.display_buffer->size() == 0))
