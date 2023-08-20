from tata import *

def main():
    print('main:: compress_notation test...')
    print('human readable (T):', compress_notation('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx'))
    print('human readble (F):', compress_notation('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx', human_readable=False))
    print('human readable (T), mode prefixed:', compress_notation('w_ABCD,EFGH,IJKL,MNOP,QRST,UVWX,abcd,efgh,ijkl,mnop,qrst,uvwx_'))
    print('hr(T), mode prefixed, prefix mode:', compress_notation('w_ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx_', prefix_mode=True))
    print()

    if False:
        print('performing some test moves...')
        cube = make_new_cube()
        cube = moves(cube, ['R'])
        print(f"cube;R       : {cube}")
        cube = moves(cube, ['x', 'U'])
        print(f"cube;R x U   : {cube}")
        cube = moves(cube, ['R\''])
        print(f"cube;R x U R': {cube}")

        print()
        cube = make_new_cube()
        moveseq = ['R', 'U', 'R\'', 'U\'']
        cube = moves(cube, moveseq)
        print(f"{moveseq}: {cube}")
        print()

        for m in ['R', 'U', 'R\'', 'U\'']:
            cube = make_new_cube()
            cube = moves(cube, [m])
            print(f"cube:: {m}: {cube}")
        print()

    if False:
        # test (RUR'U')*6
        for i in range(13):
            cube = make_new_cube()
            moveseq = ['R', 'U', 'R\'', 'U\''] * i
            cube = moves(cube, moveseq)
            print(f"(R U R' U') x {i}: {cube}")
        print()

        # test R4
        for i in range(5):
            cube = make_new_cube()
            moveseq = ['R'] * i
            cube = moves(cube, moveseq)
            print(f"'R' x {i}: {cube}")
        print()

        # test U4
        for i in range(5):
            cube = make_new_cube()
            moveseq = ['U'] * i
            cube = moves(cube, moveseq)
            print(f"'U' x {i}: {cube}")
        print()

        # test F4
        for i in range(5):
            cube = make_new_cube()
            moveseq = ['F'] * i
            cube = moves(cube, moveseq)
            print(f"'F'x{i}: {cube}")
        print()

        # test ?4
        for m in ['U', 'F', 'R', 'D', 'B']: #, 'L']:
            for i in range(5):
                cube = make_new_cube()
                moveseq = [m] * i
                cube = moves(cube, moveseq)
                print(f"{m}x{i}: {cube}")
            print()

    if False:
        # test RU
        for i in range(45 * 6 + 1):
            cube = make_new_cube()
            moveseq = ['R', 'U'] * i
            cube = moves(cube, moveseq)
            if cube == make_new_cube():
                print(f"(R U)*{i}: {cube}")
        print()

        # test FU
        for i in range(45 * 6 + 1):
            cube = make_new_cube()
            moveseq = ['F', 'U'] * i
            cube = moves(cube, moveseq)
            if cube == make_new_cube():
                print(f"(F U)*{i}: {cube}")
        print()

        # test BU
        for i in range(45 * 6 + 1):
            cube = make_new_cube()
            moveseq = ['B', 'U'] * i
            cube = moves(cube, moveseq)
            if cube == make_new_cube():
                print(f"(B U)*{i}: {cube}")
        print()

        # test DU
        for i in range(4 * 3 + 1):
            cube = make_new_cube()
            moveseq = ['D', 'U'] * i
            cube = moves(cube, moveseq)
            if cube == make_new_cube():
                print(f"(D U)*{i}: {cube}")
        print()
    
    if False:
        # test scramble (no L-moves)
        print()
        # N.B. that StO to BTFR reqs z' x';
        # i.e. scramble: "z' x' F B R' B U B R F2 U' R2 F2 D' R2 U F2 R2 D' B2 U' R F'" from StO;
        move_seq_spec = "F B R' B U B R F2 U' R2 F2 D' R2 U F2 R2 D' B2 U' R F'"
        move_seq_spec_l = move_seq_spec.split()
        for m in move_seq_spec_l:
            #cube = moves(cube, move_seq_spec_l)
            cube = moves(cube, [m])
            print(f'cube +{m}:\t{cube}')
        print()
    
    cube_ttl = translate_mode('a', 'b')
    print(f'tl_mode test: {cube_ttl}')
    # w_ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx_
    cnct = compress_notation(cube_ttl, prefix_mode=True)
    # cnct = compressed_notation_cube_ttl
    cnct = cnct.replace('w_', 'p_1_', 2)
    cnct = cnct.replace(',', '.', 2)
    cnct = cnct.replace('.', ',', 1)
    cnct = cnct.replace('.', '_2_', 1)
    print(f'cube_ttl: {cnct}')
    # print(f'hr(T), mode prefixed, prefix mode, +extra edits: {cnct}')

if __name__ == '__main__':
    main()