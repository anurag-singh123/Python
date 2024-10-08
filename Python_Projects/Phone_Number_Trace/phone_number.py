import phonenumbers
from phonenumbers import timezone, geocoder, carrier

PhNumber = input("Enter the phone number with Country code(+__):")
PhoneNumber = phonenumbers.parse(PhNumber)
TimeZone = timezone.time_zones_for_number(PhoneNumber)
Carrier = carrier.name_for_number(PhoneNumber, 'en')
Region = geocoder.description_for_number(PhoneNumber, 'en')

print(PhoneNumber)
print(TimeZone)
print(Carrier)
print(Region)
