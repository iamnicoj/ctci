def triple_sep(n, memo={}):
    if memo.get(n, None) is not None: return memo[n]
    if n == 0: return 1;
    if n < 0: return 0;

    memo[n] = triple_sep(n-1, memo) + triple_sep(n-2, memo) + triple_sep(n-3, memo)
    return memo[n]

print(triple_sep(0))
print(triple_sep(1))
print(triple_sep(2))
print(triple_sep(3))
print(triple_sep(4))
print(triple_sep(5))
print(triple_sep(6))
print(triple_sep(7))
print(triple_sep(8))
print(triple_sep(9))
print(triple_sep(10))
print(triple_sep(11))
print(triple_sep(12))
print(triple_sep(99))

