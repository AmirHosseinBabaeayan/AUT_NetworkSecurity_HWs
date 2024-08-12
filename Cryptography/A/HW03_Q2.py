str_in = '53bba305))6*;4826)4b.)4b);806*;48a8¶60))85;;]8*;:b*8a83(88)5*a;46(;88*96*?;8)*b(;485);5*a2:*b(;4956*2(5*-4)88*;4069285);)6a8)4bb;1(b9;48081;8:8b1;48a85;4)485a528806*81(b9;48;(88;4(b?34;48)4b;161;:188;b?;'

frequency_counter = {}

for ch in str_in:
    if frequency_counter.get(ch, True):
        frequency_counter[ch]= str_in.count(ch)
    
    continue

print(frequency_counter)

str_with_most_frequnted_ch = str_in.replace('8', 'E')

print("string after replace e and 8: ")
print(str_with_most_frequnted_ch)

str_with_most_frequnted_THE = str_with_most_frequnted_ch.replace(';4E', 'THE')
print(" string after replace ;4E and THE:")
print(str_with_most_frequnted_THE)

frequency_counter = {}


