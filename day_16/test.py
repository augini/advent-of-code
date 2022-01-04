def hex_to_bin(s):
    return bin(int(s, 16))[2:]


version_ids= []
# leading 0's until the length is a multiple of 4
def leading_zeros(a):
    return "0" * ((4 - len(a) % 4) % 4) + a


def parse_header(s, to_decimal=False):
    return (int(s[0:3], 2), int(s[3:6], 2)) if to_decimal else (s[0:3], s[3:6])


def parse_literal(packet, to_decimal=False):
    num_bits = 5
    num_bin = packet[6:]
    binary_numbers = [num_bin[i:i+num_bits] for i in range(0, len(num_bin), num_bits)
                      if len(num_bin[i:i+num_bits]) == 5]

    # binary_numbers = [num for num in binary_numbers if num != "00000"]
    
    parsed_literal = ""
    parse_counter = 0
    
    for binary_number in binary_numbers:
        parsed_literal += binary_number[1:]
        parse_counter += 1
        
        # check if binary_number starts with a 0 and marks the last chunk
        if binary_number[0] == "0":
            # if there are more 5 bit chunks, consider them a new packet
            if len(binary_numbers) != parse_counter:
                parse_packet(num_bin[parse_counter * num_bits:])
            break
        
    if to_decimal:
        return int(parsed_literal, 2)
    
    return parsed_literal


def parse_operator(packet):
    length_type_id = packet[6]
    length_of_bits = 0
    
    if length_type_id == "0":
        length_of_bits = 15
    elif length_type_id == "1":
        length_of_bits = 11
    
    L_bin = packet[7:7+length_of_bits]
    L = int(L_bin, 2)

    if length_type_id == "0":
        sub_packets_1 = packet[7+length_of_bits:7+length_of_bits+L]
        sub_packets_2 = packet[7+length_of_bits+L:]
        parse_packet(sub_packets_1)
        parse_packet(sub_packets_2)

    elif length_type_id == "1":
        sub_packets = packet[7+length_of_bits:]
        parse_packet(sub_packets)


def parse_packet(packet):
    if packet.count("0") == len(packet):
        return
    
    packet_version, type_id = parse_header(packet, True)
    version_ids.append(packet_version)

    global version_counter
    version_counter += packet_version
    
    if type_id == 4:
        parse_literal(packet, True)
    else:
        parse_operator(packet)
    
    
data = "A20D5CECBD6C061006E7801224AF251AEA06D2319904921880113A931A1402A9D83D43C9FFCC1E56FF29890E00C42984337BF22C502008C26982801009426937320124E602BC01192F4A74FD7B70692F4A74FD7B700403170400F7002DC00E7003C400B0023700082C601DF8C00D30038005AA0013F40044E7002D400D10030C008000574000AB958B4B8011074C0249769913893469A72200B42673F26A005567FCC13FE673004F003341006615421830200F4608E7142629294F92861A840118F1184C0129637C007C24B19AA2C96335400013B0C0198F716213180370AE39C7620043E0D4788B440232CB34D80260008645C86D16C401B85D0BA2D18025A00ACE7F275324137FD73428200ECDFBEFF2BDCDA70D5FE5339D95B3B6C98C1DA006772F9DC9025B057331BF7D8B65108018092599C669B4B201356763475D00480010E89709E090002130CA28C62300265C188034BA007CA58EA6FB4CDA12799FD8098021400F94A6F95E3ECC73A77359A4EFCB09CEF799A35280433D1BCCA666D5EFD6A5A389542A7DCCC010958D85EC0119EED04A73F69703669466A048C01E14FFEFD229ADD052466ED37BD8B4E1D10074B3FF8CF2BBE0094D56D7E38CADA0FA80123C8F75F9C764D29DA814E4693C4854C0118AD3C0A60144E364D944D02C99F4F82100607600AC8F6365C91EC6CBB3A072C404011CE8025221D2A0337158200C97001F6978A1CE4FFBE7C4A5050402E9ECEE709D3FE7296A894F4C6A75467EB8959F4C013815C00FACEF38A7297F42AD2600B7006A0200EC538D51500010B88919624CE694C0027B91951125AFF7B9B1682040253D006E8000844138F105C0010D84D1D2304B213007213900D95B73FE914CC9FCBFA9EEA81802FA0094A34CA3649F019800B48890C2382002E727DF7293C1B900A160008642B87312C0010F8DB08610080331720FC580"

data_bin = hex_to_bin(data)
data_bin = leading_zeros(data_bin)
version_counter = 0

parse_packet(data_bin)
print(version_counter)
version_ids.sort()
print(version_ids)