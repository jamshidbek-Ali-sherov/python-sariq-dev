import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+998943851620")
phone_number2 = phonenumbers.parse("+79200323738")
phone_number3 = phonenumbers.parse("+998942061620")
phone_number4 = phonenumbers.parse("+998994426405")
print("\nphone Numbers location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))
#location searcher#
