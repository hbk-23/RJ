import zipfile

# ZIPファイルのパス

# 合計値の初期化
total_sum = 0

# ZIPファイルを展開
with zipfile.ZipFile("sample.zip", 'r') as zip_ref:
    # ZIPファイル内のファイルを取得
    file_list = zip_ref.namelist()
    
    # 各ファイルに対して処理
    for file_name in file_list:
        try:
            # ファイル名から数字部分を抽出
            number = int(file_name.split('_')[1])
            
            # 奇数のファイルのみ処理
            if number % 2 != 0:
                # ファイルを展開し、数字を読み取る
                with zip_ref.open(file_name, 'r') as file:
                    file_contents = file.read().decode('utf-8')
                    file_number = int(file_contents.strip())
                    
                    # 合計値に加算
                    total_sum += file_number
        except:
            continue

# 結果を出力
print("合計:", total_sum)
