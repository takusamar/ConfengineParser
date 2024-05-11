import sys
import json

if __name__=="__main__":
  if len(sys.argv) < 3:
    print("Usage: python ParseProposal.py <idlist> <json_dir>", file=sys.stderr)
    sys.exit(-1)

  idlist = sys.argv[1]
  json_dir = sys.argv[2]

  merged_data = []
  # マージする元のJSONファイルのリスト
  with open(idlist, 'r') as f:
    for id in f.readlines():
      # 各JSONファイルからデータを読み込んでマージする
      filename = "{}/{}.json".format(json_dir, id.strip())
      with open(filename, 'r') as f:
        data = json.load(f)
        merged_data.append(data)

  print(json.dumps(merged_data, ensure_ascii=False))
