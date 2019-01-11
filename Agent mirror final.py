

#>>>>>>>>>>>>>>>>>>>>>  PROJECT 2  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Your self for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.

# >>>>>>>>>>>>>>  CHANGE LOG    <<<<<<<<<<<<<<<<<<<<<
# refactored image access/load methods
# created individual methods for comparison, load, pixel extraction
# moved comparison logic to Solve
# removed arrays for looping through images; too complicated.  replaced with vars.abs
# made better use of np for asarray, abs and sum to extract dark pixels.

# >>>>>>>>>>>>>  GENERAL TODO   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# address 3x3 problems
#

from PIL import Image
from PIL import ImageOps
import numpy as np

print('Project 2 PLAYGROUND v2')

# Load images, render dark pixels as int
def loadImages(image):
    i = np.asarray(image.convert('1')).astype(np.int)
    return 1 - i

# Use np.abs to get difference in number of pixels between imgA and imgB
def compareAtoB(pixelCountImgA, pixelCountImgB, size):
    return np.abs(pixelCountImgB - pixelCountImgA)

# similarityThrshld how many pixels within 2-D array of X-Y are the same and compare to 90%
def similarity(pixelCountImgA, pixelCountImgB, thrshld=0.98):
    i = np.equal(pixelCountImgA, pixelCountImgB).astype(int) #set pixelCountImgA and pixelCountImgB equal
    j = np.mean(i) #avg of pixelCountImgA and pixelCountImgB
    return j > thrshld, j #return the greater of either avg or thrshld, avg.

    width, height = (184, 184) #vars for W, H
    match = 0 #init match var
    for x in range(width): #loop over W vars
        for y in range(height): #loop over H var
            if pixelCountImgA[x][y] == pixelCountImgB[x][y]:
                match += 1 #if W, H vars are equal, increment "match" var
    similarity = (match / (184 * 184) > thrshld, match / (184 * 184)) #convert similarity to % and return greater of match or match, thrshld
    return similarity

#
# Evaluate answer images to find which is most similar
def similarityThrshld(imgD, answerImagePixels, thrshld=0.99):
    percent = 0 #init percent similar local var
    default = -1 #init default answer var
    for index, element in enumerate(answerImagePixels): #loop over answerImagePixels
        i, j = similarity(imgD, element, thrshld=thrshld) #compare answerImagePixels
        if i and (j > percent): #if similarity index is greater than 0
            default = index + 1
            percent = j
    return default



class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.

    def Solve(self, problem):

        answer = -1

        # create and init dict for problems.
        figures = problem.figures

        if (problem.problemType == '2x2'):

            #load training and answer images
            imgA = Image.open(figures['A'].visualFilename)
            imgB = Image.open(figures['B'].visualFilename)
            imgC = Image.open(figures['C'].visualFilename)
            img1 = Image.open(figures['1'].visualFilename)
            img2 = Image.open(figures['2'].visualFilename)
            img3 = Image.open(figures['3'].visualFilename)
            img4 = Image.open(figures['4'].visualFilename)
            img5 = Image.open(figures['5'].visualFilename)
            img6 = Image.open(figures['6'].visualFilename)

            # create pixel counts for training images using loadImages
            pixelCountImgA = loadImages(imgA)
            pixelCountImgB = loadImages(imgB)
            pixelCountImgC = loadImages(imgC)

            # create pixel counts for answer images using loadImages
            Img1Pixels = loadImages(img1)
            Img2Pixels = loadImages(img2)
            Img3Pixels = loadImages(img3)
            Img4Pixels = loadImages(img4)
            Img5Pixels = loadImages(img5)
            Img6Pixels = loadImages(img6)

            #array of pixel counts for answer answer images
            answerImagePixels = [Img1Pixels, Img2Pixels, Img3Pixels, Img4Pixels, Img5Pixels, Img6Pixels]

            # Cross coompare pixel count for training imagesself.
            # This will find trivial matches where answer image pixels = training images pixels
            if np.array_equal(pixelCountImgA, pixelCountImgB): #if imgA, imgB are the same...
                answerImage = pixelCountImgC #then answerImage var equals imgC pixels
                for index, element in enumerate(answerImagePixels): #in which case we loop over answerImagePixels
                    if np.array_equal(answerImage, element): # if imgC pixels (via answerImage) equal answer image...
                        print('array_equal TRUE for imgA imgB')
                        answer = index + 1 #then answer var equals the corresponding answer image
                        break

            #repeat the above for ImgA and imgC
            elif np.array_equal(pixelCountImgA, pixelCountImgC): # otherwise, compare imgA and imgC
                answerImage = pixelCountImgB # init answerImage to imgB
                for index, element in enumerate(answerImagePixels):
                    if np.array_equal(answerImage, element):
                        print('array_equal TRUE for imgA imgC')
                        answer = index + 1
                        break

            else:

            #check for answer image as mirror or flip of training images.
                # create var for mirroring; init to L-R mirror of imgA
                mirrorpixelCountImgA = loadImages(ImageOps.mirror(imgA))
                #same as above but for T-B flip
                flippixelCountImgA = loadImages(ImageOps.flip(imgA))

                if answer == -1 and similarity(mirrorpixelCountImgA, pixelCountImgB)[1] > .95:
                    answer = similarityThrshld(loadImages(ImageOps.mirror(imgC)), answerImagePixels)
                    print('answer = imgA, imgB mirrored')
                if answer == -1 and similarity(mirrorpixelCountImgA, pixelCountImgC)[1] > .95:
                    answer = similarityThrshld(loadImages(ImageOps.mirror(imgB)), answerImagePixels)
                    print('answer = imgA, imgC mirrored')
                if answer == -1 and similarity(flippixelCountImgA, pixelCountImgB)[1] > .98:
                    answer = similarityThrshld(loadImages(ImageOps.flip(imgC)), answerImagePixels)
                    print('answer = imgA, imgB flip')
                if answer == -1 and similarity(flippixelCountImgA, pixelCountImgC)[1] > .98:
                    answer = similarityThrshld(loadImages(ImageOps.flip(imgB)), answerImagePixels)
                    print('answer = imgA, imgC flip')


                # use array_equal to compare pixel count for ImgA and ImgB to ImgC and ImgA and ImgC to ImgB

            for index, element in enumerate(answerImagePixels):
                print('\n  Now comparing answer: ' + str(answer) + ' to ' + problem.name + ':\n')
                #print('\n  Similarity threshold for: ' + str(similarityThrshld()))


                break


        pass


        return answer
