import pandas as pd

myData = {
    'Cars' : ["BMW", "Porsche", "McLaren", "Pagani", "Lamborghini", "Mercedes", "Toyota", "Kia"],
    'Top Speed' : [250, 260, 375, 375, 350, 300, 300, 225],
    'Price' : ['600,000', '500,000', '1.5M', '1.75M', '1M', '600,000', '25,000', '30,000']
}

myDataFrame = pd.DataFrame(myData)

print(myDataFrame)
print()
print(myDataFrame.head(2))
print()
print(myDataFrame.tail(2))
print()
print(myDataFrame.loc[2])