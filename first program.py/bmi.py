from tkinter import *

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        height /= 100
        height **= 2
        bmi = weight / height

        
        
        
        if bmi < 18.5:
            message = f"You are underweight.\nTry gaining {abs(round(weight - (height * 18.5), 2))} kg."
        elif 18.5 <= bmi <= 24.9:
            message = "You are healthy.\nKeep it up!"
        elif 25.0 <= bmi <= 29.9:
            message = "You are overweight."
        elif 30.0 <= bmi <= 34.9:
            message = "You are obese."
        elif 35.0 <= bmi <= 39.9:
            message = "You are severely obese."
        else:
            message = "You are morbidly obese."

        result_text = f"Your BMI is: {bmi:.2f}"
        result_label.config(text=f"{result_text}\n{message}") 

        if bmi > 24.9:
            slweight = weight - (height * 24.9)
            result_label.config(text=f"{result_text}\n{message}\nTry losing {round(slweight, 2)} kg.")

        
        
    
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

bmi_app = Tk()

bmi_app.geometry("720x480")
bmi_app.title("BMI Calculator")

icon = PhotoImage(file="first program.py/z.png")
bmi_app.iconphoto(True,icon)
bmi_app.config(background="#f3d6ff")

label = Label(bmi_app,
              text="BMI CALCULATOR",
              font=('Arial',40,'bold'),
              fg='black',
              bg=None)
label.pack(pady=50)


# Entry widgets for height and weight
height_label = Label(bmi_app, text="Height (cm):", font=('Arial', 12))
height_label.pack(pady=5)
height_entry = Entry(bmi_app, font=('Arial', 12))
height_entry.pack(pady=5)

weight_label = Label(bmi_app, text="Weight (kg):", font=('Arial', 12))
weight_label.pack(pady=5)
weight_entry = Entry(bmi_app, font=('Arial', 12))
weight_entry.pack(pady=5)

# Button to calculate BMI
calculate_button = Button(bmi_app, text="Calculate", font=('Arial', 12), command=calculate_bmi)
calculate_button.pack(pady=20)

# Label to display BMI result
result_label = Label(bmi_app, text="", font=('Arial', 12), wraplength=300)
result_label.pack()

# Center the window on the screen
bmi_app.eval('tk::PlaceWindow . center')

bmi_app.mainloop()
