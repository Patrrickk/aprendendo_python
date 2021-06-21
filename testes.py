import time

thc = ['Tfuex$n(lhgda     uvcm     bstoihm   zedbfiyza',  # 0
       'Tçwejynizhxea     uqvmzoa     bpsoqka   ççtqwafarebdmqe',  # 1
       'ToIe23ndahjua     uqwmjta     bxçohsa   itnfbozqiiytpqe',  # 2
       'Vgyaqui   iedykolsrdxmitiqjr']  # 3
g = ['''O12b12r12i12g12a12d12o   12p12o1pr     t12e12s12t12a12r     m12e12u        c12ó12d12i12g12o     :  ) ',
     '... MoPefmuz#   DfUi2#szpci0ocbrlqdry   >     Pjkkf5#1w0zo6nx1aj6''']

hora = time.localtime().tm_hour

if 6 <= hora <= 12:
    print(thc[0][::3])
elif 12 <= hora <= 18:
    print(thc[1][::3])
elif 18 <= hora <= 24:
    print(thc[2][::3])
else:
    print(thc[3][::3])

ff = [g[0][::3]]
for b in range(0, len(ff[0])):
    time.sleep(.1)
    # print(thca[0][b], end='')
    print(ff[0][b], end='')


# thx = ['T..e..n..h..a     u..m     b..o..m   ..d..i..a']
# tha = ['T..e..n..h..a     u..m..a     b..o..a   ..t..a..r..d..e']
# thb = ['T..e..n..h..a     u..m..a     b..o..a   ..n..o..i..t..e']
