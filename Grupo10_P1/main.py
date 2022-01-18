import tkinter as tk
from LogisticRegression import *
from PIL import ImageTk, Image

BACKGROUND = "#363636"
FONTTEXT = "#84C9FB"
FONT = {"Arial", 16}
STYLE = {
    "font": FONT,
    "bg": BACKGROUND,
    "fg": FONTTEXT
}

class window():
    def __init__(self):
        
        self.Clasificador = Clasificador()

        self.ventana = tk.Tk()
        self.ventana.title('PROYECTO IA')
        self.ventana.resizable(width=False, height=False)
        self.ventana.geometry("700x650")

        self.frameMain = tk.Frame(self.ventana)
        self.frameMain.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.frameMain.grid_columnconfigure(0, weight = 1)
        self.frameMain.grid_rowconfigure(1, weight = 1)

        self.frameHeader = tk.Frame(self.frameMain)
        self.frameHeader.grid(row=0, column=0, sticky=tk.NSEW)
        self.frameHeader.configure(background="#193498")
        tk.Label(self.frameHeader, justify= tk.CENTER, text="ANÁLISIS DE SENTIMIENTOS DEL PRESIDENTE GUILLERMO LASSO", font={"Arial", 16}, fg="#D4ECDD", background="#193498").pack(fill=tk.X, expand=True, padx=5, pady=10)

        self.bodyFrame = tk.Frame(self.frameMain)
        self.bodyFrame.configure(background="white")
        self.bodyFrame.grid(row=1, column=0, sticky=tk.NSEW)

        tk.Label(self.bodyFrame,  justify= tk.LEFT, text="EFICIENCIA DEL ANALIZADOR:").grid(row=1, column=0, padx=20, pady=10)
        tk.Label(self.bodyFrame,  justify= tk.LEFT, text=str("{:.2f}".format(self.Clasificador.eficiencia))).grid(row=1, column=2, padx=10, pady=10)
        tk.Label(self.bodyFrame,  justify= tk.LEFT, text="TWEET:").grid(row=2, column=0)
        tk.Button(self.bodyFrame, text="Clasificar", command=self.analizar, background="#193498", fg="white").grid(row=3, column=2, columnspan=2, sticky=tk.NSEW, pady=20)
        tk.Label(self.bodyFrame,  justify= tk.LEFT, text="RESULTADO:").grid(row=4, column=0, pady=30)
        self.TextArea = tk.Text(self.bodyFrame,  width=50, height=10, padx=15, pady=15, relief="solid")
        self.TextArea.grid(row=2, column=2)

        self.response = tk.StringVar(self.bodyFrame, value=" ")
        self.respuesta = tk.Label(self.bodyFrame,  justify= tk.LEFT, textvariable=self.response).grid(row=5, column=2)

        self.frameHeader.tkraise()
        
        self.lasso = Image.open("lasso.jpg")
        self.lasso = self.lasso.resize((200,120), Image.ANTIALIAS)
        self.imageLasso = ImageTk.PhotoImage(self.lasso)
        self.lassoLabel = tk.Label(self.bodyFrame, image=self.imageLasso)
        self.lassoLabel.grid(row=0, column=2, columnspan=2, sticky=tk.NSEW)

        self.img = Image.open("like.png")
        self.img = self.img.resize((100,100), Image.ANTIALIAS)
        self.imageLike = ImageTk.PhotoImage(self.img)

        self.img2 = Image.open("dislike.png")
        self.img2 = self.img2.resize((100,100), Image.ANTIALIAS)
        self.imageDisLike = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open("neutro.png")
        self.img3 = self.img3.resize((100,100), Image.ANTIALIAS)
        self.imageConf = ImageTk.PhotoImage(self.img3)

        self.imageLabel = tk.Label(self.bodyFrame)
        self.imageLabel.grid(row=4, column=2)

        self.ventana.mainloop()
    
    def analizar(self):
        resultado=""
        texto = self.TextArea.get("1.0", "end").lower()
        # print(texto)
        tweet_v = self.Clasificador.vectorizer.transform([texto])
        respuesta = self.Clasificador.Clasificador.predict(tweet_v);
        if(respuesta[0]==-1):
            self.changeImageDislike()
        elif (respuesta[0]==0):
            self.changeImageConf()
        else:
            self.changeImageLike()

    def changeImageDislike(self):
        self.imageLabel.config(image=self.imageDisLike)
        self.response.set("NEGATIVO")
    
    def changeImageLike(self):
        self.imageLabel.config(image=self.imageLike)
        self.response.set("POSITIVO")
    
    def changeImageConf(self):
        self.imageLabel.config(image=self.imageConf)
        self.response.set("NEUTRAL")
        
window()