import tkinter as tk
import tts
from multiprocessing import Process
import keyboard

myTTS = tts.TTS(250)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.instruct = tk.Text(self, height=10, width=30)
        instructions = """Highlight text and press r"""
        self.instruct.pack(side="top")
        self.instruct.insert(tk.END,instructions)
#        self.read = tk.Button(self)
#        self.read["text"] = "read"
#        self.read["command"] = lambda:check(self.runTTS())
#        self.read.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def run_TTS(self):
        myTTS.text_to_speech(myTTS.copy_clipboard())

def run_TTS():
    while True:
        if keyboard.is_pressed('r'):
            myTTS.text_to_speech(myTTS.copy_clipboard())
        if keyboard.is_pressed('q'):
            break

if __name__=='__main__':
    run_TTS()
#    root = tk.Tk()
#    root.title('InstaRead')
#    app = Application(master=root)
#    app.mainloop()
