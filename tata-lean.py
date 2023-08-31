compress_notation() # usually to increase legibility for the user
expand_notation() # unimplemented as of yet;
translate_mode() # translate between w,p,b,m modes
perform_move() # actual manipulation of strings/cube-state
do_move() # prepare moves to be performed
do_move_sequence() # user-facing method; internal pre-processing
make_new_cube() # create (a string representing) a solved cube

_nf_primitive_moves_list # list of moves deemed "primitive" (length one?)
_nf_composite_moves_dict # dictionary of composite moves (convenience?)
_nf_move_mapping_dict # actual mappings/"multiplications" of characters representing pieces by move

# solved state representations
_nf_solved_w_expanded
_nf_solved_w_expanded_unannotated
_nf_solved_w_compressed
_nf_solved_w_compressed_unannotated
_nf_solved_w_compressed_unannotated_bare
_nf_solved_w_unannotated

# miscellaneous
_nf_suppress_warnings