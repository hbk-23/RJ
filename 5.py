import tkinter as tk

def draw_stick_figure(canvas, x, y):
    # 頭部
    canvas.create_oval(x, y, x+50, y+50, outline='black', width=2)
    # 胴体
    canvas.create_line(x+25, y+50, x+25, y+100, fill='black', width=2)
    # 左腕
    canvas.create_line(x+25, y+75, x-25, y+50, fill='black', width=2)
    # 右腕
    canvas.create_line(x+25, y+75, x+75, y+50, fill='black', width=2)
    # 左足
    canvas.create_line(x+25, y+100, x-25, y+150, fill='black', width=2)
    # 右足
    canvas.create_line(x+25, y+100, x+75, y+150, fill='black', width=2)

# ウィンドウの作成
window = tk.Tk()

# キャンバスの作成
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# 棒人間の描画
draw_stick_figure(canvas, 150, 100)
canvas.move()

# ウィンドウのメインループ
window.mainloop()
