

"""
Course:  Training YOLO v3 for Objects Detection with Custom Data


Labelling new Dataset in YOLO format
File: creating-train-and-test-txt-files.py
"""


# Creating files train.txt and test.txt
# for training in Darknet framework
#
# 이 코드는 이렇게 작동한다. 알고리즘 수립
# Setting up full paths --> List of paths -->
# --> Extracting 15% of paths to save into test.txt file -->
# --> Writing paths into train and test txt files
#
# Result:
# Files train.txt and test.txt with full paths to images


# Importing needed library
import os


"""
Start of:
Setting up full path to directory with labelled images
"""

# Full or absolute path to the folder with images
# Find it with Py file getting-full-path.py
# Pay attention! If you're using Windows, yours path might looks like:
# r'C:\Users\my_name\Downloads\video-to-annotate'
# or:
# 'C:\\Users\\my_name\\Downloads\\video-to-annotate'
full_path_to_images = '/Users/kimkwangil/Project/YOLO-3-OpenCV/Downloads/youtube_movToImgs'

"""
End of:
Setting up full path to directory with labelled images
"""


"""
Start of:
Getting list of full paths to labelled images
"""

# Check point
# Getting the current directory
# print(os.getcwd())

# Changing the current directory
# to one with images
os.chdir(full_path_to_images)

# Check point
# Getting the current directory
print(os.getcwd())

# Defining list to write paths in, 여가에 경로를 담을 거다. 리스트의 공간을 만들자.
p = []

# Using os.walk for going through all directories
# and files in them from the current directory
# Fullstop in os.walk('.') means the current directory
for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:
        # Checking if filename ends with '.jpeg'
        if f.endswith('.jpeg'): #jpeg로 끝나는 파일이 있으면,
            # Preparing path to save into train.txt file
            # Pay attention!
            # If you're using Windows, it might need to change
            # this: + '/' +
            # to this: + '\' +
            # or to this: + '\\' +
            path_to_save_into_txt_files = full_path_to_images + '/' + f

            # Appending the line into the list
            # We use here '\n' to move to the next line
            # when writing lines into txt files
            p.append(path_to_save_into_txt_files + '\n') #새로운 라인에 풀패스를 추가한다.


# Slicing first 15% of elements from the list
# to write into the test.txt file
p_test = p[:int(len(p) * 0.15)]  #15%를 트레이닝 할거다.

# Deleting from initial list first 15% of elements
p = p[int(len(p) * 0.15):] #이만큼씩 삭제할거다.

"""
End of:
Getting list of full paths to labelled images
"""


"""
Start of:
Creating train.txt and test.txt files
"""

# Creating file train.txt and writing 85% of lines in it
with open('train.txt', 'w') as train_txt: #학습할 파일을 만든다. 85%를 트레이닝으로 만든다.
    # Going through all elements of the list
    for e in p:
        # Writing current path at the end of the file
        train_txt.write(e)

# Creating file test.txt and writing 15% of lines in it
with open('test.txt', 'w') as test_txt: #테스트를 할거임
    # Going through all elements of the list
    for e in p_test:
        # Writing current path at the end of the file
        test_txt.write(e)

"""
End of:
Creating train.txt and test.txt files
"""
