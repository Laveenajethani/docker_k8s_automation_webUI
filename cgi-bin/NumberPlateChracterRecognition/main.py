import cgi
import cv2

form = cgi.FieldStorage()
image = form.getvalue("FU_Photo")

def get_number(image):
    img_gray = cv2.imread(image,0)

    #load HAAR cascade
    model = cv2.CascadeClassifier("indian_license_plate.xml")
    #img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    model_output = model.detectMultiScale(img_gray, 1.3, 7)

    for (x,y,w,h) in model_output:
        final_plate = img_gray[y:y+h, x:x+w]

    cv2.imwrite("num_plate.jpg", final_plate)
    
    
    
    import boto3
    file = "num_plate.jpg"
    region = "ap-south-1"
    bucket = "numberplatbucket"
    s3 = boto3.resource("s3")
    # a6.jpg = file_name & test = keyname
    s3.Bucket(bucket).upload_file(file,"test")
    
    
    
    # Textract = managed service of AWS for recognization from image/Documnet
    # Connecting to textract
    textract = boto3.client("textract", region_name = region)
    response = textract.detect_document_text(
          Document = {
            "S3Object" : {
              "Bucket" : bucket,
              "Name" : "test"
             }
         }
    )
    number = response["Blocks"][1]["Text"].replace(" ", "")
    print("Plate Number Is : ",number)

#Image which is stored in your computer 
get_number("Cars/cars.jpg")

  


