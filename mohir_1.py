#pythonda dasturlash asosolari
#Muallif:Anvar Narzullayev
#print('hello world')
#print('hayrli tong')
#pythonda funksiyalar:
#def salom_ber():
#     """salom beruvchi funksiya """
#     print("Assalomu aleykum")
#salom_ber()
#def salom_ber(ism):
#    """foydalanuvchi ismini qabul qilib unga 
#    salom beruvchi funksiya"""
#    print(f"Assalomu aleykum,hurmatli {ism.title()}!")
#salom_ber('hasan')
#salom_ber('olim')
#def  toliq_ism(ism,familiya):
#    """foydalanuvchini ismi va familiyasini jamlab chiqaruvchi
#    funksiya"""
#    print(f"foydalanuvchi ismi:{ism.title()}\n"
#          f"foydalanuvchi familiyasi:{familiya.title()}")
#toliq_ism('olim','hakimov')
#//anvar narzullayev
#def budilnik_chal():
#     print('soat 6:00  boldi turing')
#budilnik_chal()   

#def rules_day():
#    print('aslo taslim bolmang')
#rules_day()
#def motivation_daily():
#    print('harakatdan toxtamang')
#motivation_daily()    
#def intikam_al(sabrla):
#    print(f"sabr bilan {sabrla.title()}")
#intikam_al('qasos olamiz')
    

#def devoloper_dubai(freelance):
#    print(f"astoydil ishlab {freelance.upper()}")
#devoloper_dubai('freelancer bolamiz in sha allah')    

#def dushman_pro(ism,familiya):
#    print(f"birinchi raqamli dushmanimiz:{ism.title()}\n"
#          f"familiyasi:{familiya.lower()}")
#dushman_pro('anvar','muhitdinov')
#def user_data(ism,familya,yosh):
#    print(f"foydalanuvchining ismi:{ism.title()}\n"
#          f"foydalanuvchining familiyasi:{familya.title()}\n"
#          f"foydalanuvchining yoshi:{yosh.title()}")
    
#user_data('alsher','narzullayev','27 yosh')    
#def user_data(first_name, last_name, age):
#   print("Ism:", first_name)
#   print("Familiya:", last_name)
#   print("Yosh:", age)

#ism = input("Ism: ")
#familiya = input("Familiya: ")
#yosh = input("Yosh: ")
#!!! diqqat qoida
#pythonda funksiyalar 2 ta bo'lakka bo'linadi 1:argument,2:parametr
#agar parametrni belgilab ketilsa ketma-ketlikni ahamiyati yoq masalan:
#user_data(ism, familiya, yosh)
#def yosh_hisobla(ism='abbos',tugilgan_yil=1997):
#    """foydalanuvchining yoshini hisoblovchi dastur"""
#    print(f"{ism.title()} {2025-tugilgan_yil} yoshda ")
    
#yosh_hisobla()
# agar oldindan belgilanmasa ketma-ketlik buzilishi mumkin agar tartibda adashsak
#masalan:
#def     yosh_hisobla(ism,tugilgan_yil):
#    print(f"{ism()} {2025-tugilgan_yil}" )
#yosh_hisobla(1997, 'olim')    
#bundagi kodimiz hato hisoblanadi
#def avto_biography(ism='olim',familiya='hakimov',yosh='25',kasb='kiberxavsizlik'):
#    """foydalanuvchining avtobiografiyasini qaytaruvchi dastur"""
#    print(f"ismi:{ism.title()}\n"
#          f"familyasi:{familiya.title()}\n"
#          f"yoshi:{yosh.title()}\n"
#          f"kasbi:{kasb.title()} mutaxasisi"
#          )
#avto_biography()

