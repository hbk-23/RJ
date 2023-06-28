import sys

def sum(number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    return sum

nums = []  # 整数を入れるリスト

with open('C:/Users/hibiki/Documents/Seminar/RJ/Python/2023/RJ/data.txt', 'r') as fin:  # ファイルを開く
    for line in fin.readlines():  # 行を読み込んでfor文で回す
        line = line.strip()
        if line:
            try:
                num = int(line)  # 行を整数（int）に変換する
                nums.append(num)  # 変換した整数をリストに保存する
            except ValueError as e:
                print(e, file=sys.stderr)  # エラーが出たら画面に出力
                continue

y = sum(nums)
print(y)