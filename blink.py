# Testing file to develop blinking LED strip for IP address and battery
import socket 

ip_address = socket.gethostbyname(socket.gethostname())

def convert_to_eight_bit_binary(number):
    binary = bin(number)[2:]  # Convert the number to binary and remove the "0b" prefix
    binary = binary.zfill(8)  # Pad the binary string with leading zeros to ensure it is eight bits long
    return binary

number = 10
binary_string = convert_to_eight_bit_binary(number)
print(binary_string)
