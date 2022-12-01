

# part 1
version_ids = []
def bits_transmission(binary, packet_len):
  # get packet version and remove it from the binary string
  packet_version = int(binary[0:3],2)
  binary = binary[3:]

  # append version id to ids list
  version_ids.append(packet_version)

  # get type id and remove it from the binary string
  type_id = int(binary[0:3],2)
  binary = binary[3:]

  # print(f"packet version is {packet_version}")
  # print(f"type_id is {type_id}")

  # decrement packet_length by 6 since we removed 6 binaries
  packet_len=packet_len-6

  # if this is a literal value packet
  if type_id == 4:
    bits = []
    for counter in range(int(packet_len/4)):
      binary = binary[1:]
      bits.append(binary[0:4])
      binary = binary[4:]
    # print(int("".join(bits),2))
    return binary

  # haha, more calculations if it is not literal value packet
  else:
    # get the length type id
    length_type_id = binary[0]
    # print(f"length type id is {length_type_id}")
    binary = binary[1:]

    if length_type_id == "0":
      total_length_in_bits = int(binary[0:15],2)
      binary = binary[15:]
      # print(f"total_length_in_bits is {total_length_in_bits}")
      for count in range(0, total_length_in_bits, 11):
        if total_length_in_bits - count >= 11*2:
           if "1" in binary[0:12]:
             binary  = bits_transmission(binary, len(binary[0:12]))
        elif len(binary) > 0:
           if "1" in binary[0:total_length_in_bits-count+1]:
             binary  = bits_transmission(binary, len(binary[0:total_length_in_bits-count+1]))

    if length_type_id == "1":
      number_of_subpackets = int(binary[0:11],2)
      binary = binary[11:]
      # print(f"number_of_subpackets is {number_of_subpackets}")
      for count in range(number_of_subpackets):
        if len(binary) < 11:
          break
        else:
          binary = bits_transmission(binary, 11)
  return binary


def convert_decimal_to_binary(input):
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


sample_input = "D2FE28"

example_0 ="EE00D40C823060"
example_1 ="8A004A801A8002F478"
example_2="620080001611562C8802118E34"
example_3="C0015000016115A2E0802F182340"
example_4="A0016C880162017C3686B18A3D4780"

input = "A20D5CECBD6C061006E7801224AF251AEA06D2319904921880113A931A1402A9D83D43C9FFCC1E56FF29890E00C42984337BF22C502008C26982801009426937320124E602BC01192F4A74FD7B70692F4A74FD7B700403170400F7002DC00E7003C400B0023700082C601DF8C00D30038005AA0013F40044E7002D400D10030C008000574000AB958B4B8011074C0249769913893469A72200B42673F26A005567FCC13FE673004F003341006615421830200F4608E7142629294F92861A840118F1184C0129637C007C24B19AA2C96335400013B0C0198F716213180370AE39C7620043E0D4788B440232CB34D80260008645C86D16C401B85D0BA2D18025A00ACE7F275324137FD73428200ECDFBEFF2BDCDA70D5FE5339D95B3B6C98C1DA006772F9DC9025B057331BF7D8B65108018092599C669B4B201356763475D00480010E89709E090002130CA28C62300265C188034BA007CA58EA6FB4CDA12799FD8098021400F94A6F95E3ECC73A77359A4EFCB09CEF799A35280433D1BCCA666D5EFD6A5A389542A7DCCC010958D85EC0119EED04A73F69703669466A048C01E14FFEFD229ADD052466ED37BD8B4E1D10074B3FF8CF2BBE0094D56D7E38CADA0FA80123C8F75F9C764D29DA814E4693C4854C0118AD3C0A60144E364D944D02C99F4F82100607600AC8F6365C91EC6CBB3A072C404011CE8025221D2A0337158200C97001F6978A1CE4FFBE7C4A5050402E9ECEE709D3FE7296A894F4C6A75467EB8959F4C013815C00FACEF38A7297F42AD2600B7006A0200EC538D51500010B88919624CE694C0027B91951125AFF7B9B1682040253D006E8000844138F105C0010D84D1D2304B213007213900D95B73FE914CC9FCBFA9EEA81802FA0094A34CA3649F019800B48890C2382002E727DF7293C1B900A160008642B87312C0010F8DB08610080331720FC580"

