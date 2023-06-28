import zipfile
import json

def nose_value(zip_ref, file):
    with zip_ref.open(file, "r") as f:
        data = json.load(f)
    people1 = data["people"][0]["pose_keypoints_2d"]
    people2 = data["people"][1]["pose_keypoints_2d"]
    point1 = people1[0:3]
    point2 = people2[0:3]

    return point1, point2



# ZIPファイルを展開
with zipfile.ZipFile("C:/Users/hibiki/Documents/Seminar/RJ/Python/2023/RJ/kabeposter.zip", 'r') as zip_ref:
    # ZIPファイル内のファイルを取得
    file_list = zip_ref.namelist()

    # 各ファイルに対して処理
    for file_name in file_list:
        # ファイル名から数字部分を抽出
        number = int(file_name.split('_')[1])
        if number == 0:
            people1, people2 = nose_value(zip_ref, file_name)
            break
        
print(people1, people2)