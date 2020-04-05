import pickle
import wget

def read_pdf_file():
    with open("./pdf_links_dict.pkl", "rb") as f:
        links_file = pickle.load(f)
        return links_file


def download_files(year, url_dict):
    counter = 0
    for k, v in url_dict.items():
        try:
            if counter % 20 == 0:
                print("Finished downloading %d" % counter, flush=True)
            if "http" in v or "https" in v:
                org_url = v
            else:
                org_url = "https://openreview.net" + v
            wget.download(org_url, "./science-parse/input/{}/{}.pdf".format(year, k))
            counter += 1
        except Exception as ex:
            print("Error for id: %s and url: %s" %(k, org_url), flush=True)
            print(ex, flush=True)
    return

links_dict = read_pdf_file()
download_files(2017, links_dict[2017])
