
from tkinter import *
import random

questions = []
cities = []
score = ()
question_number = ()
user_answer = ()


class Home:
    def __init__(self, root):
        background_colour = "light blue"
        self.home_frame = Frame(width=700, height=700, bg=background_colour)
        self.home_frame.pack(side="top", fill="both", expand=True)
        # Code for filling frame
        # Logo
        self.logo = Label(self.home_frame,
                          bg=background_colour,
                          text="*LOGO*",
                          # image = photo,
                          font="Arial 28 bold")
        self.logo.pack()
        # Title
        self.title = Label(self.home_frame,
                           bg=background_colour,
                           text="The City Quiz",
                           font="Impact 50 bold")
        self.title.pack(pady=(100, 5))
        # Start Button
        self.start_button = Button(self.home_frame,
                                   bg="green",
                                   fg="white",
                                   text="START",
                                   width=50,
                                   font="Arial 20 bold",
                                   command=self.start_button)
        self.start_button.pack(pady=(200, 10))

    def start_button(self):    # When start Button is pressed
        self.home_frame.destroy()
        start = StartPage(self)


class StartPage:   # Main Menu page
    def __init__(self, root):
        background_colour = "Light Blue"
        self.start_page = Frame(bg=background_colour)
        self.start_page.pack(side="top", fill="both", expand=True)
        # Title
        self.title = Label(self.start_page,
                           bg="dark blue",
                           fg=background_colour,
                           text="THE CITY QUIZ",
                           font="Impact 40 bold",
                           width=200, height=3)
        self.title.pack(pady=(20, 0))
        self.sub_title = Label(self.start_page,
                               bg="dark blue",
                               fg=background_colour,
                               text="THE ULTIMATE CHALLENGE",
                               font="Impact 25 bold",
                               width=200, height=2)
        self.sub_title.pack(pady=(0, 20))
        # Start Button
        self.start_button = Button(self.start_page,
                                   bg="grey",
                                   fg="white",
                                   text="START",
                                   width=12,
                                   height=1,
                                   font="Arial 18 bold",
                                   pady=5, padx=5,
                                   command=self.start_button)
        self.start_button.pack(pady=10)
        # Help Button
        self.help_button = Button(self.start_page,
                                  bg="grey",
                                  fg="White",
                                  text="HELP",
                                  width=12,
                                  height=1,
                                  font="Arial 18 bold",
                                  command=self.help_button)
        self.help_button.pack(pady=10)
        # Quit Button
        self.quit = Button(self.start_page,
                           bg="grey",
                           fg="white",
                           text="QUIT",
                           width=12,
                           height=1,
                           font="Arial 18 bold",
                           command=self.quit_button)
        self.quit.pack(pady=10)

    def start_button(self):    # when Start is clicked
        self.start_page.destroy()
        start = Username(self)

    def help_button(self):   # When Help is clicked
        self.start_page.destroy()
        help_page = Help(self)

    def quit_button(self):    # When quit is clicked
        root.destroy()


class Help:    # Class that show Intructions
    def __init__(self, root):
        background_colour = "orange"
        # Frame
        self.help_frame = Frame(bg=background_colour,
                                height=700,
                                width=800)
        self.help_frame.pack(side="top", fill="both", expand=True)
        # Title
        self.title = Label(self.help_frame,
                           text="INSTRUCTIONS",
                           font='Arial 20 bold',
                           bg=background_colour)
        self.title.pack()

        self.instructions = Label(self.help_frame,
                                  text="To Play the city quiz just press start"
                                  "on the menu page"
                                  ", you will be asked to enter a username."
                                  " The username can be"
                                  " anything, as along as it is more than 3 "
                                  "characters and less than 10 characters."
                                  " Once you successfully choose a username,"
                                  " the quiz will begin."
                                  " You have to choose an option which you "
                                  "think is correct."
                                  " Then press next once you have chosen and"
                                  " then the answer will be taken"
                                  " and the result will be displayed."
                                  " Once you have completed answering "
                                  "20 questions, your score will be displayed."
                                  " Good Luck and Enjoy Quizzing!",
                                  font="Arial 25 bold",
                                  fg="black",
                                  wrap=925,
                                  bg=background_colour)
        self.instructions.pack(pady=20)
        # Dismiss Button
        self.dismiss_button = Button(self.help_frame,
                                     text="DISMISS",
                                     font="Arial 18 bold",
                                     bg="red",
                                     fg="white",
                                     command=self.start_page)
        self.dismiss_button.pack()

    def start_page(self):  # When dismiss is cliked
        self.help_frame.destroy()
        start_page = StartPage(self)


