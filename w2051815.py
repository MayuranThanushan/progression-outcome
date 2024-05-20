# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# IIT student ID: 20231047
# UoW student ID: 20518152
# Date: 10-12-2023



#Importing Graphics.py for histogram usage
from graphics import *

# Defining Variables
part_option = 0
view_option = 0
credits_at_pass = 0
credits_at_defer = 0
credits_at_fail = 0
total_count = 0
progress_count = 0
exclude_count = 0
module_trailer_count = 0
module_retriever_count = 0
current_outcome = 0

#Defining Constants (Refered from PEP 8)
EXCLUDE = "Exclude"
PROGRESS = "Progress"
MODULE_TRAILER = "Progress (module trailer)"
MODULE_RETRIEVER = "Module retriever"

progression_data = [] #Defining List



#defining Functions

#View selection menu
def menu_page():
    global part_option, view_option #Defining global variable for continuation
    try: 
        print("Enter 1 for Part 1 - Main version.\nEnter 2 for Part 2 - List (extension).\nEnter 3 for Part 3 - Text file(extension).")
        part_option = int(input ("Enter the Part option: "))
        
        if (part_option == 1): #Proceeding part 1
            print("\nPart option: Part 1 - Main version.\n")
            
            print("Enter 1 for Student version\nEnter 2 for staff version")
            view_option = int(input("Enter the View option: "))
            
            if (view_option == 1): #Proceeding student view
                print("\nView option: Student version\n")
                get_user_credits()
            elif (view_option == 2): #Proceeding staff view
                print("\nView option: Staff version(w/ Histogram)\n")
                get_user_credits()
            else: 
                print("Please enter the correct View option (1 or 2)\n") #Error prompt if wrong value entered
                menu_page()

        elif ( part_option == 2): #Proceeding part 2
            print("\nPart option: Part 2 - List(extension)\n")
            get_user_credits()
            
        elif (part_option == 3): #Proceeding part 3
            print("\nPart option: Part 3 - Text file(extension)\n")
            get_user_credits()
            
        else:
            print("Please enter the correct Part option (1, 2 or 3)\n") #Error prompt if wrong value entered
            menu_page()
            
    except ValueError:
            print("Integer required\n") #Error prompt if input cannot be converted to integer
            menu_page()
            
#To prompt the inputs and validate it
def validate_credits(prompt):

    while True: #To reduce the chance of infinite loop
        try:
            input_credits = int(input(prompt))
            
            if (not 0<= input_credits <=120) or (input_credits % 20 !=0): #Error prompt if wrong value entered
                print("Out of range.\n")
                return None #Signaling that the input is invalid
            else:    
                return input_credits #If no error in the first credit, proceeds to the next credit input prompt
                
        except ValueError:
            print("Integer required.\n") #Error prompt if input cannot be converted to integer
            return None


# To determine the outcome based on credits and returning the value
def determine_outcome(credits_at_pass, credits_at_defer, credits_at_fail):
    
    if credits_at_fail >= 80:
        return EXCLUDE
    elif credits_at_pass == 120:
        return PROGRESS
    elif credits_at_pass == 100:
        return MODULE_TRAILER
    else:
        return MODULE_RETRIEVER



#To check the Inputs and the total are correct                
def get_user_credits():
    global credits_at_pass, credits_at_defer, credits_at_fail, current_outcome #Defining global variable for continuation
    
    while True: #To reduce the chance of infinite loop
        try:
            credits_at_pass = validate_credits("Please enter your total PASS credits: ") #prompt pass credits
            if credits_at_pass is None: 
                continue #If the input was not valid it will call it back
            
            credits_at_defer = validate_credits("Please enter your total DEFER credits: ") #prompt defer credits
            if credits_at_defer is None:
                continue
            
            credits_at_fail = validate_credits("Please enter your total FAIL credits: ") #prompt fail credits
            if credits_at_fail is None:
                continue
            
            total_credits = credits_at_pass + credits_at_defer + credits_at_fail    
            if (total_credits != 120): #Error prompt if total is not 120
                print("Total incorrect.\n")
                continue #If the input was not valid it will call it back
                
            else:
                current_outcome = determine_outcome(credits_at_pass, credits_at_defer, credits_at_fail) #calculates outcome
                print(current_outcome)
                progression_data.append([current_outcome, credits_at_pass, credits_at_defer, credits_at_fail]) #adds the newer values to the list
                calculations()
                break # Break the loop if the input is valid
            
        except ValueError: #Error prompt if input is invalid
            print("Invalid input.\n")
            get_user_credits()

            
            
#Counting the inputs     
def calculations():
    global credits_at_pass, credits_at_fail, total_count, progress_count, exclude_count, module_trailer_count, module_retriever_count
    #Defining global variable for continuation
    
    while True:  # To handle invalid input
        try:
            if credits_at_fail >= 80: #Exclude
                exclude_count += 1
                total_count += 1

            elif credits_at_pass == 120: #Progress
                progress_count += 1
                total_count += 1

            elif credits_at_pass == 100: #Module_trailer
                module_trailer_count += 1
                total_count += 1

            else:
                module_retriever_count += 1 #Module_retriever
                total_count += 1

            break # Break the loop if the input is valid

        except ValueError:
            print("Invalid input.\n")  #Error prompt if input is invalid     
            get_user_credits()
            
    if (view_option == 1): #If it's student view, program exits
        end()
        
    else: 
        print() #Just for code clear
        staff_choice() #else, it loops for multiple outcome
    
        
            
