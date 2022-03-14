import zlib
from protocol import constants as c
from protocol.packet_parser import *


class ChecksumError(Exception):
    def __init__(self):
        self.msg = ""


class UnableToConnectException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Protocol:
    def __init__(self):
        self.winSize = c.WINDOW_SIZE
        self.clientWinSize = c.WINDOW_SIZE
        self.bufferedPackets = {}

    def parse_packet(self, packet):

        header = packet[:9]

        packet = string_to_bytes(packet)
        if header == c.HEADER_A:

        # TODO: here somehow zero comes
            if len(packet) == 56:
                print("------- Got packet A1 --------")
                packet_obj = parse_A1(packet)
                return "Command: " + str(packet_obj.command)

            if len(packet) == 14:
                print("------- Got packet A2 --------")
                packet_obj = parse_A2(packet)
                # respond_pack = respond_A2(packet_obj)
                return "Command: " + str(packet_obj.command)

        elif header == c.HEADER_B:
            print(header == c.HEADER_B)
            print("------- Got packet B --------")
            packet_obj = parse_B(packet)
            return "Max current:" + str(packet_obj.max_current)

        elif header == c.HEADER_C:
            print(header == c.HEADER_C)
            print("------- Got packet C --------")
            packet_obj = parse_C(packet)
            return "Current values:" + str(packet_obj.current1) + "|" + str(packet_obj.current2) + \
                   "|" + str(packet_obj.current3) + "|" + \
                   "Voltage values:" + str(packet_obj.voltage1) + "|" + str(packet.voltage2) + \
                   "|" + str(packet.voltage3)
        else:
            return "Invalid header. Can't process this message"

    def parse_packet_bytes(self, packet):
        print("This is parse packet function", packet)
        header = self.parse_header(packet)
        print("Header:", header.decode("utf-8"))

        checksum = self.generate_checksum(packet)
        print("Checksum generated:", checksum)

        if header.decode('utf-8') == c.HEADER_A:

            if len(packet) == 46:
                print("------- Parse packet A1 --------")
                packet_obj = parse_A1(packet)

                if packet_obj.checksum != checksum:
                    packet_obj = packet_obj._replace(checksum=0)
                return packet_obj

            if len(packet) == 14:
                print("------- Parse packet A2 --------")
                packet_obj = parse_A2(packet)
                if packet_obj.checksum != checksum:
                    packet_obj = packet_obj._replace(checksum=0)
                return packet_obj

        if header.decode('utf-8') == c.HEADER_B:
            print("------- Parse packet B --------")
            packet_obj = parse_B(packet)
            if packet_obj.checksum != checksum:
                packet_obj = packet_obj._replace(checksum=0)
            return packet_obj

        if header.decode('utf-8') == c.HEADER_C:
            print("------- Parse packet C --------")
            packet_obj = parse_C(packet)
            if packet_obj.checksum != checksum:
                packet_obj = packet_obj._replace(checksum=0)
            return packet_obj
        return "Invalid header. Can't process this message"

    @staticmethod
    def parse_header(packet):
        header = packet[:c.HEADER_LENGTH]

        if len(header) != c.HEADER_LENGTH:
            print('Invalid header length')
            return None

        result = ''
        for i in header:
            result = result + str(i)
        return bytes.fromhex(result)

    @staticmethod
    def generate_checksum(data, value=None):
        # print("data type:", data)
        if not value:
            return zlib.adler32(data)
        return zlib.adler32(data, value)

    def validate_checksum(self, checksum, data):
        if checksum != self.generate_checksum(data):
            return False
        return True
