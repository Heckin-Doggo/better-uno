import tkinter as tk

count = 0

master = tk.Tk()

def callback():
    global count
    count += 1
    print("yep {}".format(count))

butt = tk.Button(master, text="Click Me!", command=callback, padx=20, pady=40)
butt.pack()

f = tk.Frame(master, height=320, width=480)
f.pack_propagate(0)  # don't shrink
f.pack()

b = tk.Button(f, text="GET ME OUTTA HERE", command = master.quit, padx=30, pady=50)
b.pack(fill=tk.BOTH, expand=1)


tk.mainloop()