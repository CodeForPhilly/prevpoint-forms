from PIL import Image

def create_sub_images(image_path, sub_image_path, sub_image_dict):
    #current form to scan
    img = Image.open(image_path)

    #crop all sub images
    for sub_image in sub_image_dict.keys():
        #create name to save sub image under
        sub_image_name = str(sub_image) + ".jpeg"
        #create bounding box
        bounding_box = (sub_image_dict[sub_image]["origin"]["x"], 
                        sub_image_dict[sub_image]["origin"]["y"],
                        sub_image_dict[sub_image]["origin"]["x"] + sub_image_dict[sub_image]["size"]["width"],
                        sub_image_dict[sub_image]["origin"]["y"] + sub_images_dict[sub_image]["size"]["height"])
        #crop the image
        temp_img = img.crop(bounding_box)
        #save the image
        temp_img.save(sub_image_path + sub_image_name)