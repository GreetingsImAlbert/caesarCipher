code = input("Code: ")
shift_key = input("Shift Code (+/-): ")
shift = 0
decipher = []


while True:
    try:
        shift = -1 * int(input("Shift Key (number): "))
        break
    except ValueError:
        continue


for c in range(len(code)):
    if shift_key[c] == '+':
        decipher.append(chr(ord(code[c]) + shift))
    elif shift_key[c] == '-':
        decipher.append(chr(ord(code[c]) - shift))
    else:
        raise Exception


decipher = ''.join(decipher)

print(decipher)
