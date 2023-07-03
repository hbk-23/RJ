import zipfile
import json
import tkinter as tk

class Parts:
    def __init__(self, canvas, zip_ref, file, number):
        self.canvas = canvas
        self.zip_ref = zip_ref
        self.file = file
        self.number = number
        self.x = 0
        self.y = 0
    

    def parts_value(self, parts):
        x_number = parts*3
        y_number = x_number+1
        with self.zip_ref.open(self.file, "r") as f:
            data = json.load(f)
        people1 = data["people"][self.number]["pose_keypoints_2d"]
        self.x = people1[x_number]
        self.y = people1[y_number]

        return self.x, self.y


class joint_parts:
    def __init__(self, file, array):
        self.file = file
        self.array = array
    
    def joint(self):
        with open(self.file, "r") as f:
            for line in f.readlines():  # 行を読み込んでfor文で回す
                try:
                    num = line.split(',')
                    Parts
                except ValueError as e:
                    print(e, file=sys.stderr)  # エラーが出たら画面に出力
                    continue




def draw_stick(self):
    self.canvas.create_line(self.RS_x_1, self.RS_y_1, self.LS_x_1, self.LS_y_1, fill='black', width=2)
    self.canvas.create_line(self.RS_x_2, self.RS_y_2, self.LS_x_2, self.LS_y_2, fill='black', width=2)
    
# ウィンドウの作成
window = tk.Tk()

# キャンバスの作成
canvas = tk.Canvas(window, width=2000, height=2000)
canvas.pack()

# ZIPファイルを展開
with zipfile.ZipFile("C:/Users/hibiki/Documents/Seminar/RJ/Python/2023/RJ/kabeposter.zip", 'r') as zip_ref:
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

