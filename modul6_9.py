from codecs import utf_7_decode


def is_equal_string(utf8_string, utf16_string):
    utf8_decode = utf8_string.decode()
    utf16_decode = utf16_string.decode('utf-16')
    if utf8_decode.casefold() == utf16_decode.casefold():
        return True
    else:
        False
    
    
    