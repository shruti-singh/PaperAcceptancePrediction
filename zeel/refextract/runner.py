import refextract
import sys
from glob import glob
import logging
import pickle
from tika import parser
import os
sys.stdout.write('started')
i = sys.argv[1]
ii = sys.argv[2]
year = sys.argv[3]

path = '/content/drive/My Drive/Colab Notebooks/ML Project/'

if os.path.exists(path+'tmp/'+i+'-'+ii+'.pickle'):
  sys.exit()

logging.basicConfig(level=logging.INFO)

fnames = sorted(glob(path+'data/papers/'+year+'/*.pdf'))
#print('started')
glob_dict = {}

count = 0
for fname in fnames[int(i):int(ii)]:
  sys.stdout.write(str(count))
  try:
    raw = parser.from_file(fname)
  except OSError:
    logging.info(fname+' OSerror')
    count += 1
    continue
  try:
    glob_dict.update({fname.split('/')[-1]:refextract.extract_references_from_string(raw['content'], is_only_references=False)})
  except AttributeError:
    logging.info(fname+ 'ATTRerror')
  count += 1

with open(path+'tmp/'+i+'-'+ii+'.pickle','wb') as f:
  pickle.dump(glob_dict, f)