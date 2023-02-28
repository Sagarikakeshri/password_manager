from bs4 import BeautifulSoup
import requests



project_name=[]
no_of_rooms=[]
cost=[]


class Scrapping:
    def get_details(self):
        response = requests.get("https://housing.com/rent/search-CgP1gn372jxw0dd6m9nU12ng")
        housing = response.content
        soup = BeautifulSoup(housing, "html.parser")
        rooms =soup.findAll("h2", class_="css-15za28d")
        price=soup.findAll("div",class_="css-132rfk5")
        for room in rooms:
            count=room.getText().split("BHK")
            ert=count[1].split("in")
            no_of_rooms.append(count[0])
            project_name.append(ert[1])
        #print(len(project_name))
        #print(len(no_of_rooms))

        for rent in price:
            cost.append(rent.getText())
        return cost,project_name,no_of_rooms
       # print(len(cost))

