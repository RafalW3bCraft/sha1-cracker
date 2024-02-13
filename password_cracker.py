import hashlib


def crack_sha1_hash(hash, use_salts=False):
  pass_arr = []
  read_add_arr('top-10000-passwords.txt', pass_arr)

  if use_salts:
    salt_pass = {}
    salt = []
    read_add_arr('known-salts.txt', salt)
    for bsalt in salt:
      for bpass in pass_arr:
        salt_pass[hashlib.sha1(bsalt + bpass).hexdigest()] = bpass.decode('utf-8')
        salt_pass[hashlib.sha1(bpass + bsalt).hexdigest()] = bpass.decode('utf-8')
    if hash in salt_pass:
      return salt_pass[hash]

  pass_dict = {}
  for pw in pass_arr:
    hash_ln = hashlib.sha1(pw).hexdigest()
    pass_dict[hash_ln] = pw.decode('utf-8')

  if hash in pass_dict:
    return pass_dict[hash]
    
  return 'PASSWORD NOT IN DATABASE'    


def read_add_arr(file_name, arr):
  with open(file_name, 'rb') as f:
    for line in f:
      arr.append(line.strip())
