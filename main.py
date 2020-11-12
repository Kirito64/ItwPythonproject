from tkinter import *
from Converter import Converter

root = Tk()
converter = Converter('https://api.exchangerate-api.com/v4/latest/USD')
variable1 = StringVar(root) 
variable2 = StringVar(root) 


variable1.set("currency") 
variable2.set("currency") 



def RealTimeCurrencyConversion(): 
    from_currency = variable1.get() 
    to_currency = variable2.get() 
    amount = float(Amount1_field.get()) 
    new_amount = converter.Convert(from_currency, to_currency, amount)
    print(from_currency)
    print(to_currency)
    Amount2_field.insert(0, str(new_amount)) 



def clear_all() : 
    Amount1_field.delete(0, END)  
    Amount2_field.delete(0, END) 



if __name__ == "__main__":
    root.configure(background = 'light green')  

    root.geometry("450x250")  
    root.title("ITW Project")
    headlabel = Label(root, text = 'Welcome to Real Time Currency Convertor', fg = 'black', bg = "red")  
    label1 = Label(root, text = "Amount :", fg = 'black', bg = 'dark green') 
    label2 = Label(root, text = "From Currency", fg = 'black', bg = 'dark green')  
    label3 = Label(root, text = "To Currency :",fg = 'black', bg = 'dark green') 
    label4 = Label(root, text = "Converted Amount :", fg = 'black', bg = 'dark green') 


    headlabel.grid(row = 0, column = 1)  
    label1.grid(row = 1, column = 0)  
    label2.grid(row = 2, column = 0) 
    label3.grid(row = 3, column = 0) 
    label4.grid(row = 5, column = 0) 


    Amount1_field = Entry(root)  
    Amount2_field = Entry(root) 


    Amount1_field.grid(row = 1, column = 1, ipadx ="25")  
    Amount2_field.grid(row = 5, column = 1, ipadx ="25") 

    CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"] 

    FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list) 
    ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list) 

    FromCurrency_option.grid(row = 2, column = 1, ipadx = 10) 
    ToCurrency_option.grid(row = 3, column = 1, ipadx = 10) 
        
    button1 = Button(root, text = "Convert", bg = "red", fg = "black",command = RealTimeCurrencyConversion) 
    button1.grid(row = 4, column = 1) 
    button2 = Button(root, text = "Clear", bg = "red", fg = "black", command = clear_all) 
    button2.grid(row = 6, column = 1) 
    root.mainloop()  
