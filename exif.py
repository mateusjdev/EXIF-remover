from PIL import Image, ExifTags
import os
#exif remove dir list
print("Initiating exif data removing sequence...\n")
relevant_path = os.getcwd()
extenstions = ['jpg','jpeg']
listfiles = [files for files in os.listdir(relevant_path) if any(files.endswith(ext) for ext in extenstions)]
#inbuilt function
#content = filter(lambda x: not x.startswith('ex_'), listfiles)
newlist = [x for x in listfiles if not x.startswith('ex_')]
if len(newlist) == 0:
    os.system('cls')
    print("Error! Either Exif data is already removed or No jpg/png files found")
for image_file in newlist:
    image = Image.open(image_file)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break
    pre_exif = image.getexif()
    if pre_exif is not None:
        exif = dict(pre_exif.items())
        if len(exif) is not 0:
            if orientation in exif:
                exif_or = exif[orientation]
                if exif_or == 3:
                    image_without_exif = image_without_exif.rotate(180, expand=True)
                elif exif_or == 6:
                    image_without_exif = image_without_exif.rotate(270, expand=True)
                elif exif_or == 8:
                    image_without_exif = image_without_exif.rotate(90, expand=True)
    directory = os.getcwd()
    image_without_exif.save(directory + "/ex_" + image_file)
    print("(Removed) Saved as .\ex_" + image_file)
    delete = os.remove(image_file)
