#!/usr/bin/env python

import re
import sys
import base64
import numpy as np
import os.path as path
from hashlib import sha256
from Crypto.Cipher import AES

def main():

  MASTER_KEY = "master.key"
  SECRET_KEY = "hudson.util.Secret"
  CREDENTIALS = "credentials.xml"

  file_not_found = False;

  base_dir = ""
  if(len(sys.argv) > 1):
      base_dir = sys.argv[1]

  # Check if files exist
  master_key_file_path  = path.join(base_dir, MASTER_KEY)
  secret_key_file_path  = path.join(base_dir, SECRET_KEY)
  credentials_file_path = path.join(base_dir, CREDENTIALS)

  if (not path.exists(master_key_file_path)):
    print(master_key_file_path + " does not exist.")
    file_not_found = True
  
  if(not path.exists(secret_key_file_path)):
    print(secret_key_file_path + " does not exist.")
    file_not_found = True

  if(not path.exists(credentials_file_path)):
    print(credentials_file_path + " does not exist.")
    file_not_found = True

  if(file_not_found):
    return

  # read the files
  master_key = open(master_key_file_path).read()
  hudson_secret_key = open(secret_key_file_path, 'rb').read()
  credentials = open(credentials_file_path).read()
  
  # get the SHA256 digest master key
  master_key_digest = sha256(master_key.encode('utf-8')).digest()[:16]
  # decrypt the secret key using the hashed master key
  cipher = AES.new(master_key_digest, AES.MODE_ECB)
  plaintext = cipher.decrypt(hudson_secret_key)
  # slice the actual key: the first 16 bytes
  secret_key = plaintext[:16]

  usernames = re.findall(r'<username>(.*?)</username>', credentials)
  passwords = re.findall(r'<password>(.*?)</password>', credentials)   
  userpass = np.column_stack((usernames,passwords))
    
  for userpass_entry in userpass:
    username = userpass_entry[0]
    password_base64 = base64.b64decode(userpass_entry[1])
    cipher = AES.new(secret_key, AES.MODE_ECB)
    plaintext = cipher.decrypt(password_base64).decode(errors='ignore')

    # return the match with the pattern MAGIC
    password = re.findall("(.*)::::MAGIC::::", plaintext)[0]
    if(password != None):
      print (username + ":" + password)

if __name__ == "__main__":
    main()

