import cv2
import numpy as np 
import matplotlib.pyplot as plt
import utlis 

img = cv2.imread(r"c:\OPTICAL_MARKS_RECOGNITION\test.jpg")

widthImg = 700 
heightImg = 700 
questions=5
choices = 5 
ans = [1,2,0,1,4]

img = cv2.resize(img, (widthImg, heightImg))
imgContour = img.copy()
imgBiggestContour = img.copy()
imgFinal = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
imgCanny = cv2.Canny(imgBlur, 10, 50)

countours , hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContour, countours, -1, (0,255,0), 10)
rectCon = utlis.rectCountour(countours)
biggestContour = utlis.getCornerPoints(rectCon[0])
print(biggestContour)
gradePoints = utlis.getCornerPoints(rectCon[1])
print(gradePoints)

if biggestContour.size!=0 and gradePoints.size!=0:
    cv2.drawContours(imgBiggestContour, biggestContour, -1, (255,0,0), 20)
    cv2.drawContours(imgBiggestContour, gradePoints, -1, (0,0,255), 20)
    biggestContour = utlis.reorder(biggestContour)
    gradePoints = utlis.reorder(gradePoints)
    
    pt1 = np.float32(biggestContour)
    pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix = cv2.getPerspectiveTransform(pt1, pt2)
    imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    
    ptG1 = np.float32(gradePoints)
    ptG2 = np.float32([[0,0],[325,0],[0,150],[325 , 150]])
    matrixG = cv2.getPerspectiveTransform(ptG1, ptG2)
    imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150))
    
    
    imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.threshold(imgWarpGray, 180, 255, cv2.THRESH_BINARY_INV)[1]
    
    boxes=utlis.splitBoxes(imgThresh)
    #print(cv2.countNonZero(boxes[1]) , cv2.countNonZero(boxes[2]))
    
    myPixelVal = np.zeros((questions, choices))
    countC = 0
    countR=0
    
    for image in boxes:
        totalPixels = cv2.countNonZero(image)
        myPixelVal[countR][countC]= totalPixels
        countC +=1
        if (countC==choices):countC=0; countR+=1
        
    print(myPixelVal)
    
    myIndex = []
    for x in range (0, questions):
        arr = myPixelVal[x]
        myIndexVal = np.where(arr == np.amax(arr))
        myIndex.append(myIndexVal[0][0])
        
    print(myIndex)
    
    grading = []
    for x in range (0, questions):
        if myIndex[x] == ans[x]:
            grading.append(1)
        else:
            grading.append(0)
    
    print(grading)
    score = (sum(grading)/questions)*100
    print(score)
    
    
    imgResult = imgWarpColored.copy()
    imgResult = utlis.showAnswers(imgResult , myIndex , grading , ans , questions , choices)
    imRawDrawings = np.zeros_like(imgWarpColored)
    imRawDrawings = utlis.showAnswers(imRawDrawings , myIndex , grading , ans , questions , choices)
    invMatrix = cv2.getPerspectiveTransform(pt2, pt1)
    imgInvWarp = cv2.warpPerspective(imRawDrawings, invMatrix, (widthImg, heightImg))
    
    imgRawGrade=np.zeros_like(imgGradeDisplay)
    cv2.putText(imgRawGrade, str(int(score))+"%", (60,100), cv2.FONT_HERSHEY_COMPLEX ,3 , (0,255,0) , 3)
    invMatrixG = cv2.getPerspectiveTransform(ptG2, ptG1)
    imgInvGradeDisplay = cv2.warpPerspective(imgRawGrade, invMatrixG, (widthImg, heightImg))
    
    imgFinal = cv2.addWeighted(imgFinal, 1, imgInvWarp, 1, 0)
    imgFinal = cv2.addWeighted(imgFinal, 1, imgInvGradeDisplay, 1, 0)
   
    
    
    


plt.imshow(imgFinal)
plt.title("Final Image")
plt.axis('off')
plt.show()


