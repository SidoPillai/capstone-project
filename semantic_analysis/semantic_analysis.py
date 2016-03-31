from requests import get
import json
import csv


sts_link = "http://swoogle.umbc.edu/SimService/GetSimilarity"

# lists for storing captions
original_image = []
bright_light_image = []
complement_image = []
gauss_image = []
low_light_image = []

# lists to store the scores based on sementic similarity
bright_light_image_score = []
complement_image_score = []
gauss_image_score = []
low_light_image_score = []


########################
# Order of captions
# 1. Original Image
# 2. Bright Light Image
# 3. Complement Image
# 4. Gauss Image
# 5. Low Light Image
########################


# Generates the similarity cosine score
def semantic_textual_similarity(s1, s2, type='relation', corpus='webbase'):
    try:
        response = get(sts_link, params={'operation':'api','phrase1':s1,'phrase2':s2,'type':type,'corpus':corpus})
        return float(response.text.strip())
    except:
        print('Error in getting similarity for %s: %s' % ((s1,s2), response))
        return 0.0


# Retieve the captions from the json file
# adds to the list to compute the score
def retrieve_all_captions():

    with open("vis.json") as json_file:
        json_data = json.load(json_file)
        # print(json_data)
        # print(type(json_data))

        for item in json_data:
            # print(item)
            # print(type(item))
            val = int(item.get("image_id"))

            mod_val = (val-1) % 5
            caption_val = item.get("caption")
            # print(caption_val)

            if mod_val == 0:
                original_image.append(caption_val)

            elif mod_val == 1:
                bright_light_image.append(caption_val)

            elif mod_val == 2:
                complement_image.append(caption_val)

            elif mod_val == 3:
                gauss_image.append(caption_val)

            else:
                low_light_image.append(caption_val)

    compute_scores()


# Computes the Similarity Index
def compute_scores():

    for i in range(0,len(original_image)):
        bright_score = float(semantic_textual_similarity(original_image[i],bright_light_image[i]))
        complement_score = float(semantic_textual_similarity(original_image[i],complement_image[i]))
        gauss_score = float(semantic_textual_similarity(original_image[i],gauss_image[i]))
        low_score = float(semantic_textual_similarity(original_image[i],low_light_image[i]))

        print(bright_score)
        print(complement_score)
        print(gauss_score)
        print(low_score)

        bright_light_image_score.append(bright_score)
        complement_image_score.append(complement_score)
        gauss_image_score.append(gauss_score)
        low_light_image_score.append(low_score)

    write_list_to_file()


# Building the data to write on the file
def build_data():
    data = []

    for i in range(0,len(bright_light_image_score)):
        l = []
        l.append(bright_light_image_score[i])
        l.append(complement_image_score[i])
        l.append(gauss_image_score[i])
        l.append(low_light_image_score[i])
        data.append(l)
    return data


# Writes the data to the csv file
def write_list_to_file():
    data = build_data()
    print(data)

    with open('myfile.csv','w') as f:
        for sublist in data:
            for item in sublist:
                f.write(str(item) + ',')
            f.write('\n')

    # with open('scores.csv', 'a') as out_csv:
    #     # configure writer to write standard csv file
    #     writer = csv.writer(out_csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    #     writer.writerow(['bright', 'complement', 'gauss', 'low'])
    #
    #     for item in range(0,len(data)):
    #         # write item to out_csv
    #         writer.writerow(data[item])


retrieve_all_captions()