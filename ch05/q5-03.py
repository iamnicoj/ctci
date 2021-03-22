def flip_to_win_own(num):
    longest, current_segment, past_segment = 1, 0, 0
    past_zero, ghost = False, False
    while num != 0:
        if num & 1: # Current bit is 1
            current_segment += 1
            past_zero = False
        else: # Current bit is 0
            if not past_zero: # first zero
                # include the current zero as 1 if no other 0 was added before
                # as a past 0 may have already counted when ghost == True
                past_segment += (1 + current_segment) if not ghost else current_segment 
                ghost = True if not ghost else False 
                current_segment = 0
                past_zero = True
            else: # double zeros
                past_segment = 1
                current_segment = 0
        longest = max(current_segment + past_segment, longest)
        num >>= 1  # Move 1 bit to the right
    return longest

def flip_to_win(num):
    longest, current_segment, past_segment = 1, 0, 0
    while num != 0:
        if num & 1: # Current bit is 1
            current_segment += 1
        else: # Current bit is 0
            past_segment = 0 if (num & 2 == True) else current_segment
            current_segment = 0
        longest = max(current_segment + past_segment + 1, longest)
        num >>= 1  # Move 1 bit to the right
    return longest



############
print(flip_to_win(0))
print(flip_to_win(1))
print(flip_to_win(2))
print(flip_to_win(3))
print(flip_to_win(4))
# 3 >>
print(flip_to_win(5)) # 101
print(flip_to_win(6)) # 110
print(flip_to_win(7)) # 111
# check
print(flip_to_win(8))   # 1000
print(flip_to_win(9))   # 1001
print(flip_to_win(10))  # 1010 ERROR
print(flip_to_win(11))  # 1011
print(flip_to_win(12))  # 1100
print(flip_to_win(13))  # 1101 
print(flip_to_win(14))  # 1110
print(flip_to_win(15))  # 1111
print(flip_to_win(16))  # 10000



