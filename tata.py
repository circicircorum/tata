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
                  '02-1' : 'p;p-wat;what-is-at;what-is-at notation;',
                  '03' : 'b;bld;bld-memo;bld memo notation (buffer-agnostic);'}

_nf_modes_uncompressed_dict = {'01-f' : 'w-full', '02-f' : 'p-full'}


# some moves/states (mostly for reference, usage possible)
_nf_solved_w_expanded_unannotated = 'ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx'
# positions of one of the stickers of each piece uniquely determines a cube state (c->8 or 7, e->12 or 11)
_nf_solved_w_compressed_unannotated_bare = 'ABCDMNOPabcdhfrtmnop'
# w and p notations are the same in the solved state
_nf_solved_p_expanded_unannotated = _nf_solved_w_expanded_unannotated
_nf_solved_p_compressed_unannotated_bare = _nf_solved_w_compressed_unannotated_bare

compress_notation_debug = False
def compress_notation(cube, mode='01', human_readable=True, prefix_mode=False):
    if mode != '01':
        print('compress_notation: other modes are not yet supported, returning original cube...')
        return cube

    # mode: 'w';'01';
    if cube[0] == 'w':
        cube_stripped = cube[2:-1]
        cube_stripped = cube_stripped.replace(',', '')
    elif cube[0:3] == '01_':
        cube_stripped = cube[3:-1]
    else:
        cube_stripped = cube
    cs = cube_stripped

    if human_readable == True:
        ## cube_in_compressed_notation = ''.join([[cube[x] for x in [0,1,2,3]].append(',').append([cube[x] for x in [12,13,14,15]])])
        cicnl = []
        cube_in_compressed_notation_list = cicnl
        fu_corners = [0,1,2,3]
        fd_corners = [12,13,14,15]
        pos_a = _nf_solved_w_expanded_unannotated.index('a')
        pos_h = _nf_solved_w_expanded_unannotated.index('h')
        pos_r = _nf_solved_w_expanded_unannotated.index('r')
        pos_m = _nf_solved_w_expanded_unannotated.index('m')
        # print(f"pos_a: {pos_a}, pos_h: {pos_h}, pos_r: {pos_r}, pos_m: {pos_m}")
        # pos_a = 24
        # pos_h = 31
        # pos_r = 41
        # pos_m = 36

        fu_edges = [pos_a, pos_a + 1, pos_a + 2, pos_a + 3]
        se_edges = [pos_h, pos_h - 2, pos_r, pos_r + 2]
        fd_edges = [pos_m, pos_m + 1, pos_m + 2, pos_m + 3]
        if compress_notation_debug == True:
            print(f"compress_notation debug, pos_* test:: pos_a: {pos_a}, pos_h: {pos_h}, pos_r: {pos_r}, pos_m {pos_m}")
        for piece_type in [fu_corners, fd_corners, fu_edges, se_edges, fd_edges]: # U/D-face corners/edges and E-slice edges
            cicnl.append(''.join([cs[x] for x in piece_type]))
            cicnl.append(',')
        if compress_notation_debug == True:
            print(f"compress_notation debug, cincl value:: {cicnl}")
        cube_in_compressed_notation = ''.join(cicnl[:-1]) # remove trailing comma

    elif human_readable == False:
        cube_in_compressed_notation = ''.join([cs[x] for x in [0,1,2,3,12,13,14,15,24,25,26,27,31,29,41,43,36,37,38,39]])

    if prefix_mode == True:
        return '_'.join(['w', cube_in_compressed_notation, ''])
    else:
        return cube_in_compressed_notation

def expand_notation(cube, mode='01'):
    print('expand_notation: function stub for expand_notation.')

debug_translate_mode = False
debug_translate_mode_second = False
def translate_mode(mode_a, mode_b):
    # e.g. ABCDEFGHIJKL
    cube_eg = '01_1_MGTN,KDQV_2_lsij,kvxq,unef_'
    cube_explication = 'A@M, B@G, etc.'
    alt_cube_eg = '02_1_'
    proc_exp = 'at A -> look for piece at A-loc (i.e. A,F,V) -> found P@V => ~X(?)(no!!)~ Q@A'
    cube_fuller = '01_MGTN,ILPJ,EHUC,KDQV,ASBW,ORXF,lsij,cvgk,rhot,unef,wxbq,pmad'

    alg_proc = ''
    print('UNIMPLEMENTED: translate_mode stub...')

    # move_mapping = '01_MGTN,ILPJ,EHUC,KDQV,ASBW,ORXF,lsij,cvgk,rhot,unef,wxbq,pmad'
    cube                = 'MGTNILPJEHUCKDQVASBWORXFlsijcvgkrhotunefwxbqpmad'
    code_mapping        = 'ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx'
    solved_cube_state   = 'ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx'

    new_cube_l = []
    for p in solved_cube_state:
        if p in cube:
            if debug_translate_mode_second == True:
                pass
            new_cube_l.append(code_mapping[cube.index(p)])
        else:
            if debug_translate_mode == True:
                print(f'translate_mode: {p} not in mapping')
            new_cube_l.append(p)

    new_cube_translation = ''.join(new_cube_l)
    # new_cube_translation = new_cube_translation.replace('w_', 'p_', 1)
    return new_cube_translation

