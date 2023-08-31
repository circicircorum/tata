from tata import *

_s_cube = make_new_cube('w')
def do(moveseq, verbose=False):
    if isinstance(moveseq, str):
        moveseq = [moveseq]

    global _s_cube
    _s_cube = moves(_s_cube, moveseq)
    if verbose == True:
        print(f"_s_cube: {_s_cube}")

def basic_scramble_test():
    scrambles = ["D2 L' U F' U' B2 D L' F2 U' L2 D F2 D2 R2 D F2 D2 F2 R2 F'",
                "U R2 F2 R2 D L2 B2 F2 U' L2 R' D' B' L R2 F R D' L U'"]

    print('some arbitrary scrambles...')
    for i in range(len(scrambles)):
        scramble = scrambles[i]
        scramble_l = scramble.split()
        cube = make_new_cube(mode='01')
        cube = moves(cube, scramble_l)
        print(f"scramble_{i}_m = \"{scramble}\"")
        print(f"scramble_{i}_w = \"{cube}\"")

    print()
    print('testing more stuffs...')
    do("sexy sexy sexy sexy sexy".split(), verbose=True)
    do("R U R' U'".split(), verbose=True)
    print()

def synonyms_test():
    cube = make_new_cube('w')
    cube = do_move_sequence(cube, ['R'])
    print(f"synonyms_test: {cube}")

def main():
    basic_scramble_test()
    synonyms_test()

if __name__ == '__main__':
    main()