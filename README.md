# ConfengineParser

Confengine のデータを抽出するツール

## ParseProposals

プロポーザルの概要を一覧にして出力します。

### 必要なもの

- bash
- python3
- Chrome ブラウザ

### 準備

```
$ cd ParseProposals
$ pip install -r requirements.txt
```

### 使い方

```
$ ./run.sh <confengine URL>
```

（例）

```
$ ./run.sh https://confengine.com/conferences/scrum-fest-osaka-2024
```

実行すると、output フォルダが作成されて、結果が output/proposals.json として出力されます。

あとは、json を整形するなり、CSV 形式に変換するなり、お好きにどうぞ。

#### json を整形して出力（Mac の場合）

```
$ brew install jq
$ jq < output/proposals.json
```

#### CSV 形式に変換（Mac の場合）

```
$ brew install csvkit
$ in2csv output/proposals.json > output/proposals.csv
```

### 備考

- Confengine のプロポーザル一覧ページは全件を読み込めないので、Activity ページからプロポーザルの ID を取得して、各プロポーザルの詳細ページを取得する実装としている。

- Confengine の Web サイトに何度もアクセスするため、負荷をかけないよう wait を長めに入れています。プロポーザルの件数が多いと実行時間はかかりますが気長に待ってください。
