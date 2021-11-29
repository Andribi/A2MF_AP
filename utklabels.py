import os
import json

'''
This script generates a json file with the labels for the utkface dataset.

The labels of each face image is embedded in the file name, formated like [age]_[gender]_[race]_[date&time].jpg

[age] is an integer from 0 to 116, indicating the age
[gender] is either 0 (male) or 1 (female)
[race] is an integer from 0 to 4, denoting White, Black, Asian, Indian, and Others (like Hispanic, Latino, Middle Eastern).
[date&time] is in the format of yyyymmddHHMMSSFFF, showing the date and time an image was collected to UTKFace

source: https://susanqq.github.io/UTKFace/
'''


UTK_face = 'UTKFace'
res = {}
feat_names = ['age', 'gender', 'race']

for pic in os.listdir(UTK_face):
    features = pic.split('_')[:-1]
    features_dict = {}
    print(features)
    for i in range(len(features)):

        features_dict[feat_names[i]] = int(features[i])
    res[pic] = features_dict


#with open('utkface.json', 'w') as outfile:
#    json.dump(res, outfile)

