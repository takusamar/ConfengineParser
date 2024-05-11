import sys
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

driver = webdriver.Chrome() 


def listProposals(url):
  # Proposalページからは全件を取得できないので、
  # ActivityページからプロポーザルのIDを取得する
  activity_url = url + "/activity"
  driver.get(activity_url)
  wait = WebDriverWait(driver, 5)

  soup = BeautifulSoup(driver.page_source, 'html.parser')
  a_tags = soup.select('a')
  hrefs = [ a.get('href') for a in a_tags if a.get('href') is not None]

  # プロポーザルIDを取得
  ids = []
  proposal_url = "{}/proposal/".format(url)
  url_pattern = r"{}(\d+)$".format(proposal_url)
  for href in hrefs:
    match = re.search(url_pattern, href)
    if match:
      id = match.group(1)
      ids.append(id)

  # 重複排除して昇順で返す
  return  sorted(set(ids))


if __name__=="__main__":
  if len(sys.argv) < 2:
    print("Usage: python ListProposals.py <Confengine URL>", file=sys.stderr)
    sys.exit(-1)

  url = sys.argv[1]

  try:
    ids = listProposals(url)
    for id in ids:
      print(id)
  except ValueError as e:
    print(e, file=sys.stderr)
    sys.exit(-1)