#def yosh_hisobla(yosh,joriy_yil=2025):
#    """foydalanuvchining yoshini hisoblovchi funksiya"""
#    print(f"siz {joriy_yil-yosh} yoshdasiz")
#yosh_hisobla(2000)
#amaliyot
#def yosh_hisobla(yosh=' ',ism='akmal',familiya='olimov',joriy_yil=2025):
#    print(f" {ism.title()} {familiya.title()} siz {joriy_yil-yosh}  yoshdasiz")
#yosh_hisobla(1997)    
#def raqam_kvadrat(son):
    #print(f"{son} ning kvadrati {son*son}ga teng\n"
     #     f"{son} ning kubi: {son*son*son} ga teng")
#raqam_kvadrat(5)    
#def juft_toq():
#    son=int(input('bir son kiriting:'))
#    if son %2==0:
#        print('bu juft son')
#    if son %2!=0:
#        print('bu toq son')
#juft_toq()  
#def katta_kichik():
#    son_1=int(input('1-son:'))
#    son_2=int(input('2-son'))
#    if son_1>son_2:
#        print('1-son ikkinchisidan katta')
#    if son_1<son_2:
#        print('ikkinchi son birinchisidan katta')
#    elif son_1==son_2:
#        print('ikkala raqam teng')
#katta_kichik()        
#def daraja(x,y=2):
#    print(f"{x} ning {y}-darajasi {x**y} ga teng")

#daraja(5,2)
#daraja(3,3)
#daraja(94,4)
#daraja(6)


      
#def solishtir(x,y):
#    """Ikki sonni solishtiruvchi funksiya"""
#    if x>y:
#        print(f"{x}>{y}")
#    elif x<y:
#        print(f"{y}>{x}")
#    else:
#        print(f"{x}={y}")

#solishtir(10,20)
#solishtir(-9,12)
#solishtir(5*4,5*4)
    
#def user_data(first_name, last_name, age):
#    print(f"Ism: {first_name}")
#    print(f"Familiya: {last_name}")
#    print(f"Yosh: {age}")
#
#ism = input("Ismingizni kiriting: ")
#familiya = input("Familiyangizni kiriting: ")
#yosh = input("Yoshingizni kiriting: ")

#user_data(ism, familiya, yosh)

#def greet(lang):
#    if lang=='es':
#        print('hola')
#    elif lang=='fr':
#        print('bonjour')
#    else:
#        print('hello')
#greet('en')
#greet('fr')
#greet('es')

#pythonda dasturlash asoslari eng boshdan
#ism='abdulloh'
#yosh='25'
#xabar='hello world'
#print(xabar)
#matn='i 💌 paris'
#print(matn)
#ism='ahad'
#familiya='qayum'
#print(ism+' ' + familiya)
#ism='james'
#familiya='bond'
#print(f" salom mening ismim {familiya}.{ism} {familiya}")
#f stringda matnlarni birlashtiramiz matnlarni bir necha marta takrorlashimiz ham mumkin

#print('salom\tdunyo') bu bizda qator tashlash deyiladi
# input bizda foydalanuvchi bilan muloqot
#ism=input('ismingiz nima ?\n>>>')
#print('Assalomu aleykum',' ' + ism)
#amaliyot
#kocha="bog'bon"
#mahalla="sag'bon"
#tuman="bodomzor"
#viloyat='samarqand'
#kocha=input('kochangizni kiritng:')
#mahalla=input('mahalangizni kiritng:')
#tuman=input('tumaningizni kiritng:')
#viloyat=input('viloyatingizni kiritng:')
#print(kocha + "kochasi\n" +  mahalla  +  "mahallasi,\n "
 #     + tuman  +  "tumani\n"  +  viloyat  +  "viloyati")    
#manzil=f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati" 
#print(manzil.upper())

