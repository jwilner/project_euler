
def concealed_square():
    min_num,max_num = 1010101000,int(int('9'.join(str(i) for i in [i for i in range(1,10)]+[0]))**.5)
    digit_positions = sorted(((i,v) for i,v in enumerate('1_2_3_4_5_6_7_8_9_0') if v != '_'),reverse=True)
    for i in range(max_num,min_num,10):
        if i % 3 != 0 or i % 7 != 0: continue
        squared = str(i*i)
        if all(v == squared[d] for d,v in digit_positions): return i
