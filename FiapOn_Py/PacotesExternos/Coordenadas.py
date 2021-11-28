from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="olinfor") # Nome do seu aplicativo
location = geolocator.geocode("Caminho dos Cavaleiros III")
print(location.address)
print((location.latitude, location.longitude))