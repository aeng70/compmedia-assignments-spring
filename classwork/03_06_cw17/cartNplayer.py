#PART ONE:

#CODE ALONG: Fill in the constructor method for the Cart class. The template should 
#have an email (as a parameter), a total that is defaulted to 0, and a defaulted 
#empty list that is titled itemList.

class Cart:
  def __init__(self, email):
      self.email = email
      self.total = 0
      self.itemList= []
      
  def updateEmail(newEmail):
      self.email = newEmail

#Uncomment the indicated lines of code below to see if you can create the 
#Cart class in order to have all the appropriate funcitonalities.

#1. You can create a new cart with the user's email. If this code runs without error,
#you've done it. 
testCart = Cart("qrtny@csuniversity.org")



#2. You can access the user's email. If this code runs without error, you've done it.
print(testCart.email)



#3. You can access the total, and it starts off at zero for every new cart:
print(testCart.total)



#CODE ALONG: Create a method called updateEmail to this class that takes in a new 
#email address and sets that as the user's email.
    


#You can check that your updateEmail method works by uncommenting the next lines.
testCart.updateEmail("courtney@csuniversity.org")
print(testCart.email)


#YOUR TASK:
#1. Create a method called addItems to this class that takes in an item name and a 
#price. It should push the item name to the itemList and add the price to the cart 
#total.



#2. You can check that your addItems method works by uncommenting the next line.
#testCart.addItems("Bat Brownie", 2.99)



#3. After adding the item, check that your total has gone up by printing it to the 
#console.




#5. After adding the item, check to make sure your new item is in your list of 
#itemList by printing it to the console.



#6. Create a method called totalGiftCard() that takes in a gift card total as an 
#argument and returns the cart total after a gift card has been deducted.




#7. You can check that your totalGiftCard() method works by uncommenting the next 
#line.
#print(testCart.totalGiftCard(2.82))


#PART TWO:
#Imagine we are making a video game - what specifically that game is or does isn't 
#important, but let's build a class for a Player with some special functions!

#8. Create a Player class that takes in a name as a parameter and has a property 
#called lives with a default value as 3, as well as a property called score with 
#a default value of 0.

# class Player:
#   def __init__():


#9. Test your Player class by uncommenting and running the code below:
#player1 = new Player("José")
#print(player1)


#10. Create a method call gainLife that takes in a number of lives and will add those lives to the total number of lives and print the total to the console. Test that your method works below:
#player1.gainLife(2)
#print(player1.lives)


#11. Create a method called loseLife that will take a life away and return the new amount of lives. If the total lives reaches 0, return YOU LOSE. Print to the console to test!
#player1.loseLife()
#print(player1.lives)


#12. Create a method called addPoints that takes in a number of points and will add those points to the score and return the total. If the score is higher than 100, it should return score points and YOU WIN.
#player1.addPoints(120)


####PART THREE:
#####SPICY BONUS OPTION!#####

#CHALLENGE 1: Add a property to your Player class called powerUps that has a 
#default start value of an empty list. 

#Create a method called gainPowerUp that will add a powerup to the powerUps list. 
#The method should take in the powerup you are adding as a string and then push it 
#to the list (call the powerups whatever you want)

#CHALLENGE 2: In the Cart class, addItems() method accepts an optional third 
#argument for quantity. For example, to buy three bananas for $0.50 each, you 
#could use the following code (if no value is given for the third number, 
#the system should assume you're just buying one):
#testCart.addItems("banana", 0.50, 3)




#After adding the set of three items, you can see that your total has gone up three times!
#print(testCart.total)




#CHALLENGE 3: After adding the set of three items to your Cart, you can see that all the items are there. This line of code should show "Bat Brownie, banana, banana, banana" since we added 1 cookie and three bananas to our cart. If it does not, adjust your method so that it does.
#print(testCart.itemList)