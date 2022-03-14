import protocol.constants as c

def convert_bytes_to_decimal(byte_array):
    result = int(str(byte_array.hex()), 16)
    return result


def convert_bytes_to_string(byte_array):
    result = ''
    for i in byte_array:
        result = result + str(i) + ' '
    return result


def convert_header(header):
    result = ''
    for i in header:
        result = result + str(i)
    return bytes.fromhex(result).decode('utf-8')


def get_header(message):
    header = message[0:9]
    return convert_header(header)


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
