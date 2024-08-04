from typing import Dict
from base64 import b64encode, b64decode
from codecs import encode, decode
from hashlib import md5
from traceback import format_exc

def print_heading(txt: str) -> None:
    div: str = "+" + ("-" * (len(txt) + 2) + "+")
    print(("\n" * 5) + f"{div}\n| {txt} |\n{div}\n")

def read_in(prompt: str) -> None:
    inp: str = input(prompt).strip()
    while len(inp) == 0:
        print("An input is required, please try again.")
        inp = input(prompt).strip()
    return inp

def rot13_encrypt(plaintext: str) -> str:
    return encode(plaintext, "rot_13")

def rot13_decrypt(ciphertext: str) -> str:
    return decode(ciphertext, "rot_13")

def rot13_cipher_cli() -> None:
    print_heading("ROT13 Cipher")
    
    print("""How would you like to proceed?
    1... Encrypt
    2... Decrypt
    3... Back to Main Menu
          """)
    encrypting: bool = None
    match read_in("Choice: "):
        case "1":
            encrypting = True
            print("Selected encryption tool.")
        case "2":
            encrypting = False
            print("Selected decryption tool.")
        case "3":
            print("Going back to Main Menu.")
            return
    
    in_file_name: str = read_in("File name/path to read input data: ")
    out_file_name: str = read_in("File name/path to read output data: ")

    try:
        with open(out_file_name, "wt") as out_file:
            with open(in_file_name, "rt") as in_file:
                lines: list[str] = in_file.readlines()
                if len(lines) == 0:
                    print("Error: No content to read from input file")
                    return
                
                if encrypting:
                    out_file.write("r:")
                    out_file.writelines([rot13_encrypt(line) for line in lines])
                else:
                    if len(lines[0]) < 2 or lines[0][:2] != "r:":
                        print("Error: File does not appear to have been encrypted using the ROT13 tool")
                        return
                    lines[0] = lines[0][2:]
                    out_file.writelines([rot13_decrypt(line) for line in lines])
                
                print("Operation completed successfully.")
    except BaseException:
        print(f"Error: {format_exc()}")

def stream_cipher(in_text: bytes, key: str) -> bytes:
    out_text: bytearray = bytearray(in_text)
    key_ba: bytearray = bytearray(key, encoding="utf-8")
    key_i: int = 0

    if len(in_text) == 0:
        raise ValueError("input is empty")
    if len(key_ba) == 0:
        raise ValueError("key bytearray is empty")

    for i in range(len(out_text)):
        out_text[i] ^= key_ba[key_i]
        key_i += 1
        if key_i == len(key_ba):
            key_i = 0

    return bytes(out_text)

def stream_cipher_cli_encrypting(key: str, in_file_name: str, out_file_name: str) -> None:
    with open(out_file_name, "wt") as out_f:
        with open(in_file_name, "rb") as in_f:
            out_f.write("s:")
            ciphertext: bytes = stream_cipher(in_f.read(), key)
            if ciphertext is None:
                raise ValueError("ciphertext cannot be None")
            out_f.write(b64encode(ciphertext).decode())
            out_f.write(":" + md5(key.encode()).hexdigest())

def stream_cipher_cli_decrypting(key: str, in_file_name: str, out_file_name: str) -> None:
    with open(out_file_name, "wb") as out_f:
        with open(in_file_name, "rb") as in_f:
            in_b: bytearray = bytearray(in_f.read())
            if len(in_b) < 35:
                print("Error: Insufficient content to read.")
                return
            if in_b[:2] != bytearray("s:", encoding="utf-8"):
                print("Error: Ciphertext does not appear to have been encrypted using the stream cipher tool.")
                return
            in_b = in_b[2:-33]
            decoded: bytes = b64decode(bytes(in_b))
            decrypted: bytes = stream_cipher(decoded, key)
            out_f.write(decrypted)
 

def stream_cipher_cli() -> None:
    print_heading("Stream Cipher")
    
    print("""How would you like to proceed?
    1... Encrypt
    2... Decrypt
    3... Back to Main Menu
          """)
    encrypting: bool = None
    match read_in("Choice: "):
        case "1":
            encrypting = True
            print("Selected encryption tool.")
        case "2":
            encrypting = False
            print("Selected decryption tool.")
        case "3":
            print("Going back to Main Menu.")
            return
        
    key: str = read_in("Enter cipher key: ")
    in_file_name: str = read_in("File name/path to read input data: ")
    out_file_name: str = read_in("File name/path to read output data: ")
    try:
        if encrypting:
            stream_cipher_cli_encrypting(key, in_file_name, out_file_name)
        else:
            stream_cipher_cli_decrypting(key, in_file_name, out_file_name)
        print("Operation completed successfully")
    except BaseException:
        print(f"Error: {format_exc()}")

def exit_cli() -> None:
    print_heading("Thank you and goodbye...")
    exit(0)

def pause_cli() -> None:
    print("...Press [ENTER] to continue...", end="")
    input()
    print()

def main() -> None:
    print_heading("Welcome to the Supercrypt System")

    while True:
        print(f"""Please select a subprogram:
    1... ROT13 Cipher
    2... Stream Cipher
    3... Exit 
        """)

        choices: Dict[str, callable] = {
            "1": rot13_cipher_cli,
            "2": stream_cipher_cli,
            "3": exit_cli
        }
    
        inp: str = read_in("Choice: ")

        if inp in choices:
            choices[inp]()
            pause_cli()
        else:
            print(f"Invalid choice: {inp}")
                

if __name__ == "__main__":
    main()

