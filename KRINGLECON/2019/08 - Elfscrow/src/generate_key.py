KEY_LENGTH = 8
seed = 1576673497
key = ''
for i in range(KEY_LENGTH):
    seed = (214013 * seed + 2531011)
    b = hex(ord(chr(seed >> 16 & 0x7fff & 0x0ff)))[2:]
    if len(b) == 1:
        b = '0' + b
    key += b
print("key: %s" % key)