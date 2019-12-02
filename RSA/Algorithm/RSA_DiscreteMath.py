def rsa_algorithm(p1, p2, e):
    n = p1 * p2
    phi_n = (p1 - 1) * (p2 - 1)
    for i in range(1, phi_n):
        if (i * e) % phi_n == 1:
            d = i
            break
    return n, phi_n, d
def encrypted_message(message, e, n):
    message = list(message)
    encrypted_message_num = []
    for i in message:
        i = ord(i) - 64
        encrypted_num = (i ** e) % n
        encrypted_str = str(encrypted_num)
        encrypted_message_num.append(encrypted_str.zfill(3))
    return encrypted_message_num

def decrypted_message(cipher_text, d, n):
    cipher_text = cipher_text.split()
    message = []
    for i in cipher_text:
        m = (int(i) ** d) % n
        m_text = chr(m + 64)
        message.append(m_text)
    message = "".join(message)
    return message

if __name__== "__main__":
    n, phi_n, d = rsa_algorithm(23, 31, 43)
    # Encryption
    message_num1 = encrypted_message("HELP", 43, n)
    print("The encrypted message of {} is: {}".format("'HELP'", message_num1))
    message_num2 = encrypted_message("COME", 43, n)
    print("The encrypted message of {} is: {}".format("'COME'", message_num2))
    
    print("\n-------------------------------------------------------------------\n")

    # Decryption
    decrypted_message1 = decrypted_message('675 089 089 048', d , n)
    print("The decrypted message of {} is: {}".format("'675 089 089 048'", decrypted_message1))
    decrypted_message2 = decrypted_message('028 018 675 129', d , n)
    print("The decrypted message of {} is: {}".format("'028 018 675 129'", decrypted_message2))
