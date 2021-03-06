import base64
import hashlib


def decrypt(b64):
    b64 = str(base64.b64decode(b64), encoding='utf8')  # base64转换后是byte类型数据
    key = 'ISCC'
    m = hashlib.md5()
    m.update(key.encode())
    md = m.hexdigest()
    b64_len = len(b64)
    x = 0
    char = ''
    for i in range(b64_len):  # strlen($str)==strlen($char)==strlen($data)
        if x == len(md):
            x = 0
        char += md[x]
        x += 1
    data = ''
    # 也可不进行正负判断：data += chr((ord(b64[i]) - ord(char[i])+128) % 128)
    for i in range(b64_len):
        d = ord(b64[i]) - ord(char[i])
        if d > 0:  # 进行判断，如果相减小于0，说明需要加上128
            data += chr(d)
        else:
            data += chr(d + 128)
    print(data)


if __name__ == "__main__":
    b64 = 'fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA='
    decrypt(b64)
