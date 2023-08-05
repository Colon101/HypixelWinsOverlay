import tkinter as tk
from GetData import  GetBridgeData as GetBridgeWinsData
from tkinter import messagebox
import threading
import os

class HypixelWinsOverlayGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Enter API Key")
        self.window.geometry("300x150")
        self.api_label = tk.Label(self.window, text="Please type your API key")
        self.api_label.pack(pady=10)
        self.api_entry = tk.Entry(self.window)
        self.api_entry.insert(tk.END,"0d4cbe68-c39d-474b-9893-597224e30f35")
        self.api_entry.pack(pady=5)
        self.api_button = tk.Button(self.window, text="Submit API Key", command=self.run_api_key_submit)
        self.api_button.pack(pady=5)
        self.api_valid = False
        self.window.mainloop()

    def run_api_key_submit(self):
        self.window.title("Enter username")
        api_entry = self.api_entry.get()
        self.GBWD = GetBridgeWinsData(api_entry)
        if not self.GBWD.ValidApiToken:
            messagebox.showerror("API Key is invalid", "API Key is invalid")
            os._exit(-1)
        self.api_label.config(text="Enter Your Username")
        self.api_entry.delete(0, tk.END)
        self.api_entry.focus()
        self.api_entry.bind("<Return>",self.starthud)
        self.api_button.config(text="Submit Username", command=self.starthud)
        self.api_valid = True

    def create_player_hud(self):
        if not self.api_valid:
            messagebox.showerror("Error", "Please submit a valid API key first.")
            return

        self.username = self.api_entry.get()
        try:
            self.GBWD.playernametouuid(self.username)
        except Exception:
            messagebox.showerror("Error", "Couldn't find the username.")
            return

        self.window2 = tk.Toplevel(self.window)
        self.window2.geometry("1000x475")
        self.window2.config(bg="#00b140")
        self.window2.title(self.username)
        self.wins_label = tk.Label(self.window2, text="", font=("Arial", 26*5), fg="white", bg="#00b140")
        self.wins_label.pack(pady=10)
        self.wins_this_stream_label = tk.Label(self.window2, text="", font=("Arial", 16*5), fg="white", bg="#00b140")
        self.wins_this_stream_label.pack()
        self.first_time = self.GBWD.GetBridgeInfo(self.username)
        self.winloss = tk.Label(self.window2, text="", font=("Arial", 10*5), fg="white", bg="#00b140")
        self.winloss.pack()
        self.kdr = tk.Label(self.window2, text="", font=("Arial", 8*5), fg="white", bg="#00b140")
        self.kdr.pack()
        self.update_label()

    def update_label(self):
        allinfo = self.GBWD.GetBridgeInfo(self.username)
        wins = allinfo[0] - self.first_time[0]
        losses = allinfo[0] - self.first_time[0]
        if wins == 0:
            winloss = 0
        elif losses == 0:
            winloss = wins
        else:
            winloss = round(wins/losses * 10 ) / 10
        kills = allinfo[4] - self.first_time[4]
        deaths = allinfo [5] - self.first_time[5]
        if kills == 0:
            kdr = 0
        elif deaths == 0:
            kdr = kills
        else:
            kdr = round(kills/deaths * 100) / 100
        self.wins_label.config(text=f"Wins: {allinfo[0]}")
        self.wins_this_stream_label.config(text=f"Wins this stream: {allinfo[0]-self.first_time[0]}")
        self.winloss.config(text=f"WLR: {allinfo[2]}, Livestream WLR: {winloss}")
        self.kdr.config(text=f"KDR: {allinfo[3]} Livestream KDR: {kdr}")
        self.window2.after(6000 * 1, self.update_label)

    def starthud(self,event="Weee"):
        hud_thread = threading.Thread(target=self.create_player_hud)
        hud_thread.start()

if __name__ == "__main__":
    winoverlay = HypixelWinsOverlayGUI()
