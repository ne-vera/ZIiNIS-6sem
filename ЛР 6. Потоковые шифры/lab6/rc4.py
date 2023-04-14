from math import pow, floor

n = 6
BLOCK_SIZE = floor(pow(2, 6))

def key_scheduling(key):
    sched = [i for i in range(0, BLOCK_SIZE)]
    i = 0
    for j in range(0, BLOCK_SIZE):
        i = (i + sched[j] + key[j % len(key)]) % BLOCK_SIZE
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
    return sched
    
def stream_generation(sched):
    i = 0
    j = 0
    while True:
        i = (1 + i) % BLOCK_SIZE
        j = (sched[i] + j) % BLOCK_SIZE
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        yield sched[(sched[i] + sched[j]) % BLOCK_SIZE]        

def rc4_encrypt(text, key):
    text = [ord(char) for char in text]
    key = [ord(char) for char in key]
    
    sched = key_scheduling(key)
    print('Инициализация таблицы замен:', sched)
    key_stream = stream_generation(sched)
    
    ciphertext = ''
    for char in text:
        enc = str(hex(char ^ next(key_stream))).upper()
        ciphertext += (enc)
        
    return ciphertext
    
def rc4_decrypt(ciphertext, key):
    ciphertext = ciphertext.split('0X')[1:]
    ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    key = [ord(char) for char in key]
    
    sched = key_scheduling(key)
    key_stream = stream_generation(sched)
    
    plaintext = ''
    for char in ciphertext:
        dec = str(chr(char ^ next(key_stream)))
        plaintext += dec
    
    return plaintext