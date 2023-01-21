import customtkinter as ctk

def calculate():
    weight = float(weight_ent.get())
    height = float(height_ent.get())

    bmi = weight / (height ** 2)

    bmi = round(bmi, 1)

    if 10.5 > bmi:
        result_lbl.configure(text_color='blue')
        result_var.set(f'Your BMI: {bmi}\nYour Rank: Underweight, \nYou need to gain weight.')

    if 24.9 >= bmi >= 18.5:
        result_lbl.configure(text_color='lightgreen')
        result_var.set(f'Your BMI: {bmi}\nYour Rank: Normal, \nYou are all ok!')

    if 29.9 >= bmi >= 25:
        result_lbl.configure(text_color='yellow')
        result_var.set(f'Your BMI: {bmi}\nYour Rank: Overweight, \nYou need to lose a little weight.')

    if 34.9 >= bmi >= 30:
        result_lbl.configure(text_color='orange')
        result_var.set(f'Your BMI: {bmi}\nYour Rank: Obese, \nYou should lose some weight.')

    if bmi > 35:
        result_lbl.configure(text_color='red')
        result_var.set(f'Your BMI: {bmi}\nYour Rank: Extremely Obese, \nYou must lose some weight.')

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.title('BMI Calculator')
root.geometry('335x235')
root.config(padx=20, pady=20)

weight_lbl = ctk.CTkLabel(master=root, text='Weight (kg) : ', pady=15)
height_lbl = ctk.CTkLabel(master=root, text='Height (m) : ', pady=15)

weight_lbl.grid(column=0, row=0)
height_lbl.grid(column=0, row=1)

weight_ent = ctk.CTkEntry(master=root, corner_radius=5)
height_ent = ctk.CTkEntry(master=root, corner_radius=5)

weight_ent.grid(column=1, row=0)
height_ent.grid(column=1, row=1)

submit_btn = ctk.CTkButton(master=root, text='Submit', command=calculate)
submit_btn.grid(columnspan=2, row=2)

result_var = ctk.StringVar(value='')
result_lbl = ctk.CTkLabel(master=root, textvariable=result_var,
                            font=('Arial', 10),
                            text_color='white')
result_lbl.grid(columnspan=3, row=3)

root.mainloop()
