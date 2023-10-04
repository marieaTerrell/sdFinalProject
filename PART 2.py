"""
Author:  mariea terrell
Date written: mm/dd/yy
Assignment: Programm   Module#6 exercise# part# (2), etc.
Short Desc: final project
"""
# Import tkinter GUI toolkit
import tkinter


class mealChoice:
    def __init__(self):
        # main window for selecting a meal
        self.main_window = tkinter.Tk()

        # Create the frames for main window
        self.top_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
        self.bottome_frame = tkinter.Frame(self.main_window)

        # Create the widgets for meal 1
        #text for meal 1
        self.mealOne_label = tkinter.Label(self.top_frame, text="Enter Select Meal One to display the ingredients required and recipe")
        #GUI button for meal 1
        self.mealOne_button = tkinter.Button(self.top_frame, text="Select this Meal", command=self.mealOneWindow) #need to make this command to open a new window
        """
     #All this code is questionable
        
        #Code to open the picture of meal 1 fully prepared
        loadMealtOneImg = Image.open(mealOne.jpg)

        #Code to render image of meal 1
        renderMealOneImg = ImageTk.PhotoImage(loadMealOneImg)
        
        #Code to Label meal 1 picture
        imgMealOne = Label(self, imagae = renderMealOneImg)
        
        #renders image with the picture label
        imgMealOne = renderMealOneImg

        #place the picture in the window at this point (centered for now might need change)
        imageMealTwo.place(x=0, y=0)

        """        

        # Pack the widgets for the meal 1
        self.mealOne_label.pack(side="left")
        self.mealOne_button.pack(side="left")
        #write code to pack imgMealOne in the top frame 
       
        # Create the widgets for meal 2
        #text for meal 1
        self.mealTwo_label = tkinter.Label(self.second_frame, text="Enter Select Meal Two to display the ingredients required and recipe")
        #GUI button for meal 1
        self.mealTwo_button = tkinter.Button(self.second_frame, text="Select this Meal", command=self.mealTwoWindow) #need to make this command to open a new window
        """
    #All this code is questionable
    
        #Code to open the picture of meal 2 fully prepared
        loadMealtTwoImg = Image.open(mealTwo.jpg)

        #Code to render image of meal 2 
        renderMealTwoImg = ImageTk.PhotoImage(loadMealTwoImg)
        
        #Code to Label meal 2 picture
        imgMealTwo = Label(self, imagae = renderMealTwoImg)
        
        #renders image with the picture label
        imgMealTwo = renderMealTwoImg

        #place the picture in the window at this point (centered for now might need change)
        imageMealTwo.place(x=0, y=0)

        """

        # Create the widgets for meal 3
        #text for meal 3
        self.mealThree_label = tkinter.Label(self.third_frame, text="Enter Select Meal Three to display the ingredients required and recipe")
        #GUI button for meal 3
        self.mealThree_button = tkinter.Button(self.third_frame, text="Select this Meal", command=self.mealThreeWindow) #need to make this command to open a new window
        """
    #All this code is questionable

        #Code to open the picture of meal 3 fully prepared
        loadMealtThreeImg = Image.open(mealThree.jpg)

        #Code to render image of meal 3
        renderMealThreeImg = ImageTk.PhotoImage(loadMealThreeImg)
        
        #Code to Label meal 3 picture
        imgMealThree = Label(self, imagae = renderMealThreeImg)
        
        #renders image with the picture label
        imgMealThree = renderMealThreeImg

        #place the picture in the window at this point (centered for now might need change)
        imageMealThree.place(x=0, y=0)

        """        

        # Pack the widgets for the meal 3
        self.mealOne_label.pack(side="left")
        self.mealOne_button.pack(side="left")
        #write code to pack imgMealOne in the top frame 
        # Pack the widgets for the meal 3
        self.mealThree_label.pack(side="left")
        self.mealThree_button.pack(side="left")
        #write code to pack imgMealTwo in the middle frame 


        # Create the widgets for the GUI buttons
        
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the widgets for the GUI buttons
        self.quit_button.pack(side="left")

        # Pack the frames for the main window
        self.top_frame.pack()
        self.second_frame.pack()
        self.third_frame_frame.pack()
        self.bottom_frame.pack()

       
        # Enter the tkinter main loop for the program
        tkinter.mainloop()

