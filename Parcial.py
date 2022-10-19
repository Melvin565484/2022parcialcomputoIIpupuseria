from tkinter import*
from PIL import Image, ImageTk 

  
# Creacion de la ventana
ventana = Tk()
ventana.title('Pupuseria lol')
ventana.config(bg= "Gray")
ventana.geometry('900x600')

opcion = IntVar()
opcion1 = IntVar()
opcion2 = IntVar()

cantidad = IntVar()
res = DoubleVar()


#utilizamos un metodo para generar la factura 
def calcular():
	op = opcion.get()
	precio = cantidad.get()
	queso = 0.70
	fq = 0.65
	re = 0.60
	gaseosa = 0.75
	fresco = 0.60
	choc = 0.50
	domicilio = 1.50
	if op==1 and 4 and 7:
		res.set((queso*precio)+gaseosa+domicilio)
	elif op==1 and 4 and 8:
		res.set((queso*precio)+gaseosa)
	elif op==1 and 5 and 7:
		res.set((queso*precio)+chocolate+domicilio)
	elif op==1 and 5 and 8:
		res.set((queso*precio)+chocolate)
	elif op==1 and 6 and 7:
		res.set((queso*precio)+fresco+domicilio)
	elif op==1 and 6 and 8:
		res.set((queso*precio)+fresco)
	if op==2 and 4 and 7:
		res.set((queso*precio)+gaseosa+domicilio)
	elif op==2 and 4 and 8:
		res.set((queso*precio)+gaseosa)
	elif op==2 and 5 and 7:
		res.set((queso*precio)+chocolate+domicilio)
	elif op==2 and 5 and 8:
		res.set((queso*precio)+chocolate)
	elif op==2 and 6 and 7:
		res.set((queso*precio)+fresco+domicilio)
	elif op==2 and 6 and 8:
		res.set((queso*precio)+fresco)
	if op==3 and 4 and 7:
		res.set((queso*precio)+gaseosa+domicilio)
	elif op==3 and 4 and 8:
		res.set((queso*precio)+gaseosa)
	elif op==3 and 5 and 7:
		res.set((queso*precio)+chocolate+domicilio)
	elif op==3 and 5 and 8:
		res.set((queso*precio)+chocolate)
	elif op==3 and 6 and 7:
		res.set((queso*precio)+fresco+domicilio)
	elif op==3 and 6 and 8:
		res.set((queso*precio)+fresco)


#Etiquetas
etiquetaR = Label(ventana,text="Resultado: ",textvariable=res)
etiquetaR.place(x=660,y=540)
etiqueta1 = Label(ventana,text="Total $")
etiqueta1.place(x=600,y=540)
#Boton para ejecutar la orden
boton1 = Button(ventana,text=">Imprimir Factura<",command=calcular)
boton1.place(x=600,y=500)


etiqueta2 = Label(ventana,text="Especialidades de pupusas...")
etiqueta2.place(x=650,y=100)



#Etiquetas y entry para asignar un valor a cantidad
etiqueta1 = Label(ventana,text="Ingrese la cantidad de pupusas:")
etiqueta1.place(x=600,y=15)
caja1 = Entry(ventana,textvariable=cantidad)
caja1.place(x=600,y=40)

#Etiquetas y Radio buton para realizar la orden
radio1 = Radiobutton(ventana,text="Queso",value=1,variable=opcion)
radio1.place(x=50,y=170)
imagen1 = Image.open(r"images\queso.jpeg")
label1=Label(ventana, image="")
label1.place(x=15, y=16, width=150, height= 150)
imagenresiz1 = imagen1.resize((148,148), Image.Resampling.LANCZOS)
render1= ImageTk.PhotoImage(imagenresiz1)
label1.configure(image=render1)
label1.image=render1


radio2 = Radiobutton(ventana,text="F/Q",value=2,variable=opcion)
radio2.place(x=275,y=170)
imagen2 = Image.open(r"images\fq.jpeg")
label2=Label(ventana, image="")
label2.place(x=225, y=16, width=150, height= 150)
imagenresiz2 = imagen2.resize((148,148), Image.Resampling.LANCZOS)
render2= ImageTk.PhotoImage(imagenresiz2)
label2.configure(image=render2)
label2.image=render2

radio3 = Radiobutton(ventana,text="Revueltas",value=3,variable=opcion)
radio3.place(x=455,y=170)
imagen3 = Image.open(r"images\revueltas.jpeg")
label3=Label(ventana, image="")
label3.place(x=425, y=16, width=150, height= 150)
imagenresiz3 = imagen3.resize((148,148), Image.Resampling.LANCZOS)
render3= ImageTk.PhotoImage(imagenresiz3)
label3.configure(image=render3)
label3.image=render3


radio4 = Radiobutton(ventana,text="Gaseosa",value=4,variable=opcion1)
radio4.place(x=45,y=390)
imagen4 = Image.open(r"images\sodas.jpeg")
label4=Label(ventana, image="")
label4.place(x=10, y=236, width=150, height= 150)
imagenresiz4= imagen4.resize((148,148), Image.Resampling.LANCZOS)
render4= ImageTk.PhotoImage(imagenresiz4)
label4.configure(image=render4)
label4.image=render4



radio5 = Radiobutton(ventana,text="Chocolate",value=5,variable=opcion1)
radio5.place(x=250,y=390)
imagen5 = Image.open(r"images\chocolate.jpeg")
label5=Label(ventana, image="")
label5.place(x=220, y=236, width=150, height= 150)
imagenresiz5= imagen5.resize((148,148), Image.Resampling.LANCZOS)
render5= ImageTk.PhotoImage(imagenresiz5)
label5.configure(image=render5)
label5.image=render5



radio6 = Radiobutton(ventana,text="Fresco",value=6,variable=opcion1)
radio6.place(x=470,y=390)
imagen6 = Image.open(r"images\frescos.jpg")
label6=Label(ventana, image="")
label6.place(x=422, y=236, width=150, height= 150)
imagenresiz6= imagen6.resize((148,148), Image.Resampling.LANCZOS)
render6= ImageTk.PhotoImage(imagenresiz6)
label6.configure(image=render6)
label6.image=render6


etiqueta1 = Label(ventana,text="Entrega a domicilio")
etiqueta1.place(x=300,y=500)
radio7 = Radiobutton(ventana,text="Si",value=7,variable=opcion2)
radio7.place(x=400,y=530)
radio8 = Radiobutton(ventana,text="No",value=8,variable=opcion2)
radio8.place(x=300,y=530)



ventana.mainloop()