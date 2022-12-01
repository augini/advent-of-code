def prod(input):
  result = 1
  for x in input:
    result*=x
  return result

def hex_to_bin(input):
    binary = bin(int(input, 16))[2:]

    # append 0 to the beginning if initial digit is less than 8
    if input[0] == "0":
      binary = "0000"+binary
    if input[0] == "1":
      binary = "000"+binary
    elif input[0] == "2" or input[0] == "3" :
      binary = "00"+binary
    elif input[0] in "456":
      binary = "0"+binary
    return binary


def parse_header(s):
    return int(s[:3], 2), int(s[3:6], 2)


def parse_literal(packet):
    bit_index = 6
    parsed_literal = ""
    
    while True:
        parsed_literal += packet[bit_index + 1 : bit_index + 5]
        
        if packet[bit_index] == "0":
            break
        
        bit_index += 5
    
    return int(parsed_literal, 2), bit_index + 5


def parse_operator(packet):
    if packet[6] == "0":
        L = int(packet[7 : 22], 2)
        bit_index = 22
        numbers = []
        
        while bit_index < L + 22:
            result, length = parse_packet(packet[bit_index : ])
            bit_index += length
            numbers.append(result)
    
    else:
        num_sub_packets = int(packet[7 : 18], 2)
        bit_index = 18
        numbers = []
        
        for _ in range(num_sub_packets):
            result, length = parse_packet(packet[bit_index : ])
            bit_index += length
            numbers.append(result)
            
    return numbers, bit_index


def parse_packet(packet):  
    packet_version, type_id = parse_header(packet)

    if type_id == 4:
        return parse_literal(packet)
    
    else:
        numbers, bit_index = parse_operator(packet)
    
    print(numbers)
            
    if type_id in OPERATORS:
        result = OPERATORS[type_id](numbers)

    return result, bit_index


OPERATORS = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1])        
    }

data = "A20D5CECBD6C061006E7801224AF251AEA06D2319904921880113A931A1402A9D83D43C9FFCC1E56FF29890E00C42984337BF22C502008C26982801009426937320124E602BC01192F4A74FD7B70692F4A74FD7B700403170400F7002DC00E7003C400B0023700082C601DF8C00D30038005AA0013F40044E7002D400D10030C008000574000AB958B4B8011074C0249769913893469A72200B42673F26A005567FCC13FE673004F003341006615421830200F4608E7142629294F92861A840118F1184C0129637C007C24B19AA2C96335400013B0C0198F716213180370AE39C7620043E0D4788B440232CB34D80260008645C86D16C401B85D0BA2D18025A00ACE7F275324137FD73428200ECDFBEFF2BDCDA70D5FE5339D95B3B6C98C1DA006772F9DC9025B057331BF7D8B65108018092599C669B4B201356763475D00480010E89709E090002130CA28C62300265C188034BA007CA58EA6FB4CDA12799FD8098021400F94A6F95E3ECC73A77359A4EFCB09CEF799A35280433D1BCCA666D5EFD6A5A389542A7DCCC010958D85EC0119EED04A73F69703669466A048C01E14FFEFD229ADD052466ED37BD8B4E1D10074B3FF8CF2BBE0094D56D7E38CADA0FA80123C8F75F9C764D29DA814E4693C4854C0118AD3C0A60144E364D944D02C99F4F82100607600AC8F6365C91EC6CBB3A072C404011CE8025221D2A0337158200C97001F6978A1CE4FFBE7C4A5050402E9ECEE709D3FE7296A894F4C6A75467EB8959F4C013815C00FACEF38A7297F42AD2600B7006A0200EC538D51500010B88919624CE694C0027B91951125AFF7B9B1682040253D006E8000844138F105C0010D84D1D2304B213007213900D95B73FE914CC9FCBFA9EEA81802FA0094A34CA3649F019800B48890C2382002E727DF7293C1B900A160008642B87312C0010F8DB08610080331720FC580"

data_bin = hex_to_bin(data)

print("evaluated expression:", parse_packet(data_bin)[0])