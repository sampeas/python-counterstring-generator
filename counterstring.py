from tkinter import Tk

print("CounterString Generator by Samuel Peasnall")

while True:

    while True:
        try:
            total_chars = int(input("Enter string length:"))
            break
        except:
            print("Please enter a valid whole number.")

    counter_string = ""
    chars_remain = total_chars
    cs_block = ""

    while chars_remain > 0:
        if chars_remain == 1:
            cs_block = "*"
        else:
            cs_block = str(chars_remain) + "*"

        counter_string = cs_block + counter_string
        chars_remain -= len(cs_block)

    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.update()
    r.clipboard_append(counter_string)
    r.update()
    r.destroy()

    print(counter_string)
    print("CounterString has been copied to the clipboard.")
