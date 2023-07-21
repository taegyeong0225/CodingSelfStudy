class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} 원 {self.completion_year}년")


house1 = House("강남", "아파트", "매매", "10억", 2010)
house2 = House("마포", "오피스텔", "전제", "5억", 2007)
house3 = House("송파", "빌라", "월세", "500/50", 2000)

print("총 3가지 매물이 있습니다.")
house1.show_detail()
house2.show_detail()
house3.show_detail()
