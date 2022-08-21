import argparse
from tools import *

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode',
                    type=str,
                    choices=['encrypt', 'decrypt', 'genkey'],
                    required=True, help='Choose operation mode')
parser.add_argument('-f', '--file_path', type=str, help='Path of the target file')
parser.add_argument('-k', '--key', type=str, help='Path of the key file')


args = vars(parser.parse_args())

if args['mode'] == 'genkey':
    generate_key()
else:
    if args['file_path'] == None or args['key'] == None:
        raise(Exception(message="If you use encrypt or decrypt mode, you need to fill -f and -k parameters"))

    key = b'0'
    with open(args['key'],'rb') as f:
        key = f.read()
    
    if args['mode'] == 'encrypt':
        encrypt(args['file_path'],key)
    else:
        decrypt(args['file_path'],key)

