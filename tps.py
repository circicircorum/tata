def map_characters(input_str, src_str, mapping_str):
    char_map = dict(zip(src_str, mapping_str))
    output_str = ''.join(char_map[char] for char in input_str if char in char_map)
    return output_str

src_str = 'abcdefghijklmnopqrstuvwxyz'
mapping_str = 'efghabcdmnopijklqrstuvwxyz'
input_str = '_abcd,mnop_'

ss = 'ABCDEFGHIJKLMNOPQRSTUVWX_,'
ms = 'BCDAVUGHIFELMNOPQRJKSTWX_,'
qs = '_ABCD,MNOP_'

#mc  = map_characters
rs = map_characters(qs, ss, ms)
print(rs)
print()

output_str = map_characters(input_str, src_str, mapping_str)
print(output_str)




def perfX(cube):
    xp_rot_map = 'GFEHNOPMLIJKSRQTVWXU_,'
    xpd = map_characters(cube, ss, xp_rot_map)
    #print(xpd)
    return xpd

print()
print()
print()
print('xp test:')
print()

cube = qs
cube1 = perfX(cube)
print('1',cube1)
cube2 = perfX(cube1)
print('2',cube2)
cube3 = perfX(cube2)
print('3',cube3)
cube4 = perfX(cube3)
print('4',cube4)


