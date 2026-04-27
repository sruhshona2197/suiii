class TaxiRide:
    def __init__(self, distance, price_per_km):
        self.distance = distance
        self.price_per_km = price_per_km

    def calculate_fare(self):
        fare = self.distance * self.price_per_km
        print(f"Yo‘l narxi: {fare} so'm")
        return fare

    def apply_discount(self, percent):
        fare = self.calculate_fare()
        discounted = fare * (1 - percent / 100)
        print(f"Chegirmadan keyin: {int(discounted)} so'm")
