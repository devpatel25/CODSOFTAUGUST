# Task - CALCULATOR
import tkinter as tk

calculation=""
# To add the value 
def add_to_cal(sym):
    global calculation
    calculation+=str(sym)
    txt_result.delete(1.0,"end")
    txt_result.insert(1.0, calculation)

# To evalueate the value
def eval_cal():
    global calculation
    try:
        calculation=str(eval(calculation))
        txt_result.delete(1.0,"end")
        txt_result.insert(1.0, calculation)
    except:
        txt_result.delete(1.0,"end")
        txt_result.insert(1.0, "Error")

# To clear the field
def clrscr():
    global calculation
    calculation=""
    txt_result.delete(1.0,"end")


# Main

root= tk.Tk()
root.title("Calculator")
root.geometry("300x275")
root.configure(bg="black")
root.resizable(False,False)
# result field
txt_result=tk.Text(root,height=2, width=21, font=("arial", 24),fg="white")
txt_result.grid(columnspan=5)

# buttons
b_clr=tk.Button(root,text="C", command=clrscr,width=14,height=2,font=("arial",13,"bold"))
b_clr.grid(row=1,column=1,columnspan=2)
b1=tk.Button(root,text="1", command=lambda: add_to_cal(1), width=5,height=2, font=("arial",13))
b1.grid(row=2,column=1)
b2=tk.Button(root,text="2", command=lambda: add_to_cal(2), width=5,height=2, font=("arial",13))
b2.grid(row=2,column=2)
b3=tk.Button(root,text="3", command=lambda: add_to_cal(3), width=5,height=2, font=("arial",13))
b3.grid(row=2,column=3)
b4=tk.Button(root,text="4", command=lambda: add_to_cal(4), width=5,height=2, font=("arial",13))
b4.grid(row=3,column=1)
b5=tk.Button(root,text="5", command=lambda: add_to_cal(5), width=5,height=2, font=("arial",13))
b5.grid(row=3,column=2)
b6=tk.Button(root,text="6", command=lambda: add_to_cal(6), width=5,height=2, font=("arial",13))
b6.grid(row=3,column=3)
b7=tk.Button(root,text="7", command=lambda: add_to_cal(7), width=5,height=2, font=("arial",13))
b7.grid(row=4,column=1)
b8=tk.Button(root,text="8", command=lambda: add_to_cal(8), width=5,height=2, font=("arial",13))
b8.grid(row=4,column=2)
b9=tk.Button(root,text="9", command=lambda: add_to_cal(9), width=5,height=2, font=("arial",13))
b9.grid(row=4,column=3)
b0=tk.Button(root,text="0", command=lambda: add_to_cal(0), width=14,height=2, font=("arial",13))
b0.grid(row=5,column=1,columnspan=2)
b_point=tk.Button(root,text=".", command=lambda: add_to_cal("."), width=5,height=2, font=("arial",13))
b_point.grid(row=5,column=3)
b_mod=tk.Button(root,text="%", command=lambda: add_to_cal("%"), width=5,height=2, font=("arial",13))
b_mod.grid(row=1,column=3)
b_div=tk.Button(root,text="/", command=lambda: add_to_cal("/"), width=5,height=2, font=("arial",13))
b_div.grid(row=1,column=4)
b_mult=tk.Button(root,text="*", command=lambda: add_to_cal("*"), width=5,height=2, font=("arial",13))
b_mult.grid(row=2,column=4)
b_minus=tk.Button(root,text="-", command=lambda: add_to_cal("-"), width=5,height=2, font=("arial",13))
b_minus.grid(row=3,column=4)
b_add=tk.Button(root,text="+", command=lambda: add_to_cal("+"), width=5,height=2, font=("arial",13))
b_add.grid(row=4,column=4)
b_ans=tk.Button(root,text="=", command=eval_cal, width=5,height=2, font=("arial",13))
b_ans.grid(row=5,column=4)

root.mainloop()