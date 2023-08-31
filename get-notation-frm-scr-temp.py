from tata import *

scramble = "y' x R' U' F R D R D2 F2 R' B2 R U2 R' B2 F2 R2 B' U' F' R' U B2 L F R' U' F x' y"
scramble_l = scramble.split()
print(f"scramble: {scramble}")

cube = make_new_cube()

### perf moves ###
cube = moves(cube, scramble_l)
print(f"post-scramble: {cube}") # output: post-scramble: 01_RNGKSMUXPCWJDQTAFEOIHLBVheatuwgxovlbsnkcjmdqpifr

### compress notation ###
cube_compressed = compress_notation(cube)
print(f"compress-notation (w): {cube_compressed}") # output: post-scramble: RNGK,DQTA,heat,xwmq,snkc

### translate to what-is-at notation ###
cube = translate_mode(cube[3:])
print(f"p-notation: {cube}") # output: p-notation: PWJMRQCUTLDVFBSINAEOGXKHclpsbwgavqokrniutxmdejfh

### compress notation ###
cube = compress_notation(cube)
print(f"post-scramble: {cube}") # output: post-scramble: PWJM,FBSI,clps,awxd,rniu


### output summary ###
# scramble: R' U' F R D R D2 F2 R' B2 R U2 R' B2 F2 R2 B' U' F' R' U B2 L F R' U' F
# post-scramble: 01_RNGKSMUXPCWJDQTAFEOIHLBVheatuwgxovlbsnkcjmdqpifr
# compress-notation (w): RNGK,DQTA,heat,xwmq,snkc
# p-notation: PWJMRQCUTLDVFBSINAEOGXKHclpsbwgavqokrniutxmdejfh
# post-scramble: PWJM,FBSI,clps,awxd,rniu
### [(y' x) : Scr] ###
# scramble: y' x R' U' F R D R D2 F2 R' B2 R U2 R' B2 F2 R2 B' U' F' R' U B2 L F R' U' F x' y
# post-scramble: 01_LHPOGRVKCWXBTSAJEUQNIMFDxcfihtkvawelmrsqpdjgnoub
# compress-notation (w): LHPO,TSAJ,xcfi,vtdg,mrsq
# p-notation: OLIXQWEBUPHAVTDCSFNMRGJKixbrkctedsglmuvqpnofwhja
# post-scramble: OLIX,VTDC,ixbr,ecnf,muvq