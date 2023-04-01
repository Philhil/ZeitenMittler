
from tkinter import *
import tkinter as tk

win = tk.Tk()
time1 = NONE
time2 = NONE
time3 = NONE
result = NONE

class DateEntry(tk.Frame):
    def __init__(self, master, label, frame_look={}, **look):
        args = dict(relief=tk.SUNKEN, border=1)
        args.update(frame_look)
        tk.Frame.__init__(self, master, **args)

        args = {'relief': tk.FLAT}
        args.update(look)

        self.label = tk.Label(self, text=label, **args)
        self.entry_min = tk.Entry(self, width=2, **args)
        self.label_1 = tk.Label(self, text=':', **args)
        self.entry_sec = tk.Entry(self, width=2, **args)
        self.label_2 = tk.Label(self, text=':', **args)
        self.entry_millisec = tk.Entry(self, width=2, **args)

        self.label.pack(side=tk.LEFT)
        self.entry_min.pack(side=tk.LEFT)
        self.label_1.pack(side=tk.LEFT)
        self.entry_sec.pack(side=tk.LEFT)
        self.label_2.pack(side=tk.LEFT)
        self.entry_millisec.pack(side=tk.LEFT)

        self.entries = [self.entry_min, self.entry_sec, self.entry_millisec]

        self.entry_min.bind('<KeyRelease>', lambda e: self._check(0, 2))
        self.entry_sec.bind('<KeyRelease>', lambda e: self._check(1, 2))
        self.entry_millisec.bind('<KeyRelease>', lambda e: self._check(2, 4))

    def _backspace(self, entry):
        cont = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, cont[:-1])

    def _check(self, index, size):
        entry = self.entries[index]
        next_index = index + 1
        next_entry = self.entries[next_index] if next_index < len(self.entries) else None
        data = entry.get()

        if len(data) > size or not data.isdigit():
            self._backspace(entry)
        if len(data) >= size and next_entry:
            next_entry.focus()

    def get(self):
        return [e.get() for e in self.entries]

def calcCallBack():
    global time1, time2, time3, result
    time1_min = time1_sec = time1_millisec = time1_total_in_millisec = 0
    time2_min = time2_sec = time2_millisec = time2_total_in_millisec = 0
    time3_min = time3_sec = time3_millisec = time3_total_in_millisec = 0

    try:
        time1_min = int(time1.entry_min.get())
        time1_sec = int(time1.entry_sec.get())
        time1_millisec = int(time1.entry_millisec.get())
        time1_total_in_millisec = (time1_min * 60000) + (time1_sec * 1000) + time1_millisec
    except:
        time1.entry_min.config({"background": "Red"})
        time1.entry_sec.config({"background": "Red"})
        time1.entry_millisec.config({"background": "Red"})

    if time1_sec >= 60:
        time1.entry_sec.config({"background": "Red"})
        result.entry_min.config({"background": "Red"})
        result.entry_sec.config({"background": "Red"})
        result.entry_millisec.config({"background": "Red"})

    try:
        time2_min = int(time2.entry_min.get())
        time2_sec = int(time2.entry_sec.get())
        time2_millisec = int(time2.entry_millisec.get())
        time2_total_in_millisec = (time2_min * 60000) + (time2_sec * 1000) + time2_millisec
    except:
        time2.entry_min.config({"background": "Red"})
        time2.entry_sec.config({"background": "Red"})
        time2.entry_millisec.config({"background": "Red"})

    if time2_sec >= 60:
        time2.entry_sec.config({"background": "Red"})
        result.entry_min.config({"background": "Red"})
        result.entry_sec.config({"background": "Red"})
        result.entry_millisec.config({"background": "Red"})

    try:
        time3_min = int(time3.entry_min.get())
        time3_sec = int(time3.entry_sec.get())
        time3_millisec = int(time3.entry_millisec.get())
        time3_total_in_millisec = (time3_min * 60000) + (time3_sec * 1000) + time3_millisec
    except:
        time3.entry_min.config({"background": "Red"})
        time3.entry_sec.config({"background": "Red"})
        time3.entry_millisec.config({"background": "Red"})

    if time3_sec >= 60:
        time3.entry_sec.config({"background": "Red"})
        result.entry_min.config({"background": "Red"})
        result.entry_sec.config({"background": "Red"})
        result.entry_millisec.config({"background": "Red"})

    millisec = 0
    divider = 0

    if(time1_total_in_millisec > 0):
        millisec += time1_total_in_millisec
        divider += 1

    if (time2_total_in_millisec > 0):
        millisec += time2_total_in_millisec
        divider += 1

    if (time3_total_in_millisec > 0):
        millisec += time3_total_in_millisec
        divider += 1

    if(divider > 0):
        millisec = int(millisec / divider)

        seconds = (millisec / 1000) % 60
        seconds = int(seconds)
        minutes = (millisec / (1000 * 60)) % 60
        minutes = int(minutes)
        millisec = millisec - (seconds * 1000) - (minutes * 60000)

        result.entry_min.delete(0, 'end')
        result.entry_sec.delete(0, 'end')
        result.entry_millisec.delete(0, 'end')
        result.entry_min.insert(0,minutes)
        result.entry_sec.insert(0,seconds)
        result.entry_millisec.insert(0,millisec)


