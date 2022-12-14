import os
from tkinter import *
from PIL import ImageTk, Image

import cv2
import pyautogui


_DIR = os.path.dirname(os.path.realpath(__file__))
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.03


class App(Tk):
    """사이드바 객체.

    Example:
    >>> process = Process(cap)
    >>> app = App(process.run)
    >>> app.wm_attributes("-topmost", 1)
    >>> app.mainloop()
    """

    def __init__(self, function):
        Tk.__init__(self)
        # Tk.title(self, "SideBar")
        Tk.geometry(self, "140x410-50+50")
        Tk.resizable(self, 0, 0)
        Tk.configure(self, bg="white")
        self._allow_showing_frame = True
        self._allow_detecting_face = True
        self._btn_command = None
        self.__process = function

        self.__eye = self._img("eye.png")
        self.__eye_slash = self._img("eye-slash.png")
        self.__x_square = self._img("x-square.png")
        self.__zoom_in = self._img("zoom-in.png")
        self.__zoom_out = self._img("zoom-out.png")
        self.__arrow_up = self._img("arrow-up.png")
        self.__arrow_down = self._img("arrow-down.png")
        btn_style = {"bg": "white", "borderwidth": 1, "relief": "flat"}
        self.__btn_show = Button(
            self,
            image=self.__eye,
            command=self._show,
            **btn_style,
        )
        self.__btn_hide = Button(
            self,
            image=self.__eye_slash,
            command=self._hide,
            **btn_style,
        )
        self.__btn_destroy = Button(
            self,
            image=self.__x_square,
            command=self._destroy,
            **btn_style,
        )
        self.__btn_zoomin = Button(
            self,
            image=self.__zoom_in,
            command=lambda: self._set_btn_command("zoom-in"),
            **btn_style,
        )
        self.__btn_zoomout = Button(
            self,
            image=self.__zoom_out,
            command=lambda: self._set_btn_command("zoom-out"),
            **btn_style,
        )
        self.__btn_scrollup = Button(
            self,
            image=self.__arrow_up,
            command=lambda: self._set_btn_command("scroll-up"),
            **btn_style,
        )
        self.__btn_scrolldown = Button(
            self,
            image=self.__arrow_down,
            command=lambda: self._set_btn_command("scroll-down"),
            **btn_style,
        )

        self.__btn_show.image = self.__eye
        self.__btn_hide.image = self.__eye_slash
        self.__btn_destroy.image = self.__x_square
        self.__btn_zoomin.image = self.__zoom_in
        self.__btn_zoomout.image = self.__zoom_out
        self.__btn_scrollup.image = self.__arrow_up
        self.__btn_scrolldown.image = self.__arrow_down

        self.__btn_hide.grid(row=0, column=0, padx=8, pady=8)
        self.__btn_destroy.grid(row=0, column=1, padx=8, pady=8)
        self.__btn_zoomin.grid(row=1, column=0, columnspan=2, padx=16, pady=16)
        self.__btn_zoomout.grid(row=2, column=0, columnspan=2, padx=16, pady=16)
        self.__btn_scrollup.grid(row=3, column=0, columnspan=2, padx=16, pady=16)
        self.__btn_scrolldown.grid(row=4, column=0, columnspan=2, padx=16, pady=16)
        # self.__btn_show.grid(padx=8, pady=8)

        self.after(1, self._repeat_process)

    def _img(self, *paths):
        path = os.path.join(_DIR, "src", "gui", *paths)
        return ImageTk.PhotoImage(Image.open(path))

    def _repeat_process(self):
        self.__process(
            self._btn_command, self._allow_showing_frame, self._allow_detecting_face
        )
        if self._btn_command is not None:
            self._btn_command = None
        return self.after(1, self._repeat_process)

    def _hide(self):
        self.__btn_hide.grid_forget()
        self.__btn_destroy.grid_forget()
        self.__btn_zoomin.grid_forget()
        self.__btn_zoomout.grid_forget()
        self.__btn_scrollup.grid_forget()
        self.__btn_scrolldown.grid_forget()
        self.__btn_show.grid(padx=8, pady=8)
        cv2.destroyAllWindows()
        self._allow_showing_frame = False
        self._allow_detecting_face = False
        Tk.geometry(self, "140x80-50+50")

    def _show(self):
        self.__btn_show.grid_forget()
        self.__btn_hide.grid(row=0, column=0, padx=8, pady=8)
        self.__btn_destroy.grid(row=0, column=1, padx=8, pady=8)
        self.__btn_zoomin.grid(row=1, column=0, columnspan=2, padx=16, pady=16)
        self.__btn_zoomout.grid(row=2, column=0, columnspan=2, padx=16, pady=16)
        self.__btn_scrollup.grid(row=3, column=0, columnspan=2, padx=16, pady=16)
        self.__btn_scrolldown.grid(row=4, column=0, columnspan=2, padx=16, pady=16)
        self._allow_showing_frame = True
        self._allow_detecting_face = True
        Tk.geometry(self, "140x410-50+50")

    def _destroy(self):
        self.destroy()

    def _set_btn_command(self, command):
        self._btn_command = command


if __name__ == "__main__":

    def func(*args):
        pass

    app = App(func)
    app.wm_attributes("-topmost", 1)
    app.mainloop()
