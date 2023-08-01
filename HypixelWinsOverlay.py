from tkinter import *
from GetData import GetBridgeWinsData
from tkinter import messagebox
import threading
import os
class HypixelWinsOverlayGUI:
    def __init__(self):
        self.window = Tk()
        self.l1 = Label(self.window,text="Please type your API key")
        self.l1.pack()
        self.e1 = Entry(self.window)
        self.e1.pack()
        self.b1 = Button(self.window,text="Submit API Key",command=self.run_api_key_submit)
        self.b1.pack()
        self.window.mainloop()
    def run_api_key_submit(self):
        apientry = self.e1.get()
        self.GBWD = GetBridgeWinsData(apientry)
        if self.GBWD.ValidApiToken == False:
            messagebox.showerror("API Key is invalid","API Key is invalid")
            os._exit(-1)
        self.l1.config(text="Enter Your Username")
        self.e1.delete(0, END)
        self.b1.config(text="Submit Username",command=self.starthud)
    def playerhud(self):
        self.username = self.e1.get()
        try:
            self.GBWD.playernametouuid(self.username)
        except Exception:
            messagebox.showerror("Couldnt find username")
            return
        self.window2 = Tk()
        self.window2.geometry("400x150")
        self.window2.config(bg="#00b140")
        self.l2 = Label(self.window2,text=f"Wins: {self.GBWD.GetBridgeWins(self.username)}",font=("Arial",26),fg="white",bg="#00b140")
        self.l2.pack(pady=35)
        self.update_label()
        self.window2.mainloop()
    def update_label(self):
        print("updating")
        self.l2.destroy()
        self.l2 = Label(self.window2,text=f"Wins: {self.GBWD.GetBridgeWins(self.username)}",font=("Arial",26),fg="white",bg="#00b140")
        self.l2.pack(pady=35)
        self.l1.pack(pady=35)
        self.window2.after(6000 * 5, self.update_label)
    def starthud(self):
        hudthread = threading.Thread(target=self.playerhud)
        hudthread.start()
        
if __name__ == "__main__":
    winoverlay = HypixelWinsOverlayGUI()