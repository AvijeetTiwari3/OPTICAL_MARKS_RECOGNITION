# Automated MCQ Grading System

This project is an end-to-end Optical Mark Recognition (OMR) system built using Python + OpenCV.  
It reads an OMR answer sheet image, detects the filled bubbles, compares them with the answer key,  
and produces the final score along with a fully annotated result sheet.

This system replicates the logic used in online test evaluation systems and can be adapted for schools, coaching centers, and automated exam-checking platforms.



# Features

- Automatic Sheet Detection  
  Detects the answer sheet using contour detection & perspective transform.

- Bubble Recognition  
  Splits the sheet into questions × choices grid and detects filled bubbles using pixel intensity.

- Answer Evaluation  
  Compares detected answers with the provided key → generates grading array → final score.

- Result Visualization  
  Draws correct (🟢), incorrect (🔴), and selected options directly on the sheet.

- Final Annotated Output  
  Produces a clean result sheet showing score and evaluation in a single image.



#  Tech Stack

 Component | Libraries 

1. Image Processing | OpenCV 
2. Numerical Computation | NumPy 
3. Visualization | Matplotlib 
4. Utility Functions | Custom utlis.py

# Project Structure 

OPTICAL_MARKS_RECOGNITION/
│
├── OMR.py                   # Main script (OMR detection + grading)
├── utlis.py                 # Helper functions (contours, reorder, bubble split, draw)
├── test.jpg                 # Sample OMR sheet image
├── requirements.txt         # Project dependencies
│
├── pycache/                 # Auto-generated python cache files
│
└── README.md                # Project documentation

# Workflow of the Project 

1. The input OMR sheet image is read and preprocessed (grayscale → blur → edges).

2. The outer answer-sheet box is detected using contours and then warp-transform is applied
   to get a clean top-view of the sheet.

3. The sheet is divided into a grid of (questions × choices).  
   Each bubble area is isolated.

4. Pixel intensity is counted in each bubble.  
   The darkest/highest pixel count = selected option.

5. Selected options are compared with the answer key to calculate the score.

6. Finally, the sheet is annotated with correct/incorrect marks and displayed as output.

# Running the Project 

1. Clone the repository

2. Install Dependencies :
   pip install -r requirements.txt

3. Update your test image path

4. Run the OMR.py file


# Output of the project 

![image alt](https://github.com/AvijeetTiwari3/OPTICAL_MARKS_RECOGNITION/blob/main/Screenshot%202025-11-21%20144947.png?raw=true)


# Future Improvements 

- Handle uneven lighting and tilted OMR sheets more accurately
  
- Add support for larger exams (50–200 questions) with dynamic layouts
    
- Build a Streamlit web app for easy uploading and instant grading
   
- Improve bubble detection accuracy using ML models
  
- Export results as CSV or generate downloadable report cards

# Contributing

Pull requests, code improvements, and suggestions are welcome.

# License

This project is open-source and available for academic and commercial modification.



---

## 📂 Project Structure