class mealOneWindow:
    def __init__(self):
        # window for selecting a meal
        self.mealOne_window = tkinter.Tk()

        # Create the frames for this window
        self.top_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.bottome_frame = tkinter.Frame(self.main_window)

        # Create the widgets for meal 1
        #text for meal 1 ingredients
        self.mealOneIngredients_label = tkinter.Label(self.top_frame, text="Type all the ingredients")#actually add the ingredients for this meal

        # Pack the widgets for the meal 1
        self.mealOneIngredients_label.pack(side="left") 
       
        # Create the widgets for meal 2
        #text for meal 1 recipe/preperation
        self.mealOneRecipe_label = tkinter.Label(self.second_frame, text="Type the recipe here")#actually add the recipe for this meal

        # Create the widgets for the GUI buttons
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.mealOneWindow_window.destroy)

        # Pack the widgets for the GUI buttons
        self.quit_button.pack(side="left")

        # Pack the frames for the main window
        self.top_frame.pack()
        self.second_frame.pack()
        self.bottom_frame.pack()

       
        # Enter the tkinter meal one window for the program
        tkinter.mealOneWindow()


class mealTwoWindow:
    def __init__(self):
        # window for selecting a meal
        self.mealTwo_window = tkinter.Tk()

        # Create the frames for this window
        self.top_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.bottome_frame = tkinter.Frame(self.main_window)

        # Create the widgets for meal 2
        #text for meal 2 ingredients
        self.mealTwoIngredients_label = tkinter.Label(self.top_frame, text="Type all the ingredients")#actually add the ingredients for this meal

        # Pack the widgets for the meal 2
        self.mealTwoIngredients_label.pack(side="left") 
       
        # Create the widgets for meal 2
        #text for meal 2 recipe/preperation
        self.mealTwoRecipe_label = tkinter.Label(self.second_frame, text="Type the recipe here")#actually add the recipe for this meal

        # Create the widgets for the GUI buttons
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.mealTwoWindow_window.destroy)

        # Pack the widgets for the GUI buttons
        self.quit_button.pack(side="left")

        # Pack the frames for the main window
        self.top_frame.pack()
        self.second_frame.pack()
        self.bottom_frame.pack()

       
        # Enter the tkinter meal Two window for the program
        tkinter.mealTwoWindow()


class mealThreeWindow:
    def __init__(self):
        # window for selecting a meal
        self.mealThree_window = tkinter.Tk()

        # Create the frames for this window
        self.top_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.bottome_frame = tkinter.Frame(self.main_window)

        # Create the widgets for meal 3
        #text for meal 2 ingredients
        self.mealThreeIngredients_label = tkinter.Label(self.top_frame, text="Type all the ingredients")#actually add the ingredients for this meal

        # Pack the widgets for the meal 3
        self.mealThreeIngredients_label.pack(side="left") 
       
        # Create the widgets for meal 3
        #text for meal 2 recipe/preperation
        self.mealThreeRecipe_label = tkinter.Label(self.second_frame, text="Type the recipe here")#actually add the recipe for this meal

        # Create the widgets for the GUI buttons
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.mealThreeWindow_window.destroy)

        # Pack the widgets for the GUI buttons
        self.quit_button.pack(side="left")

        # Pack the frames for the main window
        self.top_frame.pack()
        self.second_frame.pack()
        self.bottom_frame.pack()

       
        # Enter the tkinter meal Two window for the program
        tkinter.mealThreeWindow()



# Create an object for mealChoice class
mealChoice_gui = mealChoice()

# Create an object for mealOne class
mealOneWindow_gui = mealOneWindow()

# Create an object for mealOne class
mealTwoWindow_gui = mealTwoWindow()

# Create an object for mealOne class
mealThreeWindow_gui = mealThreeWindow()
