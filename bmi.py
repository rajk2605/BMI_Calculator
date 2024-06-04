# task 2 
# BMI calculator

from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    gender = c.get()
    age = ent_age.get()
    height = ent_height.get()
    weight = ent_weight.get()

    # Input data validations
    if not gender:
        messagebox.showerror("Error", "Please select a gender.")
        return
    if not age:
        messagebox.showerror("Error", "Please Enter age.")
        return
    if not height:
        messagebox.showerror("Error", "Please Enter height")
        return
    if not weight:
        messagebox.showerror("Error", "Please Enter Weight")
        return
    if age.strip() == "":
        messagebox.showerror("Error", "age cannot be spaces")
        return
    if height.strip() == "":
        messagebox.showerror("Error", "height cannot be spaces")
        return
    if weight.strip() == "":
        messagebox.showerror("Error", "weight cannot be spaces")
        return
    if age.isalpha():
        messagebox.showerror("Error", "age cannot be text")
        return
    if height.isalpha():
        messagebox.showerror("Error", "Height cannot be text")
        return
    if weight.isalpha():
        messagebox.showerror("Error", "Weight cannot be text")
        return
    if not age.replace('.', '', 1).isdigit():
        messagebox.showerror(f"Error", "age cannot be Special Characters")
    if not height.replace('.', '', 1).isdigit():
        messagebox.showerror(f"Error", "height cannot be Special Characters")
    if not weight.replace('.', '', 1).isdigit():
        messagebox.showerror(f"Error", "weight cannot be Special Characters")

  

    
    try:
        age = int(age)
        height = float(height)
        weight = float(weight)

    except ValueError as e:
        print("Error", "Something Went Wrong!")
        return
    
    if (age == 0) or (age >= 120):
        messagebox.showerror("Error", "Invalid! Age should be between 2yrs to 120yrs")
        return
    if (age < 0)  :
        messagebox.showerror("Error", " Age cannot be Negative")
        return
    if (height < 0):
        messagebox.showerror("Error", "height cannot be Negative")
        return
    if (height == 0) or (height > 300 ):
        messagebox.showerror("Error", "Invalid! Height data within 300cm.")
        return
    if (weight < 0):
        messagebox.showerror("Error", "weight cannot be Negative")
        return

    if (weight == 0) or (weight > 300 ):
        messagebox.showerror("Error", "Invalid! Weight data within 300kgs")
        return
  

  	
    ent_age.delete(0 ,'end')
    ent_height.delete(0, 'end')
    ent_weight.delete(0, 'end')
    ent_age.focus()
    c.set(0)

    
    

    # Calculate BMI
    bmi = weight / ((height/100) ** 2)
    bmi = round(bmi, 2)
    #messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        messagebox.showinfo('BMI', f'Your BMI = {bmi}   Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI', f'Your BMI = {bmi}   Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI', f'Your BMI = {bmi}   Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI', f'Your BMI = {bmi}   Obesity') 
    else:
        messagebox.showerror('BMI', 'something went wrong!')
	



root = Tk()
root.title("BMI Calculator")
root.geometry("800x500+50+50")
root.configure(bg="lightgray")
f = ("Tw cen MT", 20, "bold")

#TITLE
lab_title = Label(root, text="BMI Calculator", font=("Times New Roman",28),bg="lightgray")
lab_title.place(x=275, y=5)

lab_title = Label(root, text="Body Mass Index", font=("Times New Roman",16),bg="lightgray")

lab_title.place(x=315, y=45)


#GENDER
c = IntVar()
c.set(0)
lab_choice = Label(root, text="Gender", font=f,bg="lightgray")
rb_male = Radiobutton(root, text="Male", font=f, variable=c, value=1,bg="lightgray")
rb_female = Radiobutton(root, text="Female", font=f, variable=c, value=2,bg="lightgray")

lab_choice.place(x=50, y=85)
rb_male.place(x=200, y=85)
rb_female.place(x=330, y=85)



#AGE
lab_age = Label(root, text="Age",font=f,bg="lightgray")
lab_age.place(x=50, y=160)

lab_agecondition = Label(root,text="*Between 2yrs to 120yrs", font=(("Tw cen MT", 14, "italic")),bg="lightgray")
lab_agecondition.place(x=200, y=200)

ent_age = Entry(root, font=f, text="years")
ent_age.place(x=200, y=160)

#btn_check = Button(root, text="Check", font=("Tw cen MT",12,"bold"),command=age_index)
#btn_check.place(x=500, y=160)


#HEIGHT
lab_height = Label(root, text="Height", font=f,bg="lightgray")
lab_height.place(x=50,y=255)

ent_height = Entry(root,font=f, width=5)
ent_height.place(x=200, y=255)

lab_cm = Label(root, text="in cm", font=("tw cent MT", 16),bg="lightgray")
lab_cm.place(x=280, y=265)


#btn_check = Button(root, text="Check", font=("Tw cen MT",12,"bold"))
#btn_check.place(x=350, y=260)


#WEIGHT
lab_weight = Label(root, text="Weight", font=f,bg="lightgray")
lab_weight.place(x=50, y=335)

ent_weight = Entry(root, font=f, width=5)
ent_weight.place(x=200, y=335)

lab_weightinkgs = Label(root, text="Kgs", font=("tw cent MT", 16),bg="lightgray")
lab_weightinkgs.place(x=290, y=345)

#btn_check = Button(root, text="Check", font=("Tw cen MT",12,"bold"))
#btn_check.place(x=350, y=340)


#CALCULATE BUTTON
btn_calculate = Button(root, text="Calculate", font=f, command=calculate_bmi)
btn_calculate.place(x=315, y=400)

#RESET BUTTON
#btn_reset = Button(root, text="Reset", font=f, command=reset)
#btn_reset.place(x=200, y=400)

#EXIT BUTTON
btn_exit = Button(root, text="Exit", font=f,  command=lambda:root.destroy())
btn_exit.place(x=480,y=400)           

root.mainloop()