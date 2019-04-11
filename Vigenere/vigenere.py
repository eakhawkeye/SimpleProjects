#!/usr/bin/python
# Quick Vigenere Ciphering with iterations
#
# Cipher: ( plain_text_letter.index + key_letter.index ) mod total_character_count = cipher_text_letter.index
# Decipher: ( cipher_text_letter.index - key_letter.index ) mod total_character_count = plain_text_letter.index
#



####################################
#             MODULES              #
####################################
import argparse
import string



####################################
#            FUCNTIONS             #
####################################

def cipher_message(message, cipher_key, cipher_op, lst_map, num_total):
    len_msg = len(message)
    len_key = len(cipher_key)
    return [ lst_map[(lst_map.index(list(message)[i]) + ( cipher_op * lst_map.index(list(cipher_key)[i % len_key])) ) % num_total] for i in range(0, len_msg) ]



####################################
#              MAIN                #
####################################

def main():
    # Prepare the basics
    lst_char_map = list(string.ascii_uppercase)
    total_char = len(lst_char_map)

    # Parse user arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", "-k",
                  required=True,
                  default=None,
                  help="Cipher Key")
    parser.add_argument("--message", "-m",
                  required=True,
                  default=None,
                  help="Message")
    parser.add_argument("--decrypt", "-d",
                  required=False,
                  action='store_true',
                  default=False,
                  help="Decrypt instead of encrypt")
    parser.add_argument("--iterations", "-i",
                  required=False,
                  default=1,
                  type=int,
                  help="Number of iterations of encryption (default: 1)")
    parser.add_argument("--nononsense", "-n",
                  required=False,
                  action='store_true',
                  default=False,
                  help="Just output the final message")
    args = parser.parse_args()

    # Clean the key and message
    clean_message = filter(str.isalpha, args.message).upper()
    clean_key = filter(str.isalpha, args.key).upper()

    # 1=cipher -1=decipher
    cipher_op = int(-1 if args.decrypt else 1)
    cipher_iter = int(1 if args.iterations < 1 else args.iterations)

    # Prepare the output if needed
    if not args.nononsense:
        print '     input: %s' % clean_message
        print '       key: %s' % clean_key
        print '    output:',

    # Iterate through to de/cipher the message
    i_message = clean_message
    for i in range(0, cipher_iter):
        i_message = ''.join(cipher_message(i_message, clean_key, cipher_op, lst_char_map, total_char))

    print '%s' % i_message



####################################
#               RUN                #
####################################

if __name__ == '__main__':
    main()