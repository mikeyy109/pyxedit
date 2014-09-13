'''
Author: Mike Clarke 13/09/14
'''

import Tkinter as tk
import ScrolledText

main = tk.Tk(className="Pyxedit")
text_area = ScrolledText.ScrolledText(main, width=100, height=80)
text_area.pack()
main.mainloop()
