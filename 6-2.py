import zipfile
import json
import tkinter as tk

class Shoulder:
    def __init__(self, canvas, zip_ref, file):
        self.canvas = canvas
        self.zip_ref = zip_ref
        self.file = file
        self.RS_x_1 = 0
        self.RS_y_1 = 0
        self.LS_x_1 = 0
        self.LS_y_1 = 0
        self.RS_x_2 = 0
        self.RS_y_2 = 0
        self.LS_x_2 = 0
        self.LS_y_2 = 0
    
    def shoulder_value(self):
        with self.zip_ref.open(self.file, "r") as f:
            data = json.load(f)
        people1 = data["people"][0]["pose_keypoints_2d"]
        people2 = data["people"][1]["pose_keypoints_2d"]
        self.RS_x_1 = people1[6]
        self.RS_y_1 = people1[7]
        self.LS_x_1 = people1[15]
        self.LS_y_1 = people1[16]
        self.RS_x_2 = people2[6]
        self.RS_y_2 = people2[7]
        self.LS_x_2 = people2[15]
        self.LS_y_2 = people2[16]


    def draw_stick(self):
        self.canvas.create_line(self.RS_x_1, self.RS_y_1, self.LS_x_1, self.LS_y_1, fill='black', width=2)
        self.canvas.create_line(self.RS_x_2, self.RS_y_2, self.LS_x_2, self.LS_y_2, fill='black', width=2)
    
# ウィンドウの作成
window = tk.Tk()

# キャンバスの作成
canvas = tk.Canvas(window, width=2000, height=2000)
canvas.pack()

# ZIPファイルを展開
with zipfile.ZipFile("kabeposter.zip", 'r') as zip_ref:
    # ZIPファイル内のファイルを取得
    file_list = zip_ref.namelist()

    # 各ファイルに対して処理
    for file_name in file_list:
        # ファイル名から数字部分を抽出
        number = int(file_name.split('_')[1])
        if number == 0:
            people1 = Shoulder(canvas, zip_ref, file_name)
            people1.shoulder_value()
            people1.draw_stick()
            break

# ウィンドウのメインループ
window.mainloop()