#kocha=input('kochangiz:')
#mahalla=input('mahallangiz:')
#tuman=input('tumaningiz:')
#viloyat=input('viloyatingiz:')
#print(f"{kocha} kochasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati")
#biz bu yerda oz'garuvchilar yaratib ularni foydalanuvchidan so'rab unga ma'lumotlar jamlab chiqarib berdik
#t_yil=int(input('tugilgan yilingizni kiritng:\n>'))
#yosh=2025-t_yil
#print('siz' +  str(yosh)   +  'yoshda ekansiz')
# amaliyot
#user=int(input('raqam kiriting:'))
#natija=user**2
#print(user,'ning kvadarti',natija, "ga teng")
#user=int(input('yoshingizni kiriting:'))
#yil=2025-user
#print('sizning yilingiz',yil,'yil')
#ozgaruvchilarni birlashishiga yorqin misol
#user=int(input('raqam kiriting:'))
#user_1=int(input('yana raqam:'))
#print(f"{user}+{user_1}=", user+user_1)
#print(f"{user}-{user_1}=", user-user_1)
#print(f"{user}*{user_1}=", user*user_1)
#print(f"{user}//{user_1}=", user//user_1)






#def user_data(first_name,last_name,age):
#    print('ism',first_name)
 #   print("familya",last_name)
  #  print('yosh',age)
#ism=input('ism:')  
#familya=input('familya:')
#yosh=input('yosh:')  
#user_data(ism, familya, yosh)
#ism=input('ismingiz nima:\n>>')
#print('Assalomu aleykum'+ ism.title())
#aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
#print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")
#ism='jobir'
#yosh=25
#message=ism +''+str(yosh)+'yoshda'
#print(type(yosh))
#t_yil=int(input('tugilgan yilingizni kiriting:'))
#yosh=2025-t_yil
#print('siz' + str (yosh) +  'yoshdasiz')#
#t_yil=input('yilingizni kiriting:')
#t_yil=int(t_yil)
#yosh=2025-t_yil
#print('siz'+str(yosh)+'yoshdasiz')

#amaliyot:
#1    
#kvadrat=input('istalgan raqam kiriting:')
#kvadrat=int(kvadrat)
#natija=kvadrat*kvadrat
#print(str(kvadrat)+'ning' + 'kvadrati '  + str(natija))
#2
#yosh=int(input('yoshingiz nechida:>'))
#natija=2025-yosh
#print('siz'+ str(natija)+'yilsiz')
#3
#a=int(input('1-sonni kiriting>'))
#b=int(input('2-sonni kiriting>'))
#print(f"{a}+{b}=",a+b)
#print(f"{a}-{b}=",a-b)
#print(f"{a}*{b}",a*b)
#print(f"{a}//{b}=",a//b)
#bu bizda sonlar va stringlar edi

#listlar ro'yxat
#mevalar=['olma','nok','anor']
#print('birinchi meva bu:' + mevalar[0] )
#print('ikkinchi meva bu:' + mevalar[2])
#cars=['maybach','mercedez','bmw','toyota']
#print('oxirgi model bu:' + cars[-1])
 #qiymatlarni bir-biriga qo'shish
 #masalan:
#narxlar=[12000,16000,18000,22000,25000]
#print(narxlar[1] + narxlar[2])
#agar
#narxlar=['12000,''16000,''18000'] yozilsa natija error boladi
#chunki raqamlar qo'shtirnoq ichida yozilmaydi
#pythonda listning eng oxirgi elementi -1 deb olinadi
#masalan:
#car_models=['nexia','cobalt','malibu','trecker','byd']
#print('eng yoqqan model bu\n>>>'+car_models[-1]) 
   
#message=['nexia','damas','byd','tracker']
#print("mening togam yaqinda yangi " + message[-1] + 'ni sotib  '  + 'yangi 🚊 sotib oldi' )
#endi esa elementlarni o'zgartirib koramiz
#misol uchun:
#car_models=['nexia','cobalt','malibu','trecker','byd']    
#car_models [0]='captiva'
#car_models[1]='gentra'
#car_models[3]='spark'    
#shu xolatda biz yangi elment ham qo'shishimiz mumkin
#masalan:
#kitoblar=['jinoyat va jazo','urush va tinchlik','ikki eshik orasi']
#kitoblar.append("o'tkan kunlar") 
#print(kitoblar)   
# biz yana bo'sh royxatni ham shu uslubda to'ldirib borishimiz mumkin
#misol:
#phones=[]
#phones.append('iphone')
#phones.append('galaxy')
#phones.append('go-2024')
#phones.append('readmi')
#print(phones)    
# keyingi element esa bizda insert
#cars=['lacetti','kaptiva','malibu']
#cars.insert(0, 'toyota')
#print(cars)
#insert elementini ishlatish uchun avval insert,so'ng element tartib raqami qoyiladi

