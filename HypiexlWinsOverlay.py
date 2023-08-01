from tkinter import *
from GetData import GetBridgeWinsData
from tkinter import messagebox
class HypixelWinsOverlayGUI:
    def __init__(self):
        self.window = Tk()
        l1 = Label(self.window,text="Please type your API key")
        l1.pack()
        self.e1 = Entry(self.window)
        self.e1.pack()
        b1 = Button(self.window,text="Submit API Key",command=self.run_api_key_submit)
        b1.pack()
        self.window.mainloop()
    def run_api_key_submit(self):
        apientry = self.e1.get()
        self.GBWD = GetBridgeWinsData(apientry)
        if self.GBWD.ValidApiToken == False:
            messagebox.showerror("API Key is invalid","API Key is invalid")
if __name__ == "__main__":
    winoverlay = HypixelWinsOverlayGUI()