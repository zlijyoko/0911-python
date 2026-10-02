# 字串轉為 list 才能進行更改。

s = "hello"
s_list = list(s)
s_list[0] = "H"
print("".join(s_list))