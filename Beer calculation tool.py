print("Hello, I will guide you through making a recipe for your beer")
print("How strong do you want the final beer to be? (enter ABV in percent)")
ABV=input()
print("OK, and how many liters are you brewing? (enter liters)")
volume=input()

OG_minus_FG = float(ABV)/0.132
OG  = int(round(int(OG_minus_FG)/0.7,0))
FG = int(round(int(OG)*0.3,0))
Malt =  round((int(OG)*int(volume))/(300*0.75),2)
print("OK, your grainbill should be "+str(Malt)+"kg. Your OG will be 10"+str(OG)+" and your estimated FG will be 10"+str(FG))
print("Don't forget to add specialty malts and additions to the wort!")
print("How bitter do you want your beer to be? (enter in IBU. A normal lager is around 30 and an IPA around 50)")
IBU=input()
print("OK, and what is the alpha acid content of your bitter hop? (enter in percent. This step assumes you boil for 1h)")
Alpha_acid=input()
hops = round((int(IBU)*int(volume)*10)/(float(Alpha_acid)*30),1)
print("You should add "+str(hops)+"g of your bitter hop for your 1h boil")
Beer_recipe = open("Beer_recipe.txt","w")
L=["You need "+str(Malt)+"kg of malt \n" ,
"This gives you OG 10"+ str(OG)+" and FG 10"+str(FG)+"\n",
"You need "+str(hops)+" grams of hops for your 1h boil \n"]
Beer_recipe.write("Here is your recipe \n")
Beer_recipe.writelines(L)
Beer_recipe.close()
print("Your recipe has been generated as a text-file")