_nf_move_mapping_dict = {
    # x-moves
    'x'     : 'TQRSCBADJKLIHEFGONMPXUVWtqrsbadcjklihefgnmpoxuvw',
    'x2'    : 'PONMRQTSKLIJDCBAFEHGWXUVonmpqtsrklijcbadehgfwxuv',
    'x\''   : 'GFEHNOPMLIJKSRQTBCDAVWXUfehgnopmlijkrqtsbcdavwxu',
    # y-moves
    'y'     : 'BCDAVUXWGFEHNOPMLIJKSTQRbcdavuxwfehgnopmlijkrstq',
    'y2'    : 'CDABTSRQXUVWOPMNHGFEJKLIcdabsrqtuvwxopmngfehijkl',
    'y\''   : 'DABCKJILRSTQPMNOWXUVFEHGdabcjilkrstqpmnoxuvwfehg',
    # U-moves
    'U'     : 'BCDAVUGHIFELMNOPQRJKSTWXbcdavfghieklmnopqrjtuswx',
    'U2'    : 'CDABTSGHIUVLMNOPQRFEJKWXcdabsfghivklmnopqretujwx',
    'U\''   : 'DABCKJGHISTLMNOPQRUVFEWXdabcjfghisklmnopqrvtuewx',
    # F-moves
    'F'     : 'JBCIHEFGONKLMWVPQRSTUDAXabcihefgnjklmwopqrstuvdx',
    'F2'    : 'NBCOGHEFVWKLMADPQRSTUIJXabcnghefwjklmdopqrstuvix',
    'F\''   : 'WBCVFGHEDAKLMJIPQRSTUONXabcwfghedjklmiopqrstuvnx',
    # R-moves
    'R'     : 'ABRSCFGDJKLIHEOPQNMTUVWXabrdefgcjklihnopqmstuvwx',
    'R2'    : 'ABNMRFGSKLIJDCOPQEHTUVWXabmdefgrklijcnopqhstuvwx',
    'R\''   : 'ABEHNFGMLIJKSROPQCDTUVWXabhdefgmlijkrnopqcstuvwx',
    # D-moves
    'D'     : 'ABCDEFILRJKQPMNOWXSTUVHGabcdeflhijkqpmnoxrstuvwg',
    'D2'    : 'ABCDEFRQXJKWOPMNHGSTUVLIabcdefqhijkxopmngrstuvwl',
    'D\''   : 'ABCDEFXWGJKHNOPMLISTUVQRabcdefxhijkgnopmlrstuvwq',
    # B-moves
    'B'     : 'AXUDEFGHIJBCKNOLRSTQPVWMaucdefghijblmnokrstqpvwx',
    'B2'    : 'AMPDEFGHIJXUBNOCSTQRLVWKapcdefghijulmnobstqrkvwx',
    'B\''   : 'AKLDEFGHIJMPXNOUTQRSCVWBakcdefghijplmnoutqrsbvwx',
    # L-moves
    'L'     : 'GFCDEOPHIJKLMNQTBRSAVWXUfbcdeoghijklmntpqrsavwxu',
    'L2'    : 'POCDEQTHIJKLMNBAFRSGWXUVobcdetghijklmnapqrsfwxuv',
    'L\''   : 'TQCDEBAHIJKLMNFGORSPXUVWtbcdeaghijklmnfpqrsoxuvw'
}


debug_perform_move = False
debug_perform_move_second = False

alpha = 'abcdefghijklmnopqrstuvwx'
alpha_cap = alpha.upper()
_nf_solved_cube_state_w = ''.join([alpha_cap, alpha])
if debug_perform_move_second == True:
    print(_nf_solved_cube_state_w)
if debug_perform_move == True:
    print(f'alpha_cap: {alpha_cap}')

