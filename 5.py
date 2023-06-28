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

def move_stick_figure():
    global x_position
    canvas.delete("all")  # キャンバス上の描画を全て削除
    x_position += 5  # 移動量を指定
    draw_stick_figure(canvas, x_position, 100)
    window.update()  # ウィンドウの状態を更新
    # 移動を続けるための条件
    if x_position < 350:
        window.after(100, move_stick_figure)

# ウィンドウの作成
window = tk.Tk()

# キャンバスの作成
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# 棒人間の描画
x_position = 150
draw_stick_figure(canvas, x_position, 100)

# 棒人間の移動
move_stick_figure()

# ウィンドウのメインループ
window.mainloop()