#delete biz buni elementlarni o'chirish uchun ishlatamiz

#mevalar=['anjir','anor','olma','nok']
#del(mevalar[0])
#print(mevalar)#korganingizdek bizda anjir==0 element o'chirildi
#unutmang elementlarni o'chirishda avval del songra element va list nomi kiritiladi

# remove bu ikki bir xil element berilganda bittasini o'chiradi
#masalan:
#hayvonlar=['mushuk','quyon','it','mu-shuk']  
#hayvonlar.remove('mushuk')
#print(hayvonlar)  
#bizda birinchi element mushuk o'chirib ikkinchisi qoldiriladi

#agar biz bir elementni sugurib olishni xoxlasak ochirmasdan buning uchun
#.pop bor
#bozorlik=['un','yog','kepak','non']
#mahsulot=bozorlik.pop(3)
#print(' men  ' +mahsulot+' sotib oldim')
#print('olinmagan maxsulotlar',bozorlik)
#eslatma:agar pop elementiga index berilmasa u oxirgi elementni sug'urib oladi

#mashina=['cobalt','spark',' matiz ']
#buy=mashina.pop()
#print('men' + buy + 'sotib olmoqchiman')
#ismlar=[' amir ',' muso ',' abdulhamid ',' choyxona ']
#cons_1=ismlar[3]
#cons_2=ismlar[2]

#message=ismlar.pop(0)
#print('salom' + message +'bugun' +cons_1 + 'bormi' + cons_2 +'boramizmi' ) 
#endi esa amaliyot
#dostlar=[' obit ',' sobit ',' jobir ',' abbos ']
#print('salom'+dostlar[0] + 'ishlar qalay'+dostlar[2]+' yaxshimi ')
#print('bilasanmi menga'+dostlar[-1]+ ' yoqmayabdi ')
#endi amaliyot
#sonlar=[1,5,10,15,-5,-3,100]
#sonlar.insert(0, -3,)
#sonlar.insert(5, 1)
#amalioyot
#print(sonlar)
#t_shaxslar=[' imom buxoriy ',' beruniy ',' Amir-temur ']
#z_shaxslar=[' Edvard snowden ',' Mr-robot ',' pavel-Durov ']
#favori=t_shaxslar.pop(1)
#favori_1=z_shaxslar.pop(0)
#print('men tarixiy shaxslardan' + favori +'zamonaviy shaxslardan esa'
#      + favori_1 + 'ni yaxshi koraman ')
#friends=['ali','vali','jabbor','sobir']
#friends.remove('sobir')
#friends.append('abbos')
#friends.append('nuriddin')
#friends.insert(1, 'shoxrux')
#friends.insert(3, 'olim')
#mexmonlar=[]
#friends.pop(0)
#friends.pop(1)
#friends.pop(2)
#friends.pop(3)
#friends.append(mexmonlar)
#print(friends)
#qizlar=['shaxzoda','malika','nasiba','diyora']
#qizlar.sort()//bu element bizda alifbo ketma-ketlikda tartiblaydi
#print(qizlar)#agar katta harflar bolsa osh katta harflilarni boshiga oladi
#xuddi shu holatda ro'yxatni teskari tartiblashimiz ham mumkin
#cars=['audi','bmw','daewo','evo','ferrari']
#cars.sort(reverse=True)
#print(cars)
#natijamiz teskari formatda bo'ldi
#ketma-ketlikni buzmay turib ham tartibga solishimiz mumkin
#son=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#son.sort()
#print(son)
#print(sorted(son,reverse=True))
#bazida bizdan ro'yxatni oxirini boshiga,boshini esa oxiriga aylantirish talab qilinadi

