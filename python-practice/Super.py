class Brand:
    def __init__(self, model , year ,cost):
        self.model = model
        self.year = year
        self.cost = cost

    def getData(self):
        print(f"Model : {self.model}")

# obj = Brand("Samsung Galaxy" , 2022, 75000)
# obj.getData()

class Features(Brand):
    def __init__(self , processor , ram, storage) -> None:
        super().__init__("Samsung Ultra Edge S22" , 2022 ,150000)
        self.processor = processor
        self.ram = ram
        self.storage = storage
    
    def display_data(self):
        print(self.processor)
        print(self.ram)
        print(self.storage)

features = Features("Snapdragon-54cu" ,"8Gb", "64Gb")
features.display_data()
features.getData()
print(features.processor)