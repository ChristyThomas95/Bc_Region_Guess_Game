import turtle
import pandas


#Creating the Screen and importing the image
screen = turtle.Screen()
screen.title("Bc Region Guess Game")
image = "Map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("six_region.csv")
all_regions = data.region.to_list()
guessed_regions = []

while len(guessed_regions) < 6:
    answer_region = screen.textinput(title=f"{len(guessed_regions)}/ Six Regions Correct",
                                     prompt="what's another region's name ?")
    if answer_region == "Exit":
        missing_regions = []
        for region in all_regions:
            if region not in guessed_regions:
                missing_regions.append(region)
        new_data = pandas.DataFrame(missing_regions)
        new_data.to_csv("region_to_learn.csv")
        break

    if answer_region in all_regions:
        guessed_regions.append(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        region_data = data[data.region == answer_region]
        t.goto(int(region_data.x), int(region_data.y))
        t.write(answer_region)