def resetCallBack():
    time1.entry_min.delete(0, 'end')
    time1.entry_sec.delete(0, 'end')
    time1.entry_millisec.delete(0, 'end')
    time1.entry_min.config({"background": "White"})
    time1.entry_sec.config({"background": "White"})
    time1.entry_millisec.config({"background": "White"})

    time2.entry_min.delete(0, 'end')
    time2.entry_sec.delete(0, 'end')
    time2.entry_millisec.delete(0, 'end')
    time2.entry_min.config({"background": "White"})
    time2.entry_sec.config({"background": "White"})
    time2.entry_millisec.config({"background": "White"})

    time3.entry_min.delete(0, 'end')
    time3.entry_sec.delete(0, 'end')
    time3.entry_millisec.delete(0, 'end')
    time3.entry_min.config({"background": "White"})
    time3.entry_sec.config({"background": "White"})
    time3.entry_millisec.config({"background": "White"})

    result.entry_min.delete(0, 'end')
    result.entry_sec.delete(0, 'end')
    result.entry_millisec.delete(0, 'end')
    result.entry_min.config({"background": "White"})
    result.entry_sec.config({"background": "White"})
    result.entry_millisec.config({"background": "White"})

    #set curser to time 1
    time1.entry_min.focus()
def createGUI():
    global time1, time2, time3, result
    win.title('Zeiten Mittler')
    win.geometry("550x500")

    time1 = DateEntry(win, "Time 1:", font=('Helvetica', 40, tk.NORMAL), border=0)
    time1.pack()

    time2 = DateEntry(win, "Time 2:", font=('Helvetica', 40, tk.NORMAL), border=0)
    time2.pack()

    time3 = DateEntry(win, "Time 3:", font=('Helvetica', 40, tk.NORMAL), border=0)
    time3.pack()

    calcbtn = tk.Button(win, text="Mittelwert berechnen", font=('Helvetica', 30, tk.NORMAL), command = calcCallBack)
    calcbtn.pack(pady=20)

    result = DateEntry(win, "Mittelwert:", font=('Helvetica', 40, tk.NORMAL), border=1)
    result.pack()

    resetbtn = tk.Button(win, text="Reset", font=('Helvetica', 30, tk.NORMAL), command = resetCallBack)
    resetbtn.pack(pady=20)

    win.bind('<Return>', lambda e: print(time1.get()))
    win.bind('<Return>', lambda e: print(time2.get()))
    win.bind('<Return>', lambda e: print(time3.get()))
    win.bind('<Return>', lambda e: print(result.get()))
    win.mainloop()

if __name__ == '__main__':
    createGUI()