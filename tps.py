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


debug_perf_move = False
def perf_move(cube, move_mapping):
    alpha = 'abcdefghijklmnopqrstuvwx_,'
    alpha_cap = alpha.upper()
    if debug_perf_move == True:
        print(f'alpha_cap: {alpha_cap}')

    new_cube_l = []
    for p in cube:
        if p in alpha_cap:
            new_cube_l.append(move_mapping[alpha_cap.index(p)])
        else:
            if debug_perf_move == True:
                print(f'perfmove: {p} not in mapping')
            new_cube_l.append(p)

    new_cube = ''.join(new_cube_l)
    return new_cube

def perfX(cube):
    xp_rot_map = 'GFEHNOPMLIJKSRQTBCDAVWXU_,'
    xpd = perf_move(cube, xp_rot_map)
    ##print(xpd)
    return xpd

def perfU(cube):
    U_move_map = 'BCDAVUGHIFELMNOPQRJKSTWX_,'
    Ud = perf_move(cube, U_move_map)
    return Ud

def move(cube, move):
    if move == 'U':
        return perfU(cube)
    elif move == 'x':
        cube = perfX(cube)
        cube = perfX(cube)
        cube = perfX(cube)
        return cube

print()
print()
print()
print('xp test:')
print()

##if False:
cube = 'w_ABCD,MNOP_ca'
cube1 = perfX(cube)
print('1',cube1)
cube2 = perfX(cube1)
print('2',cube2)
cube3 = perfX(cube2)
print('3',cube3)
cube4 = perfX(cube3)
print('4',cube4)

print()
print()
print()
print('move test')

cube_t = 'w_ABCD,MNOP_ca'
cube_u = move(cube_t, 'U')
print(cube_u)
cube_ux = move(cube_u, 'x')
print(cube_ux)
cube_uxu = move(cube_ux, 'U')
print(cube_uxu)

