import wget
url = 'https://pjreddie.com/media/files/yolov3.weights'
yolov3 = wget.download(url, out='yolov3.weights')
