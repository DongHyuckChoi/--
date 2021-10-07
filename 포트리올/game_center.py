import tkinter
import RPG_pygame
import Action_pygame
import Shooting_pygame
import Racing_pygame

def key_down(e):
    key = e.keysym
    if key == "1":
        RPG_pygame.main()
    if key == "2":
        Action_pygame.main()
    if key == "3":
        Shooting_pygame.main()
    if key == "4":
        Racing_pygame.main()

root = tkinter.Tk()
root.title("포트폴리올")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()
img = tkinter.PhotoImage(file="C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\gc2080.png")
canvas.create_image(400, 400, image=img)
root.mainloop()