#Prompt the staff to continue or not       
def staff_choice():
    
    while True: #To reduce the chance of infinite loop
        try:
            continue_choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
                
            if (continue_choice.lower() == "y"):
                print() #Just for code clear
                get_user_credits() #Loops it to get multiple outcomes
                break
            
            elif (continue_choice.lower() == "q"): #Ends the loop and proceeds to display results
                print() #Just for code clear
                if (part_option ==1 ) and (view_option == 2): #If it's staff view, program proceeds to display histogram
                    histogram()
                    end()
                    
                elif (part_option == 2): #If it's part 2, program proceeds to display list
                    display_progression_data()
                    end()
                    
                elif (part_option == 3): #If it's part 3, program proceeds to save text file
                    text_file()
                    end()
                    
                break # breaks if input is valid
            
            else:
                print("Invalid input.\n") #Error prompt if input is invalid
                staff_choice()
                
        except ValueError:
            print("Invalid input.\n") #Error prompt if input is invalid
            staff_choice()



#Display progression data from list
def display_progression_data():

    print("Part 2:")
    for data in progression_data: #gets all the data in the list
        print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")



#Save progression data to a text file
def save_text_file():
    
    with open("Progression_data.txt", "w") as file: #Writable text file
        file.write("Part 3:\n")
        for data in progression_data:
            file.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")
            


#Load progression data from a text file
def load_text_file():
    try:
        with open("Progression_data.txt", "r") as file: #Readable text file
            lines = file.readlines() #Reads all the lines from the file
            for line in lines:
                data = line.strip().split(",")#To remove whitespaces which can cause errors when processing data and seperating the data using comma
                print(line, end="") #Prints every line in the program
                
    except (FileNotFoundError or ValueError): #Error prompt if file not found
        print("No saved data found.")
        
        create_new_data = input("Do you want to start with a new set of data? (y/n): ") #Prompt to restart if file not found
        if (create_new_data.lower() == "y"): #returns to main page
            menu_page()
        elif (create_new_data.lower() == "n"): #ends the program
            end()
        else:
            print("Invalid input.\n") #Error prompt if input is invalid
            return create_new_data        
        


#Histogram prompt prameters
def draw_histogram(win, x, y, height, color, label, count):
    
    rectangle = Rectangle(Point(x, y), Point(x + 100, y - height)) #Rectangles for graph
    rectangle.setFill(color)
    rectangle.draw(win)

    label_text = Text(Point(x + 50, y + 20), f"{label}") #Credits label for graph
    label_text.setFace("helvetica")
    label_text.setStyle("bold")
    label_text.draw(win)
    
    count_text = Text(Point(x + 50, (y -20) - height), f"{count}") #Outcome count for graph
    count_text.setFace("helvetica")
    count_text.setSize(16)
    count_text.draw(win)
    
#Histogram using graphics.py
def histogram():
    
    win = GraphWin("Histogram", 650, 500) #Window background
    win.setBackground("Silver")

    title = Text(Point(175,50), "Histogram Results") #Title
    title.setFace("helvetica")
    title.setSize(24)
    title.setStyle("bold")
    title.draw(win)

    #Graph height calculations
    try:
        progress_height = (progress_count/total_count)*150
        trailer_height = (module_trailer_count/total_count)*150
        retriever_height = (module_retriever_count/total_count)*150
        exclude_height = (exclude_count/total_count)*150
        
    except ZeroDivisionError: #Error prompt if total_count equals 0
        print("No saved data found")
        menu_page()
        
    # Drawing histograms
    draw_histogram(win, 50, 350, progress_height, "Turquoise", "Progress", progress_count)
    draw_histogram(win, 200, 350, trailer_height, "Crimson", "Trailer", module_trailer_count)
    draw_histogram(win, 350, 350, retriever_height, "Orange", "Retriever", module_retriever_count)
    draw_histogram(win, 500, 350, exclude_height, "GreenYellow", "Excluded", exclude_count)
    
    #Total outcome display
    total_graph_count = Text(Point(150,420), f"{total_count} outcomes in total.")
    total_graph_count.setStyle("bold")
    total_graph_count.setSize(16)
    total_graph_count.draw(win)

    win.getMouse() #Pause the window until mouse click recieved
    win.close()



#Text file (Extention)
def text_file():
    
    save_text_file()
    load_text_file()
    print("\nText file has been saved")



#end prompts
def end():

    if (part_option == 1):
        print("\nProgram (Part 1) is exiting")
    elif (part_option == 2):
        print("\nProgram (Part 2) is exiting")
    elif (part_option == 3):
        print("\nProgram (Part 3) is exiting")
    else:
        print("\nProgram is exiting")


 
menu_page() #Call the main functions