#fruits=['apple','banna','lemon','peach']
#fruits.reverse()
#print(fruits)
 #elementlar sonini,yoki uzunligini bilsh
#fruits=['apple','banana','peach']
#print('elementlar soni' , len(fruits))

#range funksiyasi

#sonlar=list(range(0,10))
#print(sonlar)
#Amaliyot bosh royxatga boshqa royxatni qoshish
#friends=['bobur','jobir','abbos']
#vrags=[]
#vrags=friends.pop(2),friends.pop(1),friends.pop(0)

#print(vrags)
#print(friends)

#ro'yxatni  uzunligini bilish
#fruits=['anor','olma','nok']
#natija=len(fruits) 
#print('mevalar soni', natija)
 
#xuddi shu korinishda biz 0dan 15 gacha bolgan raqamlarni qabul qila olamiz
#sonlar=list(range(0,16))
#print(sonlar)

#bunda esa ularni qaysi ketma-ketlikda olishni xoxlasak shunday olamiz
#sonlar=list(range(0,110,20))#bunda raqamlar 10talab sanaladi/10,20,30,...100
#print(sonlar)
#yana bir yorqin misol:
#toq_sonlar=list(range(1,100,2))//bu yerda 2talab:1,3,5,7,9...99
#juft_sonlar=list(range(2,102,2))//bu yerda 2dan boshlab ikkitalab:2,4,6,...100   
#print(juft_sonlar) 
#endi esa raqamlar ustida amallar
#narxlar=[12000,22000,38000,456000,586000]//bu bizda narxlar
#arzon=min(narxlar)//bu eng pasini oladi
#qimmat=max(narxlar)//bu eng balandini
#jami=sum(narxlar)//bu esa butun narxlarni bir-biriga qo'shadi


#print('eng arzon narx:',arzon,'eng qimmat narx:',qimmat,'jami:',jami)

#endi elementlarni kesishni o'rganamiz
#cars=['byd','bmw','lada','mercedes-benz']
#my_cars=cars[0:3]//natija:byd,bmw,lada boladi 3-elementda toxtaydi
#print(my_cars)
#royxatdan nusxa olish
#sonlar=[1,2,3,4,5]
#sonlar2=sonlar[:]
#sonlar2.append(6)
#sonlar2.append(7)
#print('bu bizda \n>> sonlar',sonlar,'bu esa sonlar2:',sonlar2)

#tupl royxat nima?agar biz [] orniga,() ishlatsak bu o'zgarmas royxat ya'ni tupl
#masalan:
#toys=('dragon','snake','monkey','rabbit')
#toys[0]='moon'
#print(toys)
#natija:TypeError: 'tuple' object does not support item assignment    
  
#xosh buni qanday ozgartiramiz? keling urinib ko'ramiz:
    #biz nima qilamiz
#toys=('bus','cherry','kamaz','damas')//tupl ochamiz
#toys=list(toys)//uni listga aylantiramiz
#toys.remove('damas')//damasni u yerdan o'chirib'
#toys.append('dragon')//oxiriga dragon qo'yamiz'
#toys[1]='jeep'//1 element('cherry')ni esas jeepga almashtiramiz 
#print(toys)//natija [bus,jeep,kamaz,dragon bo'ladi']    
#amaliyot
#countrys=['Amaerica','Russia','French','Spain','China!!!']
#print('davlatlar soni:', len(countrys),'ga teng')
#print(sorted(countrys))
#print(sorted(countrys, reverse=True))
#countrys.reverse()
#print(countrys)

