from collections import namedtuple

packet_A1 = namedtuple("packet_A1", "header, device_id, command, mac, local_ip, gateway, dns, subnet, \
                       destination_ip, port, reserved, version, checksum")

packet_A2 = namedtuple("packet_A2", "header, device_id, command, checksum")

packet_B = namedtuple("packet_B", "header, device_id, command, max_current, checksum")

packet_C = namedtuple("packet_C", "header, device_id, command, state, current1, current2, current3, "
                                  "voltage1, voltage2, voltage3, reserved, checksum")


def print_packet_A1(packet):
    print("|", packet.header, "|", packet.device_id, "|", packet.command, "|", packet.mac, "|\n",
          packet.local_ip, "|", packet.gateway, "|", packet.dns, "|", packet.subnet, "|\n",
          packet.destination_ip, "|", packet.port, "|", packet.reserved, "|", packet.version, "|",
          packet.checksum, "|")


def print_packet_A2(packet):
    print("|", packet.header, "|", packet.device_id,
          "|", packet.command, "|", packet.checksum, "|")


def print_packet_B(packet):
    print("|", packet.header, "|", packet.device_id,
          "|", packet.command, "|", packet.max_current, "|", packet.checksum, "|")


def print_packet_C(packet):
    print("|", packet.header, "|", packet.device_id, "|", packet.command, "|", packet.state, "|",
          packet.current1, "|", packet.current2, "|", packet.current3, "|",
          packet.voltage1, "|", packet.voltage2, "|", packet.voltage3, "|",
          packet.reserved, "|", packet.checksum, "|")
