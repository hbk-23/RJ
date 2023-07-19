import zipfile
import json
import tkinter as tk

class Parts:
    def __init__(self, canvas, zip_ref, file, number, body_1, body_2, size):
        self.canvas = canvas
        self.zip_ref = zip_ref
        self.file = file
        self.number = number
        self.body_1 = body_1
        self.body_2 = body_2
        self.x_1 = 0
        self.y_1 = 0
        self.x_2 = 0
        self.y_2 = 0
        self.size = size
    
    def value(self):
        x_number_1 = self.body_1*3
        y_number_1 = x_number_1+1
        x_number_2 = self.body_2*3
        y_number_2 = x_number_2+1
        with self.zip_ref.open(self.file, "r") as f:
            data = json.load(f)
        people1 = data["people"][self.number]["pose_keypoints_2d"]
        self.x_1 = people1[x_number_1]
        self.y_1 = people1[y_number_1]
        self.x_2 = people1[x_number_2]
        self.y_2 = people1[y_number_2]


    def draw_stick(self):
        if self.x_1 != 0 and self.y_1 != 0 and self.x_2 != 0 and self.y_2 != 0:
            self.canvas.create_line(self.x_1*self.size, self.y_1*self.size, self.x_2*self.size, self.y_2*self.size, fill='black', width=2)

def draw():
    canvas.delete("all")
    for i in range(24):
        people1 = Parts(canvas, zip_ref, file_name, 0, joint[i][0], joint[i][1], 1/2)
        people1.value()
        people1.draw_stick()
        people2 = Parts(canvas, zip_ref, file_name, 1, joint[i][0], joint[i][1], 1/2)
        people2.value()
        people2.draw_stick()


joint=[]
path = 'bind_dic.txt'
with open(path, 'r') as fin: # ファイルを開く
    for line in fin:  # 行を読み込んでfor文で回す
        line = line.strip()
        # カンマで分割して値を取得し、整数型に変換して配列に追加する
        values = [int(x) for x in line.split(',')]
    
        joint.append(values)    

# ウィンドウの作成
window = tk.Tk()

# キャンバスの作成
canvas = tk.Canvas(window, width=1500, height=700)
canvas.pack()

# ZIPファイルを展開
with zipfile.ZipFile("kabeposter.zip", 'r') as zip_ref:
    # ZIPファイル内のファイルを取得
    file_list = zip_ref.namelist()

    # 各ファイルに対して処理
    for file_name in file_list:
        # ファイル名から数字部分を抽出
        number = int(file_name.split('_')[1])
        for j in range(number):
            draw()
            window.update()
            

# ウィンドウのメインループ
window.mainloop()

