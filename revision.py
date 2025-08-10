
# for va input operatori
dostlar=[]
print('5ta eng yaqin dostingizni kiriting')
for n in range(5):
    dostlar.append(input(f"{n+1}  eng yaqin dostingzini kiriting>"))
#amaliyot
ismlar=['abbos','sobit','muzakkir','misha','mirshohid']
for n in ismlar:
    print(f"salom {n}")
ismlar.append(input(f"bu yerda {ismlar} {len(ismlar)} marta takrorlandi"))

toq_sonlar=list(range(1,101,2))

for son in toq_sonlar:
    print(son**3)

kinolar=[]
print('5ta sevimli filmingiz qaysilar')
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)


x=[]

for n in range(5):
    x.append(input(f"bugun kimlar bilan gaplashding>{n+1}-odam>"))
print(f"siz bugun {x} lar bilan gaplashgansiz")


