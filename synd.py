#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""Tiny Synology DiskStation daemon

The service will turn off the blinking LED at startup and shut the
system down when the power button is pressed.
"""
import os
import signal
import sys

from serial import Serial

UART_PORT = "/dev/ttyS1"

POWER_BUTTON_PRESSED = b'0'
CMD_LED_POWER_BLINK = b'5'
CMD_LED_POWER_OFF = b'6'


def sigterm_handler(_signo, _stack_frame):
    sys.exit(0)


def wait_for_button_press(uart):
    while True:
        in_byte = uart.read(1)
        if in_byte == POWER_BUTTON_PRESSED:
            print("Triggering system shutdown...")
            os.system('/usr/sbin/poweroff')


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, sigterm_handler)
    uart = Serial(UART_PORT, 9600, timeout=1)
    try:
        uart.write(CMD_LED_POWER_OFF)
        wait_for_button_press(uart)
    finally:
        if uart:
            uart.write(CMD_LED_POWER_BLINK)
            uart.close()