class Username:  # Class that takes User's username
    def __init__(self, parent):
        background_colour = "light blue"
        self.name_frame = Frame(width=800, height=800, bg=background_colour)
        self.name_frame.pack(side="top", fill="both", expand=True)

        self.instructions = Label(self.name_frame,
                                  text="PLEASE ENTER A USERNAME",
                                  font="Arial 30 bold",
                                  fg="white",
                                  width=200,
                                  height=3,
                                  bg="dark Blue")
        self.instructions.pack(pady=(50, 10))
        # Entry Box
        self.name_entry_box = Entry(self.name_frame, width=35,
                                    font="Arial 20 bold")
        self.name_entry_box.pack(pady=(40, 5), ipady=20)

        self.information_output = Label(self.name_frame,
                                        text="GOOD LUCK!",
                                        font="Arial 12",
                                        bg=background_colour,
                                        fg="grey")
        self.information_output.pack()
        # Back Button
        self.back_button = Button(self.name_frame,
                                  text="BACK",
                                  font="Arial 20 bold",
                                  bg=background_colour,
                                  justify=CENTER,
                                  width=20,
                                  height=3,
                                  command=self.back_button)
        self.back_button.pack(side=LEFT, pady=15, padx=20)
        # Start Button
        self.go_button = Button(self.name_frame,
                                text="START",
                                font="Arial 20 bold",
                                bg="green",
                                width=40,
                                justify=CENTER,
                                height=3,
                                command=self.start_button)
        self.go_button.pack(side=RIGHT, pady=15, padx=20)

    def back_button(self):
        self.name_frame.destroy()
        start_page = StartPage(self)

    def start_button(self):
        self.user_name = self.name_entry_box.get()    # Gets the name inputed
        if len(self.user_name) < 10 and len(self.user_name) > 2:  # name check
            global current_user
            current_user = self.user_name
            self.name_frame.destroy()
            set_up_quiz = SetUp(self)
        else:
            self.name_entry_box.configure(bg="red")
            self.information_output.configure(text="Your nickname must be over"
                                              " 3 characters or under 10"
                                              " characters")


class SetUp:    # This class imports the questions and answers
    def __init__(self, root):
        self.import_data()
        global score
        score = 0
        global question_number
        question_number = 0
        question = Question(self)

    def import_data(self):    # Imports thw questions and answers
        del questions[0:]
        del cities[0:]
        file = open("level_1", "r")
        n = -1
        for l in file:
            n = n+1
            if n % 2 == 0:
                questions.append(l.strip())
            else:
                cities.append(l.strip())
        file.close()