# binary_string = convert_decimal_to_binary(input)
# print(bits_transmission(binary_string, len(binary_string)))

# print(sum(version_ids))



#  testing out the prototype
# 110 100 0 1010
# 3   1     3 2

#  0   0       22          |  0   4     10  |  5   4     11  |  1   0        2       |           12  |  3         13
# 000 000 0 000000000010110| 000 100 0 1010 | 101 100 0 1011 | 001 000 1 00000000010 |000 100 0 1100 | 011 100 0 1101 00

# 00000000000 00000010110 00010001010 110100010111000001000000000101111000110000010001101000000

def prod(input):
  result = 1
  for x in input:
    result*=x
  return result

operations = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1])        
}


all_values = []
# part 2

def parse_type_4(packet):
    bit_index = 6
    parsed_literal = ""
    
    while True:
        parsed_literal += packet[bit_index + 1 : bit_index + 5]
        
        if packet[bit_index] == "0":
            break
        
        bit_index += 5
    
    return int(parsed_literal, 2), bit_index + 5


def parse_operators(packet):
    if packet[6] == "0":
        L = int(packet[7 : 22], 2)
        bit_index = 22
        numbers = []
        
        while bit_index < L + 22:
            result, length = bits_transmission_2(packet[bit_index : ])
            bit_index += length
            numbers.append(result)
    
    else:
        num_sub_packets = int(packet[7 : 18], 2)
        bit_index = 18
        numbers = []
        
        for _ in range(num_sub_packets):
            result, length = bits_transmission_2(packet[bit_index : ])
            bit_index += length
            numbers.append(result)
            
    return numbers, bit_index

def bits_transmission_2(binary):
  # total_result = 0
  # get packet version and remove it from the binary string
  packet_version = int(binary[0:3],2)
  # binary = binary[3:]

  # append version id to ids list
  # version_ids.append(packet_version)

  # get type id and remove it from the binary string
  type_id = int(binary[3:6],2)
  # binary = binary[3:]


  # print(f"packet version is {packet_version}")
  print(f"type_id is {type_id}")

  # decrement packet_length by 6 since we removed 6 binaries
  # packet_len=packet_len-5

  # if this is a literal value packet
  if type_id == 4:
    return parse_type_4(binary)

  # haha, more calculations if it is not literal value packet
  else:
    numbers, bit_index = parse_operators(binary)
  print(bit_index)
  # else:
  #   # get the length type id
  #   length_type_id = binary[0]
  #   binary = binary[1:]
  #   print(f"length type id is {length_type_id}")

  #   if length_type_id == "0":
  #     total_length_in_bits = int(binary[0:15],2)
  #     binary = binary[15:]

        
  #     print(f"total_length_in_bits is {total_length_in_bits}")
  #     values = []
  #     for count in range(0, total_length_in_bits, 11):
  #       if "1" not in binary:
  #         break
  #       if total_length_in_bits - count >= 11*2 and len(binary) > 0:
  #          if "1" in binary[0:12]:
  #            binary, value  = bits_transmission_2(binary, len(binary[0:12]))
  #            print("value is ", value)
  #            all_values.append(f"{type_id, value}")

  #       elif len(binary) > 0:
  #          if "1" in binary[0:total_length_in_bits-count+1]:
  #            binary, value  = bits_transmission_2(binary, len(binary[0:total_length_in_bits-count+1]))
  #            print("value is ", value)
  #     # print(values)
  #     if len(values) > 1:
  #       total_result=operations[type_id](values)
  #     elif len(values) > 0:
  #       total_result = values[0]



  #   if length_type_id == "1":
  #     number_of_subpackets = int(binary[0:11],2)
  #     binary = binary[11:]
  #     # print(f"number_of_subpackets is {number_of_subpackets}")
  #     values = []
  #     for count in range(number_of_subpackets):
  #       if "1" not in binary:
  #         break

  #       if len(binary) < 11:
  #         break
  #       else:
  #         binary, value = bits_transmission_2(binary, 11)
  #         print("value is ", value)
  #         values.append(value) 
  #     if len(values) > 1:
  #       total_result=operations[type_id](values)
  #     elif len(values) > 0:
  #       total_result = values[0]

  if type_id in operations:
      result = operations[type_id](numbers)

  return result, bit_index

binary_string = convert_decimal_to_binary(input)
print(bits_transmission_2(binary_string))

# print(sum(version_ids))