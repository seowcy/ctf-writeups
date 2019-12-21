from Crypto.Cipher import DES
import PyPDF2
import os


KEY_LENGTH = 8
START = 1575658800
END = 1575666000
IV = 8 * b'\x00'

with open('ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf.enc', 'rb') as f:
    ciphertext = f.read()

for seed in range(START, END):
    key = ''
    for i in range(KEY_LENGTH):
        seed = (214013 * seed + 2531011)
        b = hex(ord(chr(seed >> 16 & 0x7fff & 0x0ff)))[2:]
        if len(b) == 1:
            b = '0' + b
        key += b
    cipher = DES.new(bytes.fromhex(key), DES.MODE_CBC, IV=IV)
    with open('output/%s.pdf' % key, 'wb') as f:
        f.write(cipher.decrypt(ciphertext))
    try:
        with open('output/%s.pdf' % key, "rb") as f:
            PyPDF2.PdfFileReader(f)
        print("DECRYPTION SUCCESSFUL! -> %s.pdf" % key)
        break
    except PyPDF2.utils.PdfReadError:
        os.remove('output/%s.pdf' % key)
    
