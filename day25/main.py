import csv
import  pandas
data=pandas.read_csv("./day25/central_park.csv")

grey_count=len(data[data["Primary Fur Color"]=="Grey"])
black_count=len(data[data["Primary Fur Color"]=="Black"])
cinnamon_count=len(data[data["Primary Fur Color"]=="Cinnamon"])


data_dict={
    "Fur Color":["Gray","Black","Cinanamon"],
    "count":[grey_count,black_count,cinnamon_count]
}
df=pandas.DataFrame(data_dict)
df.to_csv("./day25/colors.csv")

        
        

    