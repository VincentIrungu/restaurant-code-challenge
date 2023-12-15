from models import Restaurant, Customer, Review,session

"""data = [{
  "id": 1,
  "name": "Alain Giannoni",
  "price": 94
}, {
  "id": 2,
  "name": "Cordy Hriinchenko",
  "price": 4
}, {
  "id": 3,
  "name": "Ailene Duguid",
  "price": 59
}, {
  "id": 4,
  "name": "Deonne Dabes",
  "price": 24
}, {
  "id": 5,
  "name": "Muffin Bogies",
  "price": 89
}, {
  "id": 6,
  "name": "Koralle Havelin",
  "price": 100
}, {
  "id": 7,
  "name": "Berti Kezor",
  "price": 82
}, {
  "id": 8,
  "name": "Gabriellia Langland",
  "price": 65
}, {
  "id": 9,
  "name": "Kelli Britch",
  "price": 36
}]

restaurants = []

for datum in data:
    brst =Restaurant(**datum)
    restaurants.append(brst)


session.add_all(restaurants)
session.commit()
print("Good work Vincent restaurant's data seeded succesfully. Check your table")
"""

data = [{
  "id": 1,
  "first_name": "Dierdre",
  "last_name": "Gladyer"
}, {
  "id": 2,
  "first_name": "Frederick",
  "last_name": "Newitt"
}, {
  "id": 3,
  "first_name": "Martita",
  "last_name": "Fullerd"
}, {
  "id": 4,
  "first_name": "Nady",
  "last_name": "Key"
}, {
  "id": 5,
  "first_name": "Darin",
  "last_name": "Pieroni"
}, {
  "id": 6,
  "first_name": "Agustin",
  "last_name": "Cassell"
}, {
  "id": 7,
  "first_name": "Juanita",
  "last_name": "Fargie"
}, {
  "id": 8,
  "first_name": "Ronny",
  "last_name": "Crawford"
}, {
  "id": 9,
  "first_name": "Ursola",
  "last_name": "Dykas"
}]

customers = []

for datum in data:
    brst=Customer(**datum)
    customers.append(brst)

session.add_all(customers)
session.commit()
print("Good work Vincent customer's data seeded succesfully. Check your table")





