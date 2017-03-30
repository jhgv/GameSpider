class Spider:

    def __init__(self, limit, host):
        self.limit = limit
        self.host = host

    def get_limit(self):
        return self.limit

    def get_host(self):
        return self.host

    def run(self, max_pages=None):
        


    # def search(self):
    #     base = "http://xkcd.com/"
    #     for page in range(1, max_pages + 1):
    #         url = base + str(page)
    #         source_code = requests.get(url)
    #         plain_text = source_code.text
    #         soup = BeautifulSoup(plain_text, "html.parser")
    #         # we only want one image
    #         img = soup.select_one("#comic img") # or .find('div',id= 'comic').img
    #         download_img(img["src"], base)
