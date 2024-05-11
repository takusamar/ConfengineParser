import json
import sys
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

driver = webdriver.Chrome() 


def getProposal(url, id):
  proposal_url = "{}/proposal/{}".format(url, id)
  driver.get(proposal_url)
  wait = WebDriverWait(driver, 5)

  soup = BeautifulSoup(driver.page_source, 'html.parser')
  content = soup.select_one("div.content")
  header = content.select_one("div.proposal-header")
  proposal = content.select_one("div.proposal")

  title = header.select_one("h4").text
  tags = header.select_one("div.tags-holder")
  votes = tags.select_one("span.just-points-count").text
  theme = tags.select_one("a.tags.theme").text
  city = tags.select_one('a.tags[data-search-qualifier="City"]').text
  talk_type = tags.select_one('a.tags[data-search-qualifier="Type"]').text
  duration = tags.select_one('a.tags[data-search-qualifier="Duration"]').text
  level = tags.select_one('a.tags[data-search-qualifier="Level"]').text

  speaker_divs = proposal.select("div.bold.truncate")
  speakers = [d.text for d in speaker_divs]

  data = {
    "id": id,
    'speaker': " / ".join(speakers),
    'title': title,
    'theme': theme,
    'type': talk_type,
    'duration': duration,
    'level': level,
    'city': city,
    'vote': votes,
    'url': proposal_url,
  }
  return data


if __name__=="__main__":
  if len(sys.argv) < 3:
    print("Usage: python ParseProposal.py <Confengine URL> <proposal_id>", file=sys.stderr)
    sys.exit(-1)

  url = sys.argv[1]
  id = sys.argv[2]

  try:
    result = getProposal(url, id)
    print(json.dumps(result, ensure_ascii=False))
  except ValueError as e:
    print(e, file=sys.stderr)
    sys.exit(-1)
