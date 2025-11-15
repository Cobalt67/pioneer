#pioneer
import tkinter as tk

from tkinter import *

grid1 = [[0,0,1,0,0,0,1,0,0,0],[1,2,3,1,0,1,3,1,0,0],[3,2,1,0,0,1,1,0,0,0],[1,0,0,0,1,0,0,0,0,0],[0,0,1,2,3,1,0,0,0,0],[0,1,3,2,1,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

#def open_field():
#	if grid_rectangle[]

def clicked(event):
	canvas = event.widget
	rect = canvas.find_withtag("current")[0]
	print(rect)
	x = canvas.canvasx(event.x)
	y = canvas.canvasy(event.y)
	rect = canvas.find_closest(x,y)[0]
	print(rect)
	cood = (rect%10 ,rect//10)
	x = rect%10
	y = rect//10
	#if grid1[x][y] ==0: 
	#	canvas.itemconfigure(grid_rectangle[x][y], fill="green")
	if grid1[x-1][y] == 0:
		canvas.itemconfigure(grid_rectangle[x-1][y], fill="magenta")
	elif grid1[x-1][y] == 1:
		canvas.itemconfigure(grid_rectangle[x-1][y], fill="green")
	elif grid1[x-1][y] == 2:
		canvas.itemconfigure(grid_rectangle[x-1][y], fill="orange")
	elif grid1[x-1][y] == 3:
		canvas.itemconfigure(grid_rectangle[x-1][y], fill="red")
		paint_grid()	
	print(cood)


def paint_grid(event=None):
	for i in range(len(grid1)):
		for n in range(len(grid1[i])):
			if grid1[i][n] == 0 :
				canvas.itemconfigure(grid_rectangle[i][n], fill="grey")
			elif grid1[i][n] == 1 :
				canvas.itemconfigure(grid_rectangle[i][n], fill="green")
			elif grid1[i][n] == 2 :
				canvas.itemconfigure(grid_rectangle[i][n], fill="orange")
			elif grid1[i][n] == 3 :
				canvas.itemconfigure(grid_rectangle[i][n], fill="red")
			print('paint_grid1')

def start_grid():
	for i in range(len(grid1)):
		for n in range(len(grid1[i])):
			canvas.itemconfigure(grid_rectangle[i][n], fill="grey")
			print('paint_grid2')			

#root window
root = tk.Tk()

#size
root.geometry('500x500')

canvas = tk.Canvas(root,width=500, height = 500)
##
canvas.create_rectangle(25,25,50,50, fill="grey", tags="grid00")
canvas.create_rectangle(50,25,75,50, fill="grey", tags="grid10")
canvas.create_rectangle(75,25,100,50, fill="grey", tags="grid20")
canvas.create_rectangle(100,25,125,50, fill="grey", tags="grid30")
canvas.create_rectangle(125,25,150,50, fill="grey", tags="grid40")
canvas.create_rectangle(150,25,175,50, fill="grey", tags="grid50")
canvas.create_rectangle(175,25,200,50, fill="grey", tags="grid60")
canvas.create_rectangle(200,25,225,50, fill="grey", tags="grid70")
canvas.create_rectangle(225,25,250,50, fill="grey", tags="grid80")
canvas.create_rectangle(250,25,275,50, fill="grey", tags="grid90")

canvas.create_rectangle(25,50,50,75, fill="grey", tags="grid01")
canvas.create_rectangle(50,50,75,75, fill="grey", tags="grid11")
canvas.create_rectangle(75,50,100,75, fill="grey", tags="grid21")
canvas.create_rectangle(100,50,125,75, fill="grey", tags="grid31")
canvas.create_rectangle(125,50,150,75, fill="grey", tags="grid41")
canvas.create_rectangle(150,50,175,75, fill="grey", tags="grid51")
canvas.create_rectangle(175,50,200,75, fill="grey", tags="grid61")
canvas.create_rectangle(200,50,225,75, fill="grey", tags="grid71")
canvas.create_rectangle(225,50,250,75, fill="grey", tags="grid81")
canvas.create_rectangle(250,50,275,75, fill="grey", tags="grid91")

canvas.create_rectangle(25,75,50,100, fill="grey", tags="grid02")
canvas.create_rectangle(50,75,75,100, fill="grey", tags="grid12")
canvas.create_rectangle(75,75,100,100, fill="grey", tags="grid22")
canvas.create_rectangle(100,75,125,100, fill="grey", tags="grid32")
canvas.create_rectangle(125,75,150,100, fill="grey", tags="grid42")
canvas.create_rectangle(150,75,175,100, fill="grey", tags="grid52")
canvas.create_rectangle(175,75,200,100, fill="grey", tags="grid62")
canvas.create_rectangle(200,75,225,100, fill="grey", tags="grid72")
canvas.create_rectangle(225,75,250,100, fill="grey", tags="grid82")
canvas.create_rectangle(250,75,275,100, fill="grey", tags="grid92")

canvas.create_rectangle(25,100,50,125, fill="grey", tags="grid03")
canvas.create_rectangle(50,100,75,125, fill="grey", tags="grid13")
canvas.create_rectangle(75,100,100,125, fill="grey", tags="grid23")
canvas.create_rectangle(100,100,125,125, fill="grey", tags="grid33")
canvas.create_rectangle(125,100,150,125, fill="grey", tags="grid43")
canvas.create_rectangle(150,100,175,125, fill="grey", tags="grid53")
canvas.create_rectangle(175,100,200,125, fill="grey", tags="grid63")
canvas.create_rectangle(200,100,225,125, fill="grey", tags="grid73")
canvas.create_rectangle(225,100,250,125, fill="grey", tags="grid83")
canvas.create_rectangle(250,100,275,125, fill="grey", tags="grid93")

canvas.create_rectangle(25,125,50,150, fill="grey", tags="grid04")
canvas.create_rectangle(50,125,75,150, fill="grey", tags="grid14")
canvas.create_rectangle(75,125,100,150, fill="grey", tags="grid24")
canvas.create_rectangle(100,125,125,150, fill="grey", tags="grid34")
canvas.create_rectangle(125,125,150,150, fill="grey", tags="grid44")
canvas.create_rectangle(150,125,175,150, fill="grey", tags="grid54")
canvas.create_rectangle(175,125,200,150, fill="grey", tags="grid64")
canvas.create_rectangle(200,125,225,150, fill="grey", tags="grid74")
canvas.create_rectangle(225,125,250,150, fill="grey", tags="grid84")
canvas.create_rectangle(250,125,275,150, fill="grey", tags="grid94")

canvas.create_rectangle(25,150,50,175, fill="grey", tags="grid05")
canvas.create_rectangle(50,150,75,175, fill="grey", tags="grid15")
canvas.create_rectangle(75,150,100,175, fill="grey", tags="grid25")
canvas.create_rectangle(100,150,125,175, fill="grey", tags="grid35")
canvas.create_rectangle(125,150,150,175, fill="grey", tags="grid45")
canvas.create_rectangle(150,150,175,175, fill="grey", tags="grid55")
canvas.create_rectangle(175,150,200,175, fill="grey", tags="grid65")
canvas.create_rectangle(200,150,225,175, fill="grey", tags="grid75")
canvas.create_rectangle(225,150,250,175, fill="grey", tags="grid85")
canvas.create_rectangle(250,150,275,175, fill="grey", tags="grid95")

canvas.create_rectangle(25,175,50,200, fill="grey", tags="grid06")
canvas.create_rectangle(50,175,75,200, fill="grey", tags="grid16")
canvas.create_rectangle(75,175,100,200, fill="grey", tags="grid26")
canvas.create_rectangle(100,175,125,200, fill="grey", tags="grid36")
canvas.create_rectangle(125,175,150,200, fill="grey", tags="grid46")
canvas.create_rectangle(150,175,175,200, fill="grey", tags="grid56")
canvas.create_rectangle(175,175,200,200, fill="grey", tags="grid66")
canvas.create_rectangle(200,175,225,200, fill="grey", tags="grid76")
canvas.create_rectangle(225,175,250,200, fill="grey", tags="grid86")
canvas.create_rectangle(250,175,275,200, fill="grey", tags="grid96")

canvas.create_rectangle(25,200,50,225, fill="grey", tags="grid07")
canvas.create_rectangle(50,200,75,225, fill="grey", tags="grid17")
canvas.create_rectangle(75,200,100,225, fill="grey", tags="grid27")
canvas.create_rectangle(100,200,125,225, fill="grey", tags="grid37")
canvas.create_rectangle(125,200,150,225, fill="grey", tags="grid47")
canvas.create_rectangle(150,200,175,225, fill="grey", tags="grid57")
canvas.create_rectangle(175,200,200,225, fill="grey", tags="grid67")
canvas.create_rectangle(200,200,225,225, fill="grey", tags="grid77")
canvas.create_rectangle(225,200,250,225, fill="grey", tags="grid87")
canvas.create_rectangle(250,200,275,225, fill="grey", tags="grid97")

canvas.create_rectangle(25,225,50,250, fill="grey", tags="grid08")
canvas.create_rectangle(50,225,75,250, fill="grey", tags="grid18")
canvas.create_rectangle(75,225,100,250, fill="grey", tags="grid28")
canvas.create_rectangle(100,225,125,250, fill="grey", tags="grid38")
canvas.create_rectangle(125,225,150,250, fill="grey", tags="grid48")
canvas.create_rectangle(150,225,175,250, fill="grey", tags="grid58")
canvas.create_rectangle(175,225,200,250, fill="grey", tags="grid68")
canvas.create_rectangle(200,225,225,250, fill="grey", tags="grid78")
canvas.create_rectangle(225,225,250,250, fill="grey", tags="grid88")
canvas.create_rectangle(250,225,275,250, fill="grey", tags="grid98")

canvas.create_rectangle(25,250,50,275, fill="grey", tags="grid09")
canvas.create_rectangle(50,250,75,275, fill="grey", tags="grid19")
canvas.create_rectangle(75,250,100,275, fill="grey", tags="grid29")
canvas.create_rectangle(100,250,125,275, fill="grey", tags="grid39")
canvas.create_rectangle(125,250,150,275, fill="grey", tags="grid49")
canvas.create_rectangle(150,250,175,275, fill="grey", tags="grid59")
canvas.create_rectangle(175,250,200,275, fill="grey", tags="grid69")
canvas.create_rectangle(200,250,225,275, fill="grey", tags="grid79")
canvas.create_rectangle(225,250,250,275, fill="grey", tags="grid89")
canvas.create_rectangle(250,250,275,275, fill="grey", tags="grid99")
#grid_rectangle=[["grid00","grid01", "grid02","grid03","grid04","grid05"],["grid10","grid11", "grid12","grid13","grid14","grid15"],["grid20","grid21", "grid22","grid23","grid24","grid25"],["grid30","grid31", "grid32","grid33","grid34","grid35"],["grid40","grid41", "grid42","grid43","grid44","grid45"],["grid50","grid51", "grid52","grid53","grid54","grid55"]]
#paint_grid()
grid_rectangle=[["grid00","grid01", "grid02","grid03","grid04","grid05","grid06","grid07","grid08","grid09"],["grid10","grid11", "grid12","grid13","grid14","grid15","grid16","grid17","grid18","grid19"],["grid20","grid21", "grid22","grid23","grid24","grid25","grid26","grid27","grid28","grid29"],["grid30","grid31", "grid32","grid33","grid34","grid35","grid36","grid37","grid38","grid39"],["grid40","grid41", "grid42","grid43","grid44","grid45","grid46","grid47","grid48","grid49"],["grid50","grid51", "grid52","grid53","grid54","grid55","grid56","grid57","grid58","grid59"],["grid60","grid61", "grid62","grid63","grid64","grid65","grid66","grid67","grid68","grid69"],["grid70","grid71", "grid72","grid73","grid74","grid75","grid76","grid77","grid78","grid79"],["grid80","grid81", "grid82","grid83","grid84","grid85","grid86","grid87","grid88","grid89"],["grid90","grid91", "grid92","grid93","grid94","grid95","grid96","grid97","grid98","grid99"]]




canvas.pack()
#He
root.title("Hello!")

#canvas.tag_bind("grid00","<Button-1>",paint_grid)

canvas.bind("<Button-1>",clicked)
#loop
#root.bind("<Up>", press_up)
#root.bind("<KeyPress>", key_press)
# end of game paint_grid()
#start_grid()
#root.after(250,start_grid())
root.mainloop()


