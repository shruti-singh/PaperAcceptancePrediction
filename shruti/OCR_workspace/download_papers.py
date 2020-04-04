import pickle
import wget

def read_pdf_file():
    with open("./pdf_links_dict.pkl", "rb") as f:
        links_file = pickle.load(f)
        return links_file


def download_files(year, url_dict):
    for k, v in url_dict.items():
        org_url = "https://openreview.net" + v
        wget.download(org_url, "./science-parse/input/{}/{}.pdf".format(year, k))
        #break
        return

links_dict = read_pdf_file()
download_files(2017, links_dict[2017])