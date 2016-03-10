from PIL import Image
import os


# Returns the list of files in the directory including the path
def list_files(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(path+"/"+name)
    return files

# Predefined image size properties
sizes = [(120,120), (720,720), (1600,1600)]

# Path to the directory where the files are stored
files = list_files("/Users/siddeshpillai/PycharmProjects/imageresize/images")

# Perform the image resizing operation
for image in files:
    for size in sizes:
        try:
            img = Image.open(image)
            if img is not None:
                img.thumbnail(size)
                img.save("%s_%s" % (os.path.basename(image).split('.',1)[0], "_" + str(size[0])) + ".jpg", "JPEG")
        except Exception as e:
            print(e)
