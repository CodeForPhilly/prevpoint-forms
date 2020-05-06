import requests
import keys

sub_images_path = "images/sub_images/"

subscription_key = keys.COMPUTER_VISION_SUBSCRIPTION_KEY
endpoint = keys.COMPUTER_VISION_ENDPOINT

#api url
text_recognition_url = endpoint + "vision/v3.0-preview/read/analyze"

# Set the langauge that you want to recognize. The value can be "en" for English, and "es" for Spanish
language = "en"

headers = {'Ocp-Apim-Subscription-Key': subscription_key,
          "Content-Type": "application/octet-stream"} 

def call_read(sub_images):    
    
    #initialize dictionary
    returned_data = {}
    
    #loop through sub images and call api
    for sub_image in sub_images:
        #intialize dictionary
        returned_data[sub_image] = {}

        image_path = sub_images_path + sub_image + ".jpeg"
        image_data = open(image_path, "rb").read()

        #call api
        response = requests.post(
            text_recognition_url, headers=headers,params={'language': language}, data=image_data)
        response.raise_for_status()

        # Extracting text requires two API calls: One call to submit the
        # image for processing, the other to retrieve the text found in the image.

        # Holds the URI used to retrieve the recognized text.
        operation_url = response.headers["Operation-Location"]

        # The recognized text isn't immediately available, so poll to wait for completion.
        analysis = {}
        poll = True
        while (poll):
            response_final = requests.get(
                response.headers["Operation-Location"], headers=headers)
            analysis = response_final.json()

            #time.sleep(1)
            if ("analyzeResult" in analysis):
                poll = False
            if ("status" in analysis and analysis['status'] == 'failed'):
                poll = False
                
        #extract text and confidence from the returned api call        
        lines = analysis["analyzeResult"]['readResults'][0]['lines']
        text = ""
        for line in lines:
            if text == "":
                text = line["text"]
            else:
                text = text + " " + line["text"]

            for i,word in enumerate(line["words"]):
                returned_data[sub_image]["confidence_"+ str(i)] = word["confidence"]

        returned_data[sub_image]["text"] = text
        
    return returned_data