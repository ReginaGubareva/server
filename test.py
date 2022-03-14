import logging
from protocol.protocol import Protocol
import codecs
from protocol.packet_parser import  *
import binascii
import protocol.constants as c


logger = logging.getLogger('websockets.server')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

A1_example = bytes([25, 31, 32, 33, 23, 33, 32, 31, 25, 0xff, 0xff, 1, 0xFF, 0xFF, 0xCA, 0x4B, 0xA4, 0xFF,
                    0xfc, 0x0C, 0x11, 0x4B, 0xFF, 0xFA, 0xF1, 0xF3, 234, 89, 23, 11, 255, 100, 100, 100,
                    0xfc, 0x0C, 0x11, 0x4B, 12, 0, 80, 80, 1, 0, 0xff, 0xff])
A2_example = bytes([25, 31, 32, 33, 23, 33, 32, 31, 25, 0xff, 0xff, 99, 0xff, 0xff])
B1_example = bytes([25, 34, 35, 36, 23, 36, 35, 34, 25, 0xff, 0xff, 99, 0xff, 0xff, 0xff, 0xff])
C1_example = bytes([25, 37, 38, 39, 23, 39, 38, 37, 25, 0xff, 0xff, 99, 1, 41, 3, 0xff, 4, 0xff, 4, 0xcf,
                     3, 0xff, 4, 0xff, 4, 0xcf, 0, 0, 0xff, 0xab])
print(len(C1_example))
A2_string = "%123#321%, 65535, 99, 255"
A1_string = "%123#321%, 65535, 1, 255.255.202.75.164.255, 252.12.17.75, 255.250.241.243, " \
             "234.89.23.11, 255.100.100.100, 252.12.17.75, 3072, 80, 80, 1, 0, 65535"

B1_string = "%456#654%, 65535, 99, 65535, 65535" # turn on and turn off the charger, get max current(second message from serve)

# in charger process the server get the message type C, with
# when the charger complete client send C message with the state B, and the charger free for other operation
C1_string = "%789#987%, 65535, 100, 297, 1023, 1279, 1231, 1023, 1279, 1231, 0, 0, 65451" # the first string

# device id defined by producer, but after it will be change with A message
# because the charger need to be configure with wifi and ethernet,
# I don't respond to anything
# 150

# TODO: server ask state of powerbox
# TODO: the introduction messages for powerbox

def string_to_bytes(message):
    msg_arr = message.split(", ")
    byte_arr = []
    for i in range(len(msg_arr[0])):
        byte_arr.append(int(hex(ord(msg_arr[0][i]))[2:]))
    if msg_arr[0] == c.HEADER_B:
        id_device = int(msg_arr[1]).to_bytes(2, byteorder="big")
        command = int(msg_arr[2]).to_bytes(1, byteorder="big")

        checksum = int(msg_arr[4]).to_bytes(2, byteorder="big")
        byte_arr.append(int(hex(id_device[0]), 16))
        byte_arr.append(int(hex(id_device[1]), 16))
        byte_arr.append(int(hex(command[0]), 16))
        current = int(msg_arr[3])
        if 255 >= int(current):
            byte_arr.append(0)
            byte_arr.append(int(hex(current), 16))
        else:
            current = int(current).to_bytes(2, byteorder="big")
            byte_arr.append(int(hex(current[0]), 16))
            byte_arr.append(int(hex(current[1]), 16))
        byte_arr.append(int(hex(checksum[0]), 16))
        byte_arr.append(int(hex(checksum[1]), 16))
    else:
        for i in msg_arr[1:]:
            if i.__contains__("."):
                buff = i.split(".")
                for j in buff:
                    if int(j) >= 255:
                        hex_array = int(j).to_bytes(2, byteorder="big")
                        byte_arr.append(int(hex(hex_array[0]), 16))
                        byte_arr.append(int(hex(hex_array[1]), 16))
                    byte_arr.append(int(hex(int(j)), 16))
            else:
                if int(i) >= 255:
                    hex_array = int(i).to_bytes(2, byteorder="big")
                    byte_arr.append(int(hex(hex_array[0]), 16))
                    byte_arr.append(int(hex(hex_array[1]), 16))
                else:
                    byte_arr.append(int(hex(int(i)), 16))

    return bytes(byte_arr)


parse_B(B1_example)
parse_B(string_to_bytes(B1_string))
# print(string_to_bytes(B1_string))
# print(len(B1_example))
# print(len(string_to_bytes(B1_string)))
# print(B1_example)
# print(string_to_bytes(B1_string) == B1_example)





























# address = ('192.168.1.29', 1501)
# log_level = logging.INFO
# logging.basicConfig(format='%(levelname)s-%(message)s', level=logging.INFO)
# client = Client(address, log_level, v6=False)
# client.startClient()
#
# try:
#     try:
#         PORT = 1501
#         if len(sys.argv) > 2:
#             if sys.argv[2] == '-d':
#                 log_level = logging.DEBUG
#     except:
#         print("Please provide valid port")
#         os._exit(0)
#     server = Server(log_level)
#     server.startServer(PORT)
# except KeyboardInterrupt:
#     os._exit(0)