class Question:    # This is the main Question frame
    def __init__(self, root):
        # Declarations
        option_list = []
        global random_number
        random_number = random.randint(0, (len(questions))-1)
        answer = (cities[random_number])
        for i in range(0, 3):  # This sets up the options
            random_option = random.randint(0, (len(questions))-1)
            if random_option == random_number:
                option_list.append(cities[random_option-2])
            else:
                option_list.append(cities[random_option])
        global answer_number
        answer_number = random.randint(1, 4)
        option_list.insert(answer_number-1, answer)

        # GUI frame
        background_colour = "light blue"
        self.question_frame = Frame(bg=background_colour,
                                    width=700,
                                    height=700)
        self.question_frame.grid()

        # Username row 0 colum 0
        self.username_label = Label(self.question_frame,
                                    text=(current_user),
                                    font="Arial 14",
                                    bg=background_colour,
                                    fg="grey")
        self.username_label.grid(row=0, column=0, sticky=NW)
        # Score row 0 column 2
        self.score_label = Label(self.question_frame,
                                 text=("Score:", score),
                                 font="Arial 14",
                                 bg=background_colour,
                                 fg="grey")
        self.score_label.grid(row=0, column=2, sticky=NW)

        # Question- row 1
        self.question_label = Label(self.question_frame,
                                    text=(questions[random_number] + "?"),
                                    font="Arial 20 bold",
                                    bg=background_colour,
                                    fg="black",
                                    width=50,
                                    height=5,
                                    pady=10)
        self.question_label.grid(row=1, columnspan=2)
        # Information status for users = row 3
        self.information_label = Label(self.question_frame,
                                       text="",    # It's blank at the start
                                       font="Arial 14 bold",
                                       bg=background_colour)
        self.information_label.grid(row=2, columnspan=2, pady=(0, 40))
        # Option A - row 3 column 0
        option_a = (option_list[0])
        self.option_A = Button(self.question_frame,
                               text=(option_a),
                               font="Arial 15",
                               bg="grey",
                               fg="white",
                               width=20,
                               height=3,
                               command=lambda: self.highlight_button(1))
        self.option_A.grid(row=3, column=0)
        # option B - row 3 column 1
        option_b = (option_list[1])
        self.option_B = Button(self.question_frame,
                               text=(option_b),
                               font="Arial 15",
                               bg="grey",
                               fg="white",
                               width=20,
                               height=3,
                               command=lambda: self.highlight_button(2))
        self.option_B.grid(row=3, column=1)
        # option C row 4 column 0
        option_c = (option_list[2])
        self.option_C = Button(self.question_frame,
                               text=(option_c),
                               font="Arial 15",
                               bg="grey",
                               fg="white",
                               width=20,
                               height=3,
                               command=lambda: self.highlight_button(3))
        self.option_C.grid(row=4, column=0, pady=20)
        # option D row 4 column 1
        option_d = (option_list[3])
        self.option_D = Button(self.question_frame,
                               text=(option_d),
                               font="Arial 15",
                               bg="grey",
                               fg="white",
                               width=20,
                               height=3,
                               command=lambda: self.highlight_button(4))
        self.option_D.grid(row=4, column=1, pady=20)
        # Quit Button - row 5 column 0
        self.quit_button = Button(self.question_frame,
                                  text="QUIT",
                                  font="Arial 14 bold",
                                  bg="Dark grey",
                                  fg="black",
                                  width=5,
                                  height=2,
                                  command=self.quit_button)
        self.quit_button.grid(row=5, column=0, sticky=SW, pady=(20, 5), padx=5)
        # Next button - row 5 column 1
        self.next_button = Button(self.question_frame,
                                  text="NEXT",
                                  font="Arial 14 bold",
                                  bg="grey",
                                  fg="white",
                                  height=2,
                                  width=12,
                                  command=(self.next_button))
        self.next_button.grid(row=5, column=1, pady=(20, 5), padx=0,
                              sticky=SE)

    def quit_button(self):
        self.quit_button.configure(state=DISABLED)
        quit_button = QuitWindow(self)
        self.quit_button.configure(state=NORMAL)

    def highlight_button(self, user_choice):
        global user_answer
        background_colour = "grey"
        self.user_choice = user_choice
        if self.user_choice == 1:    # Highlights the user option
            self.option_A.configure(bg="dark blue")
            self.option_B.configure(bg=background_colour)
            self.option_C.configure(bg=background_colour)
            self.option_D.configure(bg=background_colour)
            user_answer = (1)
        elif self.user_choice == 2:
            self.option_B.configure(bg="dark blue")
            self.option_A.configure(bg=background_colour)
            self.option_C.configure(bg=background_colour)
            self.option_D.configure(bg=background_colour)
            user_answer = (2)
        elif self.user_choice == 3:
            self.option_C.configure(bg="dark blue")
            self.option_B.configure(bg=background_colour)
            self.option_A.configure(bg=background_colour)
            self.option_D.configure(bg=background_colour)
            user_answer = (3)
        else:
            self.option_D.configure(bg="dark blue")
            self.option_B.configure(bg=background_colour)
            self.option_C.configure(bg=background_colour)
            self.option_A.configure(bg=background_colour)
            user_answer = (4)

    def next_button(self):    # This function is called for next button
        global user_answer
        if user_answer == answer_number:
            self.information_label.configure(text="Correct Answer!  :)",
                                             fg="green")
            global score
            score = score + 1
            if user_answer == 1:
                self.option_A.configure(bg="green")
            elif user_answer == 2:
                self.option_B.configure(bg="green")
            elif user_answer == 3:
                self.option_C.configure(bg="green")
            else:
                self.option_D.configure(bg="green")
            global question_number
            question_number = question_number + 1
            self.next_button.configure(text="Next Question",
                                       bg="Orange",
                                       fg="white",
                                       command=self.next_question)
            self.option_A.configure(state=DISABLED)  # Disable the options
            self.option_B.configure(state=DISABLED)  # so that the user
            self.option_C.configure(state=DISABLED)  # cannot change the answer
            self.option_D.configure(state=DISABLED)
            user_answer = ()    # set back to default
            del questions[random_number:random_number + 1]
            del cities[random_number:random_number + 1]
            # prevent repetition of questions

        elif user_answer == ():
            self.information_label.configure(text="Please select an option",
                                             fg="red")

        else:    # Shows the correct answer to the user
            self.information_label.configure(text="INCORRECT!  :(", fg="red")
            if user_answer == 1:
                self.option_A.configure(bg="red")
                if answer_number == 1:
                    self.option_A.configure(bg="green")
                elif answer_number == 2:
                    self.option_B.configure(bg="green")
                elif answer_number == 3:
                    self.option_C.configure(bg="green")
                else:
                    self.option_D.configure(bg="green")
            elif user_answer == 2:
                self.option_B.configure(bg="red")
                if answer_number == 1:
                    self.option_A.configure(bg="green")
                elif answer_number == 2:
                    self.option_B.configure(bg="green")
                elif answer_number == 3:
                    self.option_C.configure(bg="green")
                else:
                    self.option_D.configure(bg="green")
            elif user_answer == 3:
                self.option_C.configure(bg="red")
                if answer_number == 1:
                    self.option_A.configure(bg="green")
                elif answer_number == 2:
                    self.option_B.configure(bg="green")
                elif answer_number == 3:
                    self.option_C.configure(bg="green")
                else:
                    self.option_D.configure(bg="green")
            else:
                self.option_D.configure(bg="red")
                if answer_number == 1:
                    self.option_A.configure(bg="green")
                elif answer_number == 2:
                    self.option_B.configure(bg="green")
                elif answer_number == 3:
                    self.option_C.configure(bg="green")
                else:
                    self.option_D.configure(bg="green")

            question_number = question_number + 1
            self.next_button.configure(text="Next Question",
                                       bg="Orange",
                                       fg="White",
                                       command=self.next_question)
            self.option_A.configure(state=DISABLED)
            self.option_B.configure(state=DISABLED)
            self.option_C.configure(state=DISABLED)
            self.option_D.configure(state=DISABLED)
            user_answer = ()    # set to Default
            del questions[random_number:random_number + 1]
            del cities[random_number:random_number + 1]

    def next_question(self):    # After user clicks next again
        if question_number == 20:
            # checks question number
            self.question_frame.destroy()
            display_score = Display_score(root)
        else:
            self.question_frame.destroy()
            question = Question(self)


