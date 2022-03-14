MAX_PACKET_SIZE = 1024

WINDOW_SIZE = 5
MAX_SEQ_NUM = 65536
MAX_ACK_NUM = 65536
HEADER_LENGTH = 9  # length in bytes

MAX_ATTEMPTS = 3

SEND_TIMEOUT = 0.05
RECV_TIMEOUT = 0.5
CON_TIMEOUT = 0.5
PACKET_TIMEOUT = 0.175
END_TIMEOUT = 1

MAX_WINSIZE = 0xffff

# HEADERS
HEADER_A = "%123#321%"
HEADER_B = "%456#654%"
HEADER_C = "%789#987%"

command_B = {0: "turn off", 1: "turn on", 2: "max_current change"}

COMMANDS_A = {0: 'save settings',
              1: 'read settings'}  # код заказа/функции, отправленный сервером

COMMANDS_C = {100: 'auth',
              150: 'the charger send the state of charge to the server and current/voltage value'}  # код заказа/функции, отправленный сервером


STATES = {1: 'Estado A: VE is not connected',
          2: 'Estado B: VE is connected, but on hold',
          3: 'Estado C: VE on and charging',
          4: 'Estado D: VE on charge and air circulation is mandaroty'}

key_ethernet = {0x04, 0x0A, 0x04, 0x0B, 0x04, 0x0C,
                0x04, 0x0D, 0x04, 0x0E, 0x04, 0x0F,
                0x04, 0x0A, 0x04, 0x0B}