#juft_sonlar=list(range(120,1200,2))
#katta=max(juft_sonlar)
#kichik=min(juft_sonlar)
#natija=sum(juft_sonlar)
#print(katta-kichik)
#print(juft_sonlar[:20])
#print(juft_sonlar[-20:])

#taomlar=['osh','shashlik','somsa']
#nonushta=taomlar[:]
#nonushta.remove('osh')
#nonushta.remove('shashlik')
#nonushta.remove('somsa')
#nonushta.append('Non')
#nonushta.append('Qaymog')
#nonushta=tuple(nonushta)
#nonushta[0]='qaymog'
#print(nonushta)
#print(taomlar)


#for operatori
#mexmonlar=['Ali','vali','hasan','husan']
#for mexmon in mexmonlar:
#    print(mexmonlar)
#qasoslar=['anvar','muzaffar','abbos']
#for qasos in qasoslar:
#    print(f"{qasos} ni  hayotdan to'ydirilsin")
#    print('emir golgeden geldi')//bu esa har qasosdan so'ng qaytariladi
#qasoslar=['muzaffar','anvar','abbos']
#for qasos in qasoslar:
    
 #print(f"{qasos} dan o'ch olinib eng ayxshi ko'rgani olinsin")
#print('emir golgeden geldi\n')/bu siklni oxirida bir marta aylanadi chunki u sikldan tashqarida
#endi raqamlar ustida amallar
#sonlar=list(range(1,11))
#for son in sonlar:
    #print(f"{son} ning kvadrati {son**2} ga teng")
#bu yerda natija 1-10gacha sonlar kvadrati print qilinadi    
 

#yangi royxat shakllantirish
#sonlar=list(range(1,11))
#sonlar_kvadrati=[]
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
#    print(sonlar)
#    print(sonlar_kvadrati)
#amaliyot
#dosyalar=[]
#print('en gizli bes dosya')
#for d in range(5):
#    dosyalar.append(input(f"{d+1}-dosya"))
#    print(dosyalar)
#ismlar=['abbos','akmal','sardor','bosit','anvar']
#for ism in ismlar:
#    print(f"salom {ism} qalaysan")
#print('kod',len(ismlar),'marta takrorlanadi')
#toq_sonlar=list(range(11,101,2))
#for son in toq_sonlar:
   # print(son**3)
#qasoslar=['anvar','muzaffar','barno']
#for qasos in qasoslar:
#    print(f"{qasos} ni yo'q qilinsin  va hayoyi bilan o'ynalsin")  
#print('emir golgeden geldi')    
    
#if else matnlarni solishtirish
#ism=input('ismingiz nima?\n>>>')
#if ism.lower()!='ali':
# print('kechirasiz',ism,'biz alini kutyapmiz')
#else:
#    print('hos geldin ali')

#login uzunligini tekshirish
#login=input('login kiriting\n>>>')
#if len(login)<=5:
#    print('login 5ta harfdan katta bolishi kerak')
#else:
#    print('xush kelibsiz')       
    
    
#yil=int(input('yilingzini kiriting>>'))
#if 2025-yil<=18:
#    print('kechirasiz kira olmaysiz')
#else:
   # print('xush kelibsiz')    
    
    


#cars=['toyota','mazda','hyundai','gm','kia']
#for car in cars:
#    if car!='gm':
#        print(car.title())
#    else:
#        print(car.upper())
#ism=input('login kiriting>')
#if ism=='admin':
#  print('xush kelibsiz foydalanuvchi royxatini korasizmi')   
#else:
 #   print(f"xush kelibsiz {ism}")
    
    
#user=int(input('raqam kiriting>'))
#user_1=int(input('raqam kiriting'))
#if user==user_1:
#    print(f"{ism.title()} raqamlar ozaro teng ")
#else:
#    print('bilmadim')    
#manfiy=int(input('raqam kiriting')) 
#if manfiy>=0:
 #   print('bu musbat son')
#else:
#    print('bu manfiy raqam')    
#>>>

    
       