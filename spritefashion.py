import tkinter
images = {}
class objects:
    class image:
        def __init__(self,where,x,y,image_path,name):
            global images
            where.tk.last_image_file = images[image_path] = tkinter.PhotoImage(image_path)
            self.root_sprite = where.root.create_image(x,y,image=images[image_path])
            self.name = name
    class text:
        def __init__(self,where,x,y,string,justify,font,fill,name):
            root_sprite = where.root.create_text(x,y,text=string,justify=justify,fill=fill,font=font)
            self.name = name
    class rectangle:
        def __init__(self,where,x,y,width,height,fill,outline,name):
            root_sprite = where.root.create_rectangle(x, y, x+height, y+width, fill=fill, outline = outline)
            self.name = name
    class square:
        def __init__(self,where,x,y,a,fill,outline,name):
            root_sprite = where.root.create_rectangle(x,y,x+a,x+a,fill=fill,outline=outline)
            self.name=name
    class line:
        def __init__(self,where,x,y,x2,y2,color,width,name):
            root_sprite = where.root.create_line(x,y,x2,y2,fill=color,width=width)
            self.name=name
    class polygon:
        def __init__(self,where,args,fill,outline,name):
            root_sprite = where.root.create_polygon(args,fill=fill,outline=outline)
            self.name=name
    class oval:
        def __init__(self,where,x,y,x2,y2,fill,outline,name):
            root_sprite = where.root.create_oval(x,y,x2,y2,fill=fill,outline=outline)
            self.name=name
    class circle:
        def __init__(self,where,x,y,size,fill,outline,name):
            root_sprite = where.root.create_oval(x,y,x+size,y+size,fill=fill,outline=outline)
            self.name=name
class draw:
    def image(where,x,y,image_path,name="image"):
        where.sprites[name] = objects.image(where,x,y,image_path,name)
    def text(where,x,y,string='',justify='left',font='Arial',fill="black",name='text'):
        where.sprites[name] = objects.text(where,x,y,string,justify,font,fill,name)
    def rectangle(where,x,y,width=144,height=160,fill="black",outline="black",name='rectangle'):
        where.sprites[name] = objects.rectangle(where,x,y,width,height,fill,outline,name)
    def square(where,x,y,a=150,fill="black",outline="black",name='square'):
        where.sprites[name] = objects.square(where,x,y,a,fill,outline,name)
    def line(where,x,y,x2,y2,color='black',width=1,name="line"):
        where.sprites[name] = objects.line(where,x,y,x2,y2,color,width,name)
    def polygon(where,*args,fill='black',outline='black',name='polygon'):
        where.sprites[name] = objects.polygon(where,args,fill,outline,name)
    def oval(where,x,y,x2,y2,fill="black",outline="black",name="oval"):
        where.sprites[name] = objects.oval(where,x,y,x2,y2,fill,outline,name)
    def circle(where,x,y,size=100,fill="black",outline="black",name="circle"):
        where.sprites[name] = objects.circle(where,x,y,size,fill,outline,name)
def bind(where,name,command,action='<ButtonPress-1>'):
    where.root.tag_bind(where.sprites[name], '<ButtonPress-1>', command)   
class window:
    '''Your programs main window. (or not)'''
    def __init__(self,width=1000,height=800,title="SpriteFashion window"):
        '''Initalization command'''
        self.sprites = {}
        self.exited = False
        self.tk = tkinter.Tk()
        self.tk.geometry(str(width)+'x'+str(height))
        self.tk.title(title)
        self.width=width
        self.height=height
        self.root = tkinter.Canvas(width=width,height=height)
        self.root.pack()
    def coords(self,obj_name):
        return self.root.coords(self.sprites[obj_name])
    def move(self,obj_name,x,y):
        self.root.move(self.sprites[obj_name],x,y)
    def updateActionsUpdate(self,function):
        if type(function).__name__ == "function":
            self.updateActions = function
    def updateActions(self):
        '''Place for your commands and
stuff in main loop.'''
        pass
    def on_exit(self):
        '''Closes the window. You can change this script,
but don't forget to add this part on the top:
self.tk.destroy()
self.exited = True'''
        try: self.tk.destroy()
        except: pass
        self.exited = True
    def mainloop(self):
        '''Window main loop. Dejavu, anyone?
In arguments you must insert the window class.
(sorry for making it harder, but this is the only way)'''
        while not self.exited:
            self.tk.update()
            self.root.update()
            self.root.update_idletasks()
            try:
                self.tk.protocol("WM_DELETE_WINDOW",self.on_exit)
                self.window_x = self.tk.winfo_x()
                self.window_y = self.tk.winfo_y()
                self.window_width = self.tk.winfo_screenwidth()
                self.window_height = self.tk.winfo_screenheight()
                self.root.config(width=self.window_width,height=self.window_height)
                self.mouse_coords_x = self.tk.winfo_pointerx() - self.tk.winfo_rootx()
                self.mouse_coords_y = self.tk.winfo_pointery() - self.tk.winfo_rooty()
            except: self.on_exit()
            self.updateActions()
    def title(self,*args):
        '''Changes the title of window. Dejavu, anyone?'''
        try:
            self.tk.title(" ".join(args))
        except TypeError:
            raise TypeError("Title must be done from string, but none-string found.")
    def size(width=1000,height=800):
        '''Changes the size of window.'''
        self.tk.geometry(str(width)+'x'+str(height))
if __name__ == "__main__":
    new_window = window()
    draw.text(new_window,100,50,'це тест','center','text')
    new_window.mainloop()