def perform_move(cube, move):
    if move in _nf_move_mapping_dict:
        move_mapping = _nf_move_mapping_dict[move]
    else:
        print(f"perform_move: Unimplemented move {move} was asked to be performed. Returning original cube...")
        return cube

    new_cube_l = []
    for p in cube:
        if p in move_mapping:
            if debug_perform_move_second == True:
                to_add = move_mapping[_nf_solved_cube_state_w.index(p)]
                print(f"pm: {to_add}")
            new_cube_l.append(move_mapping[_nf_solved_cube_state_w.index(p)])
        else:
            if debug_perform_move == True:
                print(f'perform_move: {p} not in mapping')
            new_cube_l.append(p)

    new_cube = ''.join(new_cube_l)
    return new_cube

# create a list of move primitives used to check the validity of moves (in do_move)
_nf_primitive_moves_list_bare = ['x', 'y', 'U', 'F', 'R', 'D', 'B', 'L']
_nf_primitive_moves_list = []
for bm in _nf_primitive_moves_list_bare:
    _nf_primitive_moves_list.extend([bm, bm + '2', bm + '\''])

debug_prim_list = False
if debug_prim_list == True:
    print(f"debug(pl):: _nf_primitive_moves_list: {_nf_primitive_moves_list}")


# N.B. move compositions are supposed to be lists of primitive moves
_nf_composite_moves_dict = {
    # composite moves
    'sexy' : ['R', 'U', 'R\'', 'U\'']
}

def do_move(cube, move):
    # decide how the move should be performed
    if move in _nf_primitive_moves_list:
        if debug_prim_list == True:
            print(f"{move} is a primitive move.")
        cube = perform_move(cube, move)
    elif move in _nf_composite_moves_dict.keys():
        if debug_prim_list == True:
            print(f"{move} is a composite move performed using ({' '.join(_nf_composite_moves_dict[move])})")
        cube = moves(cube, _nf_composite_moves_dict[move])
    else:
        print(f"do_move: Unimplemented move {move} was asked to be performed. Returning original cube...")
    return cube

_nf_suppress_warnings = False
def moves(cube, moves):
    if isinstance(moves, list):
        pass # maybe it will do sth in e futur
    else:
        if _nf_suppress_warnings == False:
            print(f"WARNING:: moves: the variable 'moves' is a {type(moves)} instead of a list; be very sure that this is what you want to do!")
    for move in moves:
        cube = do_move(cube, move)
    return cube

# nb the different ways in which the cube state is represented.
def make_new_cube(mode='01-l'):#mode='01'):

    # handle mode name transformations
    mode = mode.replace('w', '01', 1) # TBD: shd we w->01 or 01->w?
    mode = mode.replace('p', '02', 1) # be careful that this does not work in other contexts;
    mode = mode.replace('b', '03', 1) # replacing characters in cube states may affect edges etc.
    mode = mode.replace('m', '04', 1) # specifying how many instances to replace may help, but
    #mode = mode.replace('x', '05', 1) # when modes are implicit, edges may be affected anyway;
    #mode = mode.replace('l', '06', 1) # aka be careful/mindful when working on strings and consider
    #mode = mode.replace('s', '07', 1) # different situations/formats the cube state may be represented in.
    # nb w-l -> 01-l -> 01-06 (be sure that this is what you want to do)

    # w: where-is-it notation (wii,w)
    if mode == '01':
        return '01_1_ABCD,MNOP_2_abcd,hfrt,mnop_'
    # w-simp(?): implied corner-edge order, among other things
    if mode == '01-s':
        return '01_ABCD,MNOP_abcd,hfrt,mnop_'
    # w-learn: (tentatively for generating move mappings)
    if mode == '01-l':
        return '01_ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx'
    # w-learn-implied: mode wii is implied
    if mode == '01-li':
        return 'ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwx'
    # w-full: "human-readable" fully expanded notation for sanity checks and possibly convenience
    if mode == '01-f':
        return '011_1_ABCD,EFGH,IJKL,MNOP,QRST,UVWX_2_abcd,efgh,ijkl,mnop,qrst,uvwx_'
    # w-ultra-full: human-readable full notation with the reduced form in brackets
    if mode == '01-ff':
        return '0111_1_ABCD,EFGH,IJKL,MNOP,QRST,UVWX_(ABCD,MNOP)_2_abcd,efgh,ijkl,mnop,qrst,uvwx_(abcd,hfrt,mnop)_'
    # p: positional/what-is-at notation; identical to wii notation in the solved state
    if mode == '02-0' or mode == '02-1':
        return '02_1_ABCD,MNOP_2_abcd,hfrt,mnop_'
    # b: bld targets; empty string in solved state
    if mode == '03':
        return ''
    # m: moves performed; non-unique representation of a cube state; empty string in solved state
    if mode == '04':
        return ''

def main():
    return 'True'

if __name__ == '__main__':
    main()
