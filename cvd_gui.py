import tkinter as tk
from cvd_model1 import *

class CVD_GUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Fertility Disease Predictor")

        # Create two frames to group widgets.
        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()
        self.five_frame = tk.Frame()
        self.six_frame = tk.Frame()
        self.seven_frame = tk.Frame()
        self.eight_frame = tk.Frame()
        self.nine_frame = tk.Frame()
        self.ten_frame = tk.Frame()
        self.eleven_frame = tk.Frame()

        # Create the widgets for one frame. (title display)
        self.title_label = tk.Label(self.one_frame, text='Fertility Disease Predictor',fg="Blue", font=("Helvetica", 18))
        self.title_label.pack()

        # Create the widgets for two frame. (season input)
        self.season_label = tk.Label(self.two_frame, text='season:')
        self.click_season_var = tk.StringVar()
        self.click_season_var.set("Winter")
        self.season_inp = tk.OptionMenu(self.two_frame, self.click_season_var, "Winter", "Spring", "Summer", "Fall")
        self.season_label.pack(side='left')
        self.season_inp.pack(side='left')


        # Create the widgets for three frame. (age input)
        self.age_label = tk.Label(self.three_frame, text='Age:')
        self.age_entry = tk.Entry(self.three_frame, bg="white", fg="black", width = 10)
        #self.age_entry.insert(0,'50')
        self.age_label.pack(side='left')
        self.age_entry.pack(side='left')

        # Create the widgets for four frame. (Childish Disease input)
        self.cd_label = tk.Label(self.four_frame, text='Childish Disease :')
        self.click_cd_var = tk.StringVar()
        self.click_cd_var.set("No")
        self.cd_inp = tk.OptionMenu(self.four_frame, self.click_cd_var, "No", "Yes")
        self.cd_label.pack(side='left')
        self.cd_inp.pack(side='left')

        # Create the widgets for five frame. (Accident or Serious Trauma input)
        self.ast_label = tk.Label(self.five_frame, text='Accident or Serious Trauma :')
        self.click_ast_var = tk.StringVar()
        self.click_ast_var.set("No")
        self.ast_inp = tk.OptionMenu(self.five_frame, self.click_ast_var, "No", "Yes")
        self.ast_label.pack(side='left')
        self.ast_inp.pack(side='left')

        # Create the widgets for six frame. (surgical intervention  input)
        self.st_label = tk.Label(self.six_frame, text='surgical intervention :')
        self.click_st_var = tk.StringVar()
        self.click_st_var.set("No")
        self.st_inp = tk.OptionMenu(self.six_frame, self.click_st_var, "No", "Yes")
        self.st_label.pack(side='left')
        self.st_inp.pack(side='left')

        # Create the widgets for seven frame. (High fevers in the last year   input)
        self.hfly_label = tk.Label(self.seven_frame, text='High fevers in the last year:')
        self.click_hfly_var = tk.StringVar()
        self.click_hfly_var.set("less than three months ago")
        self.hfly_inp = tk.OptionMenu(self.seven_frame, self.click_hfly_var,"less than three months ago", "more than three months ago", "no")
        self.hfly_label.pack(side='left')
        self.hfly_inp.pack(side='left')

        # Create the widgets for eight frame. (Frequency of alcohol consumption input)
        self.fac_label = tk.Label(self.eight_frame, text='Frequency of alcohol consumption:')
        self.click_fac_var = tk.StringVar()
        self.click_fac_var.set("several times a day")
        self.fac_inp = tk.OptionMenu(self.eight_frame, self.click_fac_var, "several times a day", "every day", "several times a week", "once a week")
        self.fac_label.pack(side='left')
        self.fac_inp.pack(side='left')

         # Create the widgets for nine frame. (Smoking habit  input)
        self.sh_label = tk.Label(self.nine_frame, text='Smoking habit:')
        self.click_sh_var = tk.StringVar()
        self.click_sh_var.set("never")
        self.sh_inp = tk.OptionMenu(self.nine_frame, self.click_sh_var, "never", "occasional", "daily")
        self.sh_label.pack(side='left')
        self.sh_inp.pack(side='left')

  # Create the widgets for ten frame. (Number of hours spent sitting per day input)
        self.hssspd_label = tk.Label(self.ten_frame, text='Number of hours spent sitting per day:')
        self.hssspd_entry = tk.Entry(self.ten_frame, bg="white", fg="black", width = 10)
        #self.age_entry.insert(0,'50')
        self.hssspd_label.pack(side='left')
        self.hssspd_entry.pack(side='left')

        #Create the widgets for eleven frame = fd (prediction of fertility disease)
        self.fd_predict_ta = tk.Text(self.eleven_frame,height = 10, width = 25,bg= 'light blue')

        #Create predict button and quit button
        self.btn_predict = tk.Button(self.eleven_frame, text='Predict Fertility Disease', command=self.predict_fd)
        self.btn_quit = tk.Button(self.eleven_frame, text='Quit', command=self.main_window.destroy)


        self.fd_predict_ta.pack(side='left')
        self.btn_predict.pack()
        self.btn_quit.pack()

        # Pack the frames.
        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()
        self.four_frame.pack()
        self.five_frame.pack()
        self.six_frame.pack()
        self.seven_frame.pack()
        self.eight_frame.pack()
        self.nine_frame.pack()
        self.ten_frame.pack()
        self.eleven_frame.pack()

        # Enter the tkinter main loop.
        tk.mainloop()
    def predict_fd(self):
        result_string = ""

        self.fd_predict_ta.delete(0.0, tk.END)

        season = self.click_season_var.get()
        if(season == "winter"):
            season = -1;
        elif(season == "spring"):
            season = -0.33;
        elif(season == "summer"):
            season = 0.33;
        else:
            season = 1;


        age = self.age_entry.get()
        # age = patient_age/36



        childish_disease = self.click_cd_var.get()
        if(childish_disease == "Yes"):
            childish_disease = 0
        else:
            childish_disease = 1


        accident_or_serious_trauma = self.click_ast_var.get()
        if(accident_or_serious_trauma == "Yes"):
            accident_or_serious_trauma = 0
        else:
            accident_or_serious_trauma = 1

        surgical_intervention = self.click_st_var.get()
        if(surgical_intervention == "Yes"):
            surgical_intervention = 0
        else:
            surgical_intervention = 1

        high_fevers_in_the_last_year = self.click_hfly_var.get()
        if(high_fevers_in_the_last_year == "less than three months ago"):
            high_fevers_in_the_last_year = -1
        elif(high_fevers_in_the_last_year == "more than three months ago"):
            high_fevers_in_the_last_year = 0
        else:
            high_fevers_in_the_last_year = 1


        frequency_of_alcohol_consumption = self.click_fac_var.get()
        if(frequency_of_alcohol_consumption == "several times a day"):
            frequency_of_alcohol_consumption = 0,2
        elif(frequency_of_alcohol_consumption == "every day"):
            frequency_of_alcohol_consumption = 0.4
        elif(frequency_of_alcohol_consumption == "several times a week"):
            frequency_of_alcohol_consumption = 0.6
        elif(frequency_of_alcohol_consumption == "once a week"):
            frequency_of_alcohol_consumption = 0.8
        else:
            frequency_of_alcohol_consumption = 1

        smoking_habit = self.click_sh_var.get()
        if(smoking_habit == "less than three months ago"):
            smoking_habit = -1
        elif(smoking_habit == "more than three months ago"):
            smoking_habit = 0
        else:
            smoking_habit = 1

        hours_spent_sitting_per_day=self.hssspd_entry


        result_string += "===Patient Diagnosis=== \n"
        patient_info = (season,age,childish_disease, accident_or_serious_trauma,surgical_intervention,\
                         high_fevers_in_the_last_year,frequency_of_alcohol_consumption,\
                         smoking_habit, hours_spent_sitting_per_day)


        fd_prediction =  best_model.predict([patient_info])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        result = fd_prediction

        if(fd_prediction == [0]):
            result_string = (disp_string, '\n', "0 - You have lower risk of fertility disease")
        else:
            result_string = (disp_string, '\n'+ "1 - You have higher risk of fertility disease, please consult your GP soon")
        self.fd_predict_ta.insert('1.0',result_string)




my_cvd_GUI = CVD_GUI()

