import tkinter

window = tkinter.Tk()
window.title("BMI V.1")
window.minsize(width=350,height=250)
window.config(padx=25,pady=25)

#label1
boy_label = tkinter.Label(text="Lütfen Boy Giriniz(cm) ",font=('Arial',10,'normal'))
boy_label.config(fg="black",pady=10,padx=10)
boy_label.pack()

#entry1
boy_entry = tkinter.Entry(width=20)
boy_entry.pack()

#label2
kilo_label = tkinter.Label(text="Lütfen Kilo Giriniz(kg)",font=('Arial',10,'normal'))
kilo_label.config(fg="black",padx=10,pady=10)
kilo_label.pack()

#entry2
kilo_entry = tkinter.Entry(width=20)
kilo_entry.pack()

def button_click():
   boy = float(boy_entry.get())/100
   kilo = float(kilo_entry.get())
   BMI = (kilo / (boy*boy))
   bmi_label = tkinter.Label(print("Vücut kitle indeksiniz: ", BMI))
   bmi_label.pack()

   #print("Vücut kitle indeksiniz: ",BMI)
   if (BMI > 0):
      if (BMI <= 18.5):
         print("Düşük kilo")
      elif (BMI <= 24.9):
         print("Normal")
      elif (BMI <= 29.9):
         print("Kilolu")
      else:
         print("obez")
   else:
      print("geçerli bilgileri girin")

#button
button = tkinter.Button(text="Hesapla",command=button_click)
button.config(padx=10,pady=5)
button.pack()

window.mainloop()

#son
