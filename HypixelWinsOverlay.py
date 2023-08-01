from tkinter import *
from GetData import GetBridgeWinsData
from tkinter import messagebox
import threading
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
        self.l1.config(text="Enter Your Username")
        self.e1.config(text="")
        self.b1.config(text="Submit Username",command=self.starthud)
    def playerhud(self):
        username = self.e1.get()
        try:
            self.GBWD.playernametouuid(username)
        except Exception:
            messagebox.showerror("Couldnt find username")
            return
        window = Tk()
        l1 = Label(window,text=f"Wins: {self.GBWD.GetBridgeWins(username)}")
        l1.pack()
        window.mainloop()
    def starthud(self):
        hudthread = threading.Thread(target=self.playerhud)
        
if __name__ == "__main__":
    winoverlay = HypixelWinsOverlayGUI()