# #
# # ? SYNTAXIS
# byte_n = b''

# cadena_bytes = b'1010101010101010' # REPRESENTACION DE BINARIO

# cadena_byte = b'\x00\x1f'
# print(cadena_byte)
# print(type(cadena_byte))

# print(bin(543))
# print(type(bin(543)))

# # * 00000010 = 2 
# # * 0000 = 0
# # * 0010 = 2

# # * 00011111 = 31
# # * 0001 = 1
# # * 1111 = 15

#  # ? 543

# print(hex(543))
# print(type(hex(543)))
# print(b'\x02\x1f')

# num_byte = b'\x02\x1f'
# print(int.from_bytes(num_byte, "big"))

# * 65 = A
# print(ord("A"))
print(bin(1000))

# * Binario = 01000001
# * 0100 = 4
# * 0001 = 1
caracter_byte = b'\x41'

print(int.from_bytes(caracter_byte, "big"))
print(chr(65))

# * 0000 0011  = 03      1110 1000 = E8

caracter_byte2 = b'\x03\xE8'
print(int.from_bytes(caracter_byte2, "big"))
print(chr(1000))

# TODO: CREA UN PROGRAMA HEXADECIMAL DE "Hola mundo". (Solo mostrar codigo hexadecimal)