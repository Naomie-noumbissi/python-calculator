import tkinter as tk


fenetre = tk.Tk()
fenetre.title("Calculs simples")
fenetre.geometry("300x450")

affichage = tk.Entry(fenetre, width=5, font=("Arial", 20), borderwidth=5,  relief="ridge")
affichage.grid(row=0, column=0, columnspan=5, pady=10)

def bouton_click(val):
    affichage.insert(tk.END, val)

def bouton_clear():
    affichage.delete(0,tk.END)

def bouton_egal():
    try:
        expression = affichage.get()
        resultat = eval(expression)
        affichage.delete(0, tk.END)
        affichage.insert(0, str(resultat))
    except:
        affichage.delete(0, tk.END)
        affichage.insert(0, "erreur")
bouton = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("3", 3, 0), ("2", 3, 1), ("1", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]
for (text, row, col) in bouton:
    if text == "=":
        b = tk.Button(fenetre, text=text, width=5, height=2, command=bouton_egal)
    else:
        b=tk.Button(fenetre, text=text, width=5, height=2, fg="black", command=lambda
            val=text: bouton_click(val))
    b.grid(row=row, column=col,padx=5,pady=5)

bouton_vide = tk.Button(fenetre, text="C", width=5, height=2,command=bouton_clear,
                        bg="red", fg="white")
bouton_vide.grid(row=5, column=0, columnspan=5,pady=10)

fenetre.mainloop()