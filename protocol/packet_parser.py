from protocol.utils import *
from protocol.packet import *
from protocol.constants import *

# MSG Servidor→powerbox: enviar/ler configuração/reboot (S2P_A1)
def respond_A1(packet):
    # full_packet = packet_A1(header, device_id, command, mac, local_ip, gateway, dns, subnet,
    #                   destination_ip, port, reserved, version, checksum)
    print("Created message type A1 to Client.")

    return packet



# 2. MSG Servidor→powerbox: enviar/ler configuração/reboot (S2P_A2)
def respond_A2(packet):
    if packet.command == 0:
        print("Save settings, save a settings in database.")
    elif packet.command == 1:
        print("Read settings, is it how?")
    elif packet.command == 99:
        print("Reboot.")

    full_packet = packet_A2(packet.header, packet.device_id, packet.command, packet.checksum)
    print("Server has send message type A2 to Client.")
    return full_packet
#
# # 5. MSG Servidor→powerbox: enviar mensagem ligar/desligar (S2P_B)
# def send_B():
#     packet_B1 = bytes([25, 34, 35, 36, 23, 36, 35, 34, 25, 0xff, 0xff, 99, 0, 32, 0xff, 0xff])
#     # server.send(packet_B1)
#     print("Server has send message type B1 to Client.")
#     return packet_B1


# 3. MSG Cliente→ servidor: resposta a uma trama tipo A (P2S_A1)
def parse_A1(message):
    header = convert_header(message[0:9])
    print("header: ", header)

    device_id = convert_bytes_to_decimal(message[9:11])
    print("id_device: ", device_id)

    command = message[11]
    print("command: ", command)

    mac = convert_bytes_to_string(message[12:18])
    print("MAC: ", mac)

    local_ip = convert_bytes_to_string(message[18:22])
    print("local IP: ", local_ip)

    gateway = convert_bytes_to_string(message[22:26])
    print("gateway: ", gateway)

    dns = convert_bytes_to_string(message[26:30])
    print("DNS_4:", dns)

    subnet = convert_bytes_to_string(message[30:34])
    print("subnet:", subnet)

    destination_ip = convert_bytes_to_string(message[34:38])
    print("destination IP:", destination_ip)

    port = convert_bytes_to_decimal(message[38:40])
    print("Port:", port)

    reserved = convert_bytes_to_string(message[40:42])
    print("reserved bytes:", reserved)

    version = convert_bytes_to_string(message[42:44])
    print("firmware version:", version)

    checksum = convert_bytes_to_decimal(message[44:46])
    print("checksum:", checksum)


    packet = packet_A1(header, device_id, command, mac, local_ip, gateway, dns, subnet,
                       destination_ip, port, reserved, version, checksum)
    return packet


# 4. MSG Cliente→ servidor: resposta a uma trama tipo A (P2S_A2)
def parse_A2(message):
    header = get_header(message)
    print("header: ", header)

    device_id = convert_bytes_to_decimal(message[9:11])
    print("id_device: ", device_id)

    command = message[11]
    print("command: ", command)

    checksum = convert_bytes_to_decimal(message[12:13])
    print("checksum:", checksum)

    packet = packet_A2(header, device_id, command, checksum)
    return packet

# def parse_A2(message):
#     arr = message.split(", ")
#     header = arr[0]
#     print("header: ", header)
#
#     device_id = arr[1]
#     print("id_device: ", device_id)
#
#     command = arr[2]
#     print("command: ", command)
#
#     checksum = arr[3]
#     print("checksum:", checksum)
#
#     packet = packet_A2(header, device_id, command, checksum)
#     return packet

# 6. MSG powerbox→ servidor: resposta a uma trama tipo B (P2S_B)
def parse_B(message):
    print("------- Get response from powerbox type B -------")
    header = get_header(message)
    print("header: ", header)

    device_id = convert_bytes_to_decimal(message[9:11])
    print("id_device: ", device_id)

    command = message[11]
    print("command: ", command)

    max_current = convert_bytes_to_decimal(message[12:14])
    print("Maximal current:", max_current)

    checksum = convert_bytes_to_decimal(message[14:16])
    print("Checksum:", checksum)

    packet = packet_B(header, device_id, command, max_current, checksum)
    return packet


def parse_B_bytes(message):
    print("------- Get response from powerbox type B -------")
    header = get_header(message)
    print("header: ", header)

    device_id = convert_bytes_to_decimal(message[9:11])
    print("id_device: ", device_id)

    command = message[11]
    print("command: ", command)

    max_current = convert_bytes_to_decimal(message[12:14])
    print("Maximal current:", max_current)

    checksum = convert_bytes_to_decimal(message[14:16])
    print("Checksum:", checksum)

    packet = packet_B(header, device_id, command, max_current, checksum)
    return packet


# 7. MSG powerbox→ servidor: envio de uma trama tipo C (P2S_C)
def parse_C(message):
    print("------- Get response from powerbox type C -------")
    header = get_header(message)
    print("header: ", header)

    device_id = convert_bytes_to_decimal(message[9:11])
    print("id_device: ", device_id)

    command = message[11]
    print("command: ", command)

    state = convert_bytes_to_decimal(message[12:14])
    print("Analog input values:", state)

    current1 = convert_bytes_to_decimal(message[14:16])
    print("Current phase1:", current1)

    current2 = convert_bytes_to_decimal(message[16:18])
    print("Current phase2:", current2)

    current3 = convert_bytes_to_decimal(message[18:20])
    print("Current phase3:", current3)

    voltage1 = convert_bytes_to_decimal(message[20:22])
    print("Voltage phase1:", voltage1)

    voltage2 = convert_bytes_to_decimal(message[22:24])
    print("Voltage phase2:", voltage2)

    voltage3 = convert_bytes_to_decimal(message[24:26])
    print("Voltage phase3:", voltage3)

    reserved = convert_bytes_to_decimal(message[26:28])
    print("Reserved bytes:", reserved)

    checksum = convert_bytes_to_decimal(message[28:30])
    print("Checksum:", checksum)

    packet = packet_C(header, device_id, command, state, current1, current2, current3,
                      voltage1, voltage2, voltage3, reserved, checksum)

    string_packet = '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(str(header), str(device_id),
                                                                                    str(command), str(state),
                                                                                    str(current1), str(current2),
                                                                                    str(current3), str(voltage1),
                                                                                    str(voltage2), str(voltage3),
                                                                                    str(checksum))
    return packet, string_packet
