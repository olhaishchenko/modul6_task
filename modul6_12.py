import base64


def encode_data_to_base64(data):
    data_end = []
    for i in data:
        message_bytes = i.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("utf-8")
        data_end.append(base64_message)
    return data_end
print(encode_data_to_base64(['andry:uyro18890D', 'steve:oppjM13LL9e']))

    
    
 