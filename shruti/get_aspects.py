from glob import glob
import numpy as np
import json
import pickle


data_dir = "/home/singh_shruti/workspace/PeerRead/data/iclr_2017/[a-z]*/reviews/*.json"

file_list = glob(data_dir)
print(len(file_list))

review_jsons = {}

for f in file_list:
    d = json.load(open(f))
    if "id" in d:
        review_jsons[d["id"]] = d

with open("reviewratings_iclr17_peeread.pkl", "wb") as f:
    pickle.dump(review_jsons, f)
