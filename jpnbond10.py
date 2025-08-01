#! /usr/bin/env python3

# 日本国債10年もの金利
# NOTE: requestsの簡単な使い方としては妥当ではない
# CSVをiteratorオブジェクトとして扱うので、基本的なCSV操作を紹介するには妥当でない

# ダウンロードする方針でいこう

import csv
from pathlib import Path

import requests


# 変数設定
FILE_NAME = 'jpnbond10.csv'

# 財務省の金利情報（CSV）を取得
URL = 'https://www.mof.go.jp/jgbs/reference/interest_rate/jgbcm.csv'


res = requests.get(URL)
res.encoding = 'Shift_JIS'
res.raise_for_status()


# 実行ファイルと同階層にCSVファイルを保存
path = Path(__file__)
csv_downloaded = path.parent.resolve() / FILE_NAME

downloaded = open(csv_downloaded, 'w', encoding='UTF-8')
downloaded.write(res.text)
downloaded.close()

# CSVデータとして開く
with open(csv_downloaded, newline='', encoding='UTF-8') as csvfile:

    # , delimiter=',', quotechar='"'
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)

    # データを列挙
    for enum in enumerate(data):
        # 0番目コラムの値が空文字だったら
        # 1つ前の行（有効なデータの最終行）を選択
        cur_row = enum[1]
        if cur_row[0] == '':
            last_row = data[enum[0] - 1]
            break

    # 最終行を出力
    print(f'日本国債10年もの金利 {last_row[0]} {last_row[10]}')
