import argparse

debug = False

parser = argparse.ArgumentParser(description="Encrypt text using a selected algorithm.")
parser.add_argument('-m', '--mode', required=True, choices=['encrypt', 'decrypt'], help="Choose to encrypt or decrypt")
parser.add_argument('-s', '--source', required=True, help="Path to the source.txt text file")
parser.add_argument('-o', '--output', required=True, help="Path to the output encrypted file")
parser.add_argument('-a', '--algorithm', required=True, help="Encryption algorithm to use")
parser.add_argument('-d', '--debug', action='store_true', help="Enable debug mode")
args = parser.parse_args()

def ceasarthree(content):
    return ''.join(chr(ord(c) + 3) for c in content)

def ceasarthree_decrypt(content):
    return ''.join(chr(ord(c) - 3) for c in content)


def shift_array(arr, x):
    return [element + x for element in arr]

def axoo_encrypt(content):
    ascii_values = [ord(char) for char in content]
    if debug:
        print(ascii_values)
    shifted_array = shift_array(ascii_values, 10)
    encrypted = ''.join(chr(((code - 32) % 95) + 32) for code in shifted_array)
    return encrypted

def axoo_decrypt(content):
    ascii_values = [ord(char) for char in content]
    if debug:
        print(ascii_values)
    shifted_back = shift_array(ascii_values, -10)
    decrypted = ''.join(chr(((code - 32) % 95) + 32) for code in shifted_back)
    return decrypted

def process(source_path, output_path, debugoption, algorithm, mode):
    global debug
    debug = debugoption

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if algorithm == "ceasarthree":
        result = ceasarthree(content) if mode == "encrypt" else ceasarthree_decrypt(content)
    elif algorithm == "axooencrypt":
        result = axooencrypt(content) if mode == "encrypt" else axoo_decrypt(content)
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"[+] {mode.capitalize()}ed using {algorithm} and saved to {output_path}")

if __name__ == '__main__':
    process(args.source, args.output, args.debug, args.algorithm, args.mode)
