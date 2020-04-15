import requests
from bs4 import BeautifulSoup




def read_csv_to_list():
    pass

    return None


def check_stock(soup):
    is_soldout = soup.findAll("div", {"class":{"soldOutBlock"}})
    if is_soldout:
        return "在庫ありません"
    else:
        return "在庫あるかも！！！"


def get_item_info(url):
    r = requests.get(url)
    print(r.status_code)
    # html_doc = .text
    # print(html_doc.)
    # soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
    # item_title = soup.select("h1.productTitle.wrongInformationModalTarget-name")[0].text.strip()
    # item_price = soup.select("p.priceNum span.num")[0].text.strip()
    # item_price_with_tax = soup.select("p.priceNum span.tax")[0].text.strip()

    # print(item_title)
    # print(item_price)
    # print(item_price_with_tax)
    # print(check_stock(soup))

    return None


if __name__ == "__main__":
    # url = "https://www.askul.co.jp/p/5784271/"
    # url = "https://www.askul.co.jp/p/095499/"
    url = "https://www.irisplaza.co.jp/index.php?KB=SHOSAI&SID=7600600"
    res = get_item_info(url)

    # print(res.text)




# print(soup.prettify())

# # TODO1 このページのaタグをすべて抜き出してください。(HTMLの内容)
# real_page_tags = soup.find_all("a")
# for tag in real_page_tags:
# print(tag)

# # TODO2 このページのaタグをすべて抜き出してください。(HTMLの内容)

# for tag in real_page_tags:
# print(tag.string)
# # TODO3 このページのaタグをすべて抜き出してください。(HTMLの内容)

# for tag in real_page_tags:
# print(tag.get("href"))