class QuitWindow:
    def __init__(self, parthner):
        background = "orange"
        self.quit_box = Toplevel()
        self.quit_frame = Frame(self.quit_box, bg=background)
        self.quit_frame.pack()
        # Set up Help heading (row 0)
        self.confirmation_msg = Label(self.quit_frame,
                                      text="Are you Sure  you want to quit?",
                                      font=("Arial", "14", "bold"),
                                      bg=background)
        self.confirmation_msg.pack()
        # Help Text
        self.help_text = Label(self.quit_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.pack()
        # No button
        self.no_button = Button(self.quit_frame, text="No", width=10,
                                bg=background,
                                font=("Arial", "10", "bold"),
                                command=(self.close_help))
        self.no_button.pack(side=LEFT, padx=5)
        # Yes Button
        self.yes_button = Button(self.quit_frame, text="Yes", width=10,
                                 bg=background, font=("Arial", "10", "bold"),
                                 command=(self.quit_game))
        self.yes_button.pack(side=RIGHT, padx=5, pady=2)

    def close_help(self):
        self.quit_box.destroy()

    def quit_game(self):
        self.quit_box.destroy()
        root.destroy()


class Display_score:    # after 20 Questions have been answered
    def __init__(self, root):
        background_colour = "light green"
        self.score_frame = Frame(bg=background_colour)
        self.score_frame.pack(side="top", fill="both", expand=True)

        self.finish_message = Label(self.score_frame,
                                    bg="black",
                                    fg="light green",
                                    text="YOU HAVE COMPLETED THE QUIZ",
                                    width=200,
                                    font="Arial 35 bold")
        self.finish_message.pack(pady=(20, 0))
        # Quiz finish text
        self.finish_message = Label(self.score_frame,
                                    bg="black",
                                    fg=background_colour,
                                    width=200,
                                    text="WELL DONE!",
                                    font="Arial 40 bold")
        self.finish_message.pack()
        # User name Label
        self.user_name = Label(self.score_frame,
                               bg="black",
                               fg=background_colour,
                               width=200,
                               text=("Username: " + current_user),
                               font="Arial 15 bold")
        self.user_name.pack()
        # Score
        self.score = Label(self.score_frame,
                           bg="black",
                           fg=background_colour,
                           width=200,
                           text=("Score:", score, "/20"),
                           font="Arial 15 bold")
        self.score.pack()
        # Calculations
        self.score_percentage = int((score/20)*100)
        # Percentage Display
        self.percentage_display = Label(self.score_frame,
                                        bg=background_colour,
                                        text=(self.score_percentage, "%"),
                                        font="Arial 75 bold")
        self.percentage_display.pack(pady=(70, 0))
        # Congratulation messages
        if self.score_percentage >= 90:
            message = "Outstanding!!!"
        elif self.score_percentage >= 80:
            message = "Excellent!!!"
        elif self.score_percentage >= 70:
            message = "Well done!"
        elif self.score_percentage >= 60:
            message = "Good job!"
        elif self.score_percentage >= 50:
            message = "Not bad, You got half of them!"
        elif self.score_percentage >= 40:
            message = "good try, but you can do much better!"
        elif self.score_percentage >= 30:
            message = "Good try, better luck next time!"
        else:
            message = "Come on you can do better!"
        # Reward messages
        self.reward_message = Label(self.score_frame,
                                    text=message,
                                    font="Arial 16 bold",
                                    bg=background_colour,
                                    fg="dark blue")
        self.reward_message.pack(pady=(5, 0))

        self.mainmenu_button = Button(self.score_frame,
                                      text="Main Menu",
                                      font="Arial 20 bold",
                                      bg="black",
                                      fg="white",
                                      command=self.main_menu)
        self.mainmenu_button.pack(pady=(80, 10),
                                  padx=20,
                                  side=LEFT)
        self.play_again = Button(self.score_frame,
                                 text="Play Again",
                                 font="Arial 20 bold",
                                 bg="black",
                                 fg="white",
                                 command=self.play_again)
        self.play_again.pack(pady=(80, 10),
                             padx=20,
                             side=RIGHT)

    def play_again(self):  # When play again is clicked
        self.score_frame.destroy()
        play_again = SetUp(self)

    def main_menu(self):  # Goes back to main menu
        self.score_frame.destroy()
        main_menu = Home(self)


if __name__ == "__main__":
    root = Tk()
    root.resizable(0, 0)
    root.title("GUESS THE CITY")
    root.geometry("940x580")
    start = Home(root)
    root.mainloop()
