# (in w-notation)
cube = '01_1_ABCD,MNOP_2_abcd,hfrt,mnop_'
td_corners = ['UFL', 'ULB', 'UBR', 'URF', # U-face, clockwise from bottom-left (blue in BTRF; ABCD ; 01020304 ;
                     'FUR', 'FLU', 'FDL', 'FRD', # F-face, ccw from top-right (red in BTRF); EFGH ; 05060708 ;
                     'RDF', 'RFU', 'RUB', 'RBD', # R-face, cw from bottom-left facing R (yellow in BTRF); IJKL ; 09101112 ;
                     'DRB', 'DFR', 'DLF', 'DBL', # D-face, ccw from bottom-right facing D (green in BTRF); MNOP ; 13141516 ;
                     'BLD', 'BDR', 'BRU', 'BUL', # B-face, cw from bottom-right facing B (orange in BTRF); QRST ; 17181920 ;
                     'LBU', 'LUF', 'LFD', 'LDB', # L-face, cw* from top-left facing L (white in BTRF); UVWX ; 21222324 ;
                     'YZ' ] # forms a cycle if not for the swapping of V and X on the L face for historical/arbitrary reasons.

td_edges = ['UL', 'UB', 'UR', 'UF',
            'FU', 'FL', 'FD', 'FR',
            'RF', 'RU', 'RB', 'RD',
            'DR', 'DF', 'DL', 'DB',
            'BD', 'BR', 'BU', 'BL',
            'LB', 'LU', 'LF', 'LD',
            'YZ']


# to be streamlined/removed/renamed at another date due to ambiguity in notation and inconsistency in representation
_nf_w_edges_state_solved = 'abcdefghijklmnopqrstuvwx_,'
_nf_w_corners_state_solved = 'ABCDEFGHIJKLMNOPQRSTUVWX_,'

_nf_w_edges_state_R = ''
_nf_w_corners_state_R = ''

_nf_w_edges_state_x = ''
_nf_w_corners_state_x = ''

_nf_modes_dict = {'01' : 'w;wii;where-is-it;where-is-it notation;', # implies compressed notation
                  '02-0' : 'p;p;positional;positional notation;', # likewise for all other modes in the current dictionary
                  '02-1' : 'p;p-wat;what-is-at;what-is-at notation;';
                  '03' : 'b;bld;bld-memo;bld memo notation (buffer-agnostic);'}

_nf_modes_uncompressed_dict = {'01-f' : 'w-full', '02-f' : 'p-full'}


# some moves/states (mostly for reference, usage possible)
_nf_solved_w_expanded_unannotated = 'ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx'
# positions of one of the stickers of each piece uniquely determines a cube state (c->8 or 7, e->12 or 11)
_nf_solved_w_compressed_unannotated_bare = 'ABCDMNOPabcdhfrtmnop'
# w and p notations are the same in the solved state
_nf_solved_p_expanded_unannotated = _nf_solved_w_expanded_unannotated
_nf_solved_p_compressed_unannotated_bare = _nf_solved_w_compressed_unannotated

# note: incomplete; does not account for edges yeta
compress_notation_debug = False
def compress_notation(cube, mode='01', human_readable=True):
    if mode != '01':
        print('compress_notation: other modes are not yet supported, returning original cube...')
        return cube
    if human_readable == True:
        ## cube_in_compressed_notation = ''.join([[cube[x] for x in [0,1,2,3]].append(',').append([cube[x] for x in [12,13,14,15]])])
        ## todo: add stripping / reformatting
        cicnl = []
        cube_in_compressed_notation_list = cicnl
        fu_corners = [0,1,2,3]
        fd_corners = [12,13,14,15]
        pos_a = _nf_solved_w_expanded_unannotated.indexof('a')
        pos_h = _nf_solved_w_expanded_unannotated.indexof('h')
        pos_r =  _nf_solved_w_expanded_unannotated.indexof('r')
        pos_f =  _nf_solved_w_expanded_unannotated.indexof('m')

        fu_edges = [pos_a, pos_a + 1, pos_a + 2, pos_a + 3]
        se_edges = [pos_h, pos_h - 2, pos_r, pos_r + 2]
        fd_edges = [pos_m, pos_m + 1, pos_m + 2, pos_m + 3]
        if compress_notation_debug == True:
            print(f"pos_* test:: pos_a: {pos_a}, pos_h: {pos_h}, pos_r: {pos_r}, pos_f: {pos_f}")
        for piece_type in [fu_corners, fd_corners, fu_edges, fd_edges]: # fu -> U-face, fd -> D-face, etc.
            cicnl.append([cube[x] for x in piece_type])
            cicnl.append(',')
        cube_in_compressed_notation = ''.join(cicnl)

    elif human_readable == False:
        cube_in_compressed_notation = ''.join([cube[x] for x in [0,1,2,3,12,13,14,15,24,25,26,27,36,37,38,39]])
    return cube_in_compressed_notation

def expand_notation(cube, mode='01'):
    print('expand_notation: function stub for expand_notation.')

def translate_mode(mode_a, mode_b):
    pass

def perform_move(cube, move):
    pass

def move(cube, move):
    if move == 'R':
        cube = perform_move(cube, 'R')
    elif move == 'R2':
        cube = perform_move(cube, 'R')
        cube = perform_move(cube, 'R')
    elif move == 'R\'':
        cube = perform_move(cube, 'R2') # note: recursion
        cube = perform_move(cube, 'R')
    elif move == 'U':
        cube = perform_move(cube, 'U')
    elif move == 'x':
        cube = perform_move(cube, 'x')
    return cube

def moves(cube, moves):
    for move in moves:
        cube = move(cube, move)
    return cube

# note the different ways in which the cube state is represented.
def make_new_cube(mode='01'):
    if mode == '01':
        return '01_1_ABCD,MNOP_2_abcd,hfrt,mnop_'
    if mode == '02-0' or mode == '02-1':
        return '02_1_ABCD,MNOP_2_abcd,hfrt,mnop_'
    if mode == '03':
        return ''


def main():
    print('compress_notation test:')
    print(compress_notation('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx'))
    print(compress_notation('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx', human_readable=False))

    cube = make_new_cube()
    cube = moves(cube, ['R'])
    print(f"cube;R: {cube}")
    cube = moves(cube, ['x', 'U'])
    print(f"cube;R: {cube}")
    print()
    return

if __name__ == '__main__':
    main()
