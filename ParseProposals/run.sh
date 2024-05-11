#!/bin/bash

URL=${1}
IDLIST="output/idlist"

mkdir output

# プロポーザルのID一覧作成
echo "list proposals..."
python ./ListProposals.py ${URL} > ${IDLIST}

# プロポーザルを1つずつ処理
while IFS= read -r ID; do
  echo "parse proposal: ${ID} ..."
  python ./ParseProposal.py ${URL} ${ID} > output/${ID}.json
done < ${IDLIST}

# jsonをマージする
echo "merge result"
python ./MergeJson.py ${IDLIST} output > output/proposals.json

echo "done."
