from tkinter import *
root = Tk()
coseDaVedere = []
topTextStr = ''
#topTextStrSet = StringVar()

def crea():
    global topTextStr #rendo globale la variabile
    topTextGet = topText.get()#funzione specifica per l'entry
    topTextStr = str(topTextGet) # converto ciò che è nell'entry in stringa
    coseDaVedere.append(topTextStr) #aggiungo la stringa all'array
    label.configure(text=coseDaVedere) #configuro il label in modo che mostri le info
    topText.delete(0, 'end') #cancello ciò che è nell'entry
    
    for x in range(len(coseDaVedere)):
        coseDaVedere[x].bind('<Button-1>',elimina)

    
def elimina(event):
    coseDaVedere.delete(x)


#Aggiungi qualcosa
topFrame = Frame(root, height=300, width=300)
topText = Entry(topFrame)
createButton = Button(topFrame, text="Aggiunge cose alla to do list", command=crea)
topFrame.pack()
topText.grid(column=0,row=0)
createButton.grid(column=1,row=0)

#cose mostrate

label = Label(root,text="")
label.pack()
#topTextStrSet.set(topTextStr)

root.mainloop()
