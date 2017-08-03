
class BowlStack():
    dog_picture = '''
   ^___^
   (o o)\_______
    \_/\       )\__/
        ||-----||
        ||     ||      '''

    human_picture = '''
    /\/\/\ 
   |      | 
   | (o)(o) 
   C      _)
    | ,___| 
    |   /   
'''

    def __init__(self):
        self.top_bowl = None 
        self.eaten_bowl_counter = 0 
        self.player = "human"

    def __repr__(self):
        if (self.player == "dog"):
            text = BowlStack.dog_picture
        else:
            text = BowlStack.human_picture
        current_bowl = self.top_bowl
        while (current_bowl != None):
            text += str(current_bowl)
            current_bowl = current_bowl.next 
    
        if (self.player == "dog"):
            text += "\n" + str(self.eaten_bowl_counter) + " bowls of food eaten so far\n"
        return text

    def add_bowl(self,new_bowl):
        new_bowl.next = self.top_bowl
        self.top_bowl = new_bowl  
    
    def remove_bowl(self):
        if(self.top_bowl==None):
            print("\nError: bowl stack is empty")
            return

        if(self.top_bowl.is_full):
            print("\nError: can't remove full bowl! Eat the food first")
            return

        self.top_bowl = self.top_bowl.next

    def eat_food(self):
        if(not self.top_bowl.is_full):
            print("\nError: top bowl is empty!")
            return
        self.top_bowl.is_full = False
        self.eaten_bowl_counter +=1

    def get_full_bowl_count(self):
        current_bowl = self.top_bowl
        cnt = 0
        while (current_bowl != None):
            if (current_bowl.is_full):
                cnt += 1
            current_bowl = current_bowl.next
        return cnt 

class Bowl():
    empty_picture = ''' 
\     /
 -----'''
    full_picture = ''' 
\ *** /
 -----'''

    def __init__(self, empty_or_full):
        if(empty_or_full=="empty"):
            self.is_full = False
        elif(empty_or_full=="full"):
            self.is_full = True

        self.next = None

    def __repr__(self):
        if(self.is_full):
            return(Bowl.full_picture)
        else:
            return(Bowl.empty_picture)

# Main program
if (__name__ == "__main__"):
    game_over = False
    print("Hi human, let's feed your dog")
    myBowlStack = BowlStack()
    print(myBowlStack)

    while (not game_over):
        if (myBowlStack.player == "human"):
            # Human plays
            action = str(input("\nSelect one of the choices:\n1 - add bowl with food\n2 - add empty bowl\n3 - let the dog eat\n"))
            if (action == "1"):
                myBowlStack.add_bowl(Bowl("full"))                
            elif (action == "2"):
                myBowlStack.add_bowl(Bowl("empty"))
            elif (action == "3"):
                if (myBowlStack.get_full_bowl_count() == 0):
                    print("Error: please add some food first!")
                else:
                    myBowlStack.player = "dog"
                    print("\n\nHi dog!")
            else:
                print("Incorrect input!")
        else:
            # Dog plays
            action = str(input("Select one of the choices:\n1 - eat food\n2 - remove top bowl\n3 - ask your master for more food\n"))  
            if (action == "1"):
                myBowlStack.eat_food()
            elif(action == "2"):
                myBowlStack.remove_bowl()
            elif(action == "3"):
                print("Woof! Woof! [translation: human - give me more food]")
                myBowlStack.player = "human"
            else:
                print("Incorrect input!")
            if (myBowlStack.top_bowl == None):
                game_over = True
        print(myBowlStack)
        

    print("Nice job! Now let's go for a walk")