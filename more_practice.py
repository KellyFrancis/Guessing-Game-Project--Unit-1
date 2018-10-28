import random

def start_game():

    def welcome():
        print("Welcome to my Numbers Guessing Game!  Enter a number between 1 and 20 to start the game. Thanks for playing.")

    welcome()
    empty_list = []
    
    
    
    
    
    
     
        
        
    def number_generator():
        
        random_number = random.randint(1,20)
        
            
        def guess_loop():
            guess = 0

            guess_number = 0
    
            def add_to_list(item):
                empty_list.append(item)
        
            while True:
                try:
                    x = int(input("Enter Number: "))
                
                    
                
            
                except ValueError:
                    print("Oops. Please enter an INTEGER between 1 and 20.")
                    continue
                
                
            
                while guess != random_number:
                
                    guess = x
            
                    guess_number += 1    
            
                    if guess > 0:
                        if guess > 20:
                            print("Number ouside of the range. Enter a number between 1 and 20.")
                            break
                        elif guess > random_number:
                            print("Number to large. Please try again.")
                            break
            
                        elif guess < random_number:
                            print("Number too small. Please try again.")
                            break
                        
            
                    else:
                        print("Number ouside of the range. Enter a number between 1 and 20.")
                        break
                        
                else: 
                
                
                    print("Congratulations! You guessed the correct number! It took you", guess_number, "number of tries.")
                    break
                
                
        
            add_to_list(guess_number)
            
            print("Your best score to beat is", + min(empty_list))
        
        
        
            

            
            def play_again():
                
                answer = input("""Would you like to play again? If yes, enter 'YES'. If no, enter 'NO'.
""")
                
            
                while answer != "NO":
                    
                    if answer == "YES":
                        
                        number_generator()
            
                    else:
                        print("Oops. Please type 'YES' or 'NO', exactly.")
                        play_again()
                        
                else:
                    
                    print("Game Over. Thank you for playing.")
                    exit()
    
                while answer != "YES":
            
                    if answer == "NO":    
                
                        print("Game Over. Thanks you for playing.")
                        exit()
        
                    else:
                        print("Oops. Please type 'YES' or 'NO', exactly.")
                        play_again()
            
                else:
                    
                    number_generator()
                
                    
                    
                
            
            play_again()    
                        
        
        guess_loop()        
        
    number_generator()    
           
    
        
              
        
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()