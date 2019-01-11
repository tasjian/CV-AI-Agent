

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
#
#

from PIL import Image
from PIL import ImageOps
import numpy as np
#from matplotlib import pyplot

print('Project 2 PLAYGROUND v3')

# Load images, render dark pixels as int
def loadImages(image):
    i = np.asarray(image.convert('1')).astype(np.int)
    return 1 - i

# Load images and convert to 8-bit for ImageChops
def loadImages8Bit(image):
    i = np.asarray(image.convert('L')).astype(np.int)
    return 1 - i

# Calculate abs value difference in number of pixels between imgA and imgB
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

# Evaluate if answer image is subtraction from training images
# def BLessThanA(pixelCountImgC, answerImagePixels):
#     for index, element in enumerate(answerImagePixels):
#         #np.where(pixelCountImgA > pixelCountImgB) and (pixelCountImgC > answerImagePixels)
#         #np.where(pixelCountImgA > pixelCountImgB) and (pixelCountImgC > answerImagePixels)
#         if np.array_equal(pixelCountImgC, answerImagePixels):
#             answerImage = pixelCountImgC # init answerImage to imgB
#             BLessThanA = -1
#             for index, element in enumerate(answerImagePixels):
#                 if np.array_equal(answerImage, element):
#                     BLessThanA = index + 1
#     return BLessThanA

# Evaluate if answer image adds pixels to training images
def BGreaterThanA(pixelCountImgA, pixelCountImgB, pixelCountImgC, answerImagePixels, thrshld=0.70):
    output = []
    default = -1
    i= np.abs(pixelCountImgA - pixelCountImgB)
    j= np.abs(answerImagePixels - pixelCountImgC)
    for index, element in enumerate(answerImagePixels):
        if (j >= i).any():
        #if np.abs(j < i):
            output.append(element)
            if len(output) <= 1:
                default = index + 1
    return default
#
def BLessThanA(pixelCountImgA, pixelCountImgB, pixelCountImgC, answerImagePixels, thrshld=0.70):
    output = []
    default = -1
    i= np.abs(pixelCountImgA - pixelCountImgB)
    j= np.abs(answerImagePixels - pixelCountImgC)
    for index, element in enumerate(answerImagePixels):
        if (j <= i).any():
        #if np.abs(j < i):
            output.append(element)
            if len(output) <= 1:
                default = index + 1
    return default
#
# def B09(pixelCountImgA, pixelCountImgB, pixelCountImgC, answerImagePixels, thrshld=0.70):
#     #output = []
#     default = -1
#     i= np.abs(pixelCountImgB)
#     j= np.abs(pixelCountImgA)
#     if (i > j):
#         for index, element in enumerate(answerImagePixels):
#             default = np.abs(element > pixelCountImgC)
#             #default = index + 1
#     return default

# def rot90(matrixImagesProcessed, answerImagesProcessed): #and (matrixList[3]) == np.rot90(answerList):
#     default = -1#i = ([matrixImagesProcessed][1])
#     key = matrixImagesProcessed
#     i = np.array([matrixImagesProcessed][key])
#     j = np.array([matrixImagesProcessed][key])
#     if np.abs(i) == np.rot90(j) and np.abs(j) == np.rot90(answerImagesProcessed):
#         dict((k, matrixImagesProcessed[k]) for k in answerImagesProcessed if k in matrixImagesProcessed)
#     #i = np.array([matrixImagesProcessed][1])
#     # j = np.array([matrixImagesProcessed][2])
#     # k = np.array([matrixImagesProcessed][3])   # init answerImage to imgB
#     # default = -1
#     # for index, element in enumerate(answerImagesProcessed):
#     #     if np.abs(i) == np.rot90(j) and np.abs(j) == np.rot90(answerImagesProcessed):
#         default = answerImagesProcessed[key] + 1
#     return default

#    dict((k, matrixImagesProcessed[k]) for k in keys_to_select)

# def difference(pixelCountImgA, pixelCountImgB, pixelCountImgC, answerImagePixels):
#     # default = -1
#     # i = pixelCountImgB - pixelCountImgA
#     # x = np.equal(pixelCountImgC, answerImagePixels).astype(int)
#     #j = np.mean(i) #avg of pixelCountImgA and pixelCountImgB
#     for index, element in enumerate(answerImagePixels):
#          #set pixelCountImgA and pixelCountImgB equal
#         if np.where(pixelCountImgB > pixelCountImgA and pixelCountImgC > answerImagePixels):
#             default = index + 1
#     return default

# Evaluate if answer image adds pixels to training images
# def rotation90(pixelCountImgA, pixelCountImgB, pixelCountImgC, answerImagePixels, thrshld=0.98):
#     for index, element in enumerate(answerImagePixels):
#         if np.where(pixelCountImgB) == np.rot90(pixelCountImgA) < thrshld and (pixelCountImgC) == np.rot90(answerImagePixels) < thrshld:
#             answerImage = pixelCountImgC # init answerImage to imgB
#             default = -1
#             for index, element in enumerate(answerImagePixels):
#                 if np.array_equal(answerImage, element):
#                     default = index + 1
#     return default



# def contours(answerImagePixels):
#
#     for index, element in enumerate(answerImagePixels):
#         thresh1 = 127
#         thresh2 = 254
#
#         gryim = np.mean(answerImagePixels[:,:,0:2],2)
#         region1 = (thresh1 < gryim)
#         region2 = (thresh2 < gryim)
#         nregion1 = ~ region1
#         nregion2 = ~ region2
#
#         #Get location of edge by comparing array to it's
#         #inverse shifted by a few pixels
#         shift = -2
#         edgex1 = (region1 ^ np.roll(nregion1,shift=shift,axis=0))
#         edgey1 = (region1 ^ np.roll(nregion1,shift=shift,axis=1))
#         edgex2 = (region2 ^ np.roll(nregion2,shift=shift,axis=0))
#         edgey2 = (region2 ^ np.roll(nregion2,shift=shift,axis=1))
#
#         #Plot location of edge over image
#         axs[1,1].imshow(answerImagePixels)
#         axs[1,1].contour(edgex1,2,colors='r',lw=2.)
#         axs[1,1].contour(edgey1,2,colors='r',lw=2.)
#         axs[1,1].contour(edgex2,2,colors='g',lw=2.)
#         axs[1,1].contour(edgey2,2,colors='g',lw=2.)




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

            elif np.count_nonzero(pixelCountImgA - np.rot90(pixelCountImgB, k = 1)):
                answerImage = pixelCountImgB #
                for index, element in enumerate(answerImagePixels):
                    if np.count_nonzero(pixelCountImgA - np.rot90(pixelCountImgB, k = 1)): #np.array_equal(answerImage, element):
                        print('90 degree rot')
                        answer = index + 1
                        break

            #    lambda imgA, imgB, threshold


            # if np.rot90(pixelCountImgA, pixelCountImgB): #if imgA, imgB are the same...
            #     answerImage = pixelCountImgC #then answerImage var equals imgC pixels
            #     for index, element in enumerate(answerImagePixels): #in which case we loop over answerImagePixels
            #         if np.array_equal(answerImage, element): # if imgC pixels (via answerImage) equal answer image...
            #             print('array_equal TRUE for imgA imgB')
            #             answer = index + 1 #then answer var equals the corresponding answer image
            #             break



            #repeat the above for ImgA and imgC
            # elif np.rot90(pixelCountImgA, pixelCountImgC): # otherwise, compare imgA and imgC
            #     answerImage = pixelCountImgB # init answerImage to imgB
            #     for index, element in enumerate(answerImagePixels):
            #         if np.array_equal(answerImage, element):
            #             print('array_equal TRUE for imgA imgC')
            #             answer = index + 1
            #             break

            # elif answer == -1:
            #     output = []
            #     answer = -1
            #     i= np.abs(pixelCountImgB - pixelCountImgA)
            #     j= np.abs(pixelCountImgC - pixelCountImgC)
            #     for index, element in enumerate(answerImagePixels):
            #         if (j > i).any():
            #             output.append(element)
            #             if len(output) <= 1:
            #                 answer = index + 1


            else:

                #check for answer image as mirror or flip of training images.
                # create var for mirroring; init to L-R mirror of imgA
                mirrorpixelCountImgA = loadImages(ImageOps.mirror(imgA))
                #same as above but for T-B flip
                flippixelCountImgA = loadImages(ImageOps.flip(imgA))
                #imagePixelCountC = loadImages(imgC)
                #difference = loadImages(np.asarray(image.convert('1').astype(np.int)(imgC)

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

                if answer == 1:
                    answer = BGreaterThanA(pixelCountImgC, pixelCountImgB, pixelCountImgA, answerImagePixels)
                    print('answer = imgA, imgC flip')

                if answer == -1:
                    answer = BLessThanA(pixelCountImgC, pixelCountImgB, pixelCountImgA, answerImagePixels)
                    print('answer = imgA, imgC flip')

                # if answer == -1:
                #     answer = lambda imgA, imgB, threshold: np.count_nonzero(imgA - np.rot90(imgB, k = 1)) < threshold

                #     # check to see if whole image is rotated 180deg
                #     rot180 = lambda imgA, imgB, threshold: np.count_nonzero(imgA - np.rot90(imgB, k = 2)) < threshold
                #
                #     # check to see if whole image is rotated 270deg
                #     rot270 = lambda imgA, imgB, threshold: np.count_nonzero(imgA - np.rot90(imgB, k = 3)) < threshold
                #
                # if answer == -1 and B09(pixelCountImgC, pixelCountImgB, pixelCountImgA, answerImagePixels) !=6:
                #     answer = B09(pixelCountImgC, pixelCountImgB, pixelCountImgA, answerImagePixels)
                #     print('answer = imgA, imgC flip')




            #    greaterThanLocal = loadImages(np.where(greaterThanAB)and(greaterThanAC))

            # if answer == -1 and np.array_equal(pixelCountImgC, answerImagePixels):
            #     answer = BLessThanA(pixelCountImgC, answerImagePixels)
            #    print('answer less than C')
            # if answer == -1:
            #     answer = (BGreaterThanA(pixelCountImgA, pixelCountImgB, pixelCountImgC, answerImagePixels))
            #     print('answer = B greater than A')
            # if answer == -1:
            #     answer = (rotation90(pixelCountImgA, pixelCountImgB, pixelCountImgC, answerImagePixels))
            #
            # if answer == -1 and difference(pixelCountImgA, pixelCountImgB, pixelCountImgC, answerImagePixels)[1] > .98:
            #     answer = difference(answerImagePixels)
            #     print('answer = imgA, imgC flip')


                # use array_equal to compare pixel count for ImgA and ImgB to ImgC and ImgA and ImgC to ImgB

            # for index, element in enumerate(answerImagePixels):
            #     print('\n  Now comparing answer: ' + str(answer) + ' to ' + problem.name + ':\n')
                #print('\n  Similarity threshold for: ' + str(similarityThrshld()))


            return answer
        #print ('\n  3x3 pixels for ' + problem.name + str(answerImagePixels))

        elif problem.problemType == "3x3":

            print("\n" + problem.name + "\n")

            # Store figure variables in a list

            matrixList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            answerList = ['1', '2', '3', '4', '5', '6', '7', '8']

            matrixImages = {}
            answerImages = {}
            matrixImages1 = {}
            answerImages1 = {}
            matrixImagesProcessed = {}
            answerImagesProcessed = {}


            for key in matrixList:
                matrixImages1[key] = Image.open(problem.figures[key].visualFilename)
                matrixImagesProcessed[key] = np.asarray(matrixImages1[key].convert('1')).astype(np.int)

            for key in answerList:
                answerImages1[key] = Image.open(problem.figures[key].visualFilename)
                answerImagesProcessed[key] = np.asarray(answerImages1[key].convert('1')).astype(np.int)

            # for key in answerImagesProcessed:
            #     if answer == -1:
            #         answer = rot90(matrixImagesProcessed, answerImagesProcessed)
            #
            # for key in answerList:
            #     n = min(len(matrixImagesProcessed), len(answerImagesProcessed))
            #     out_idx = np.flatnonzero(matrixImagesProcessed[:n] == answerImagesProcessed[:n])
            #     out_val = matrixImagesProcessed[out_idx] # or b[out_idx] both work
            #         if np.where(matrixList[7] < answerList).any():
            #
            #             #i = -1 if matrixImagesProcessed[8] else answerList[key]
            #         #if np.array_equal(matrixImagesProcessed, answerImagesProcessed):
            #            answer = answerImagesProcessed[key]
            #            return answer
            #            print ('answer ' + matrixImagesProcessed[key])
            #            break





            for key in answerList:
                if answer == -1 and similarity(matrixImages1, answerImages1)[1] > .98:
                #if answer = -1 and np.array_equal(matrixImagesProcessed[8], answerImagesProcessed[key]):
                    #for key in matrixImagesProcessed:
                    #i = -1
                    for index, key in enumerate(answerImagesProcessed):
                    #    if np.array(matrixImages1[]) > answerImages1[key]):
                        if np.array_equal(matrixImagesProcessed[8], answerImagesProcessed[key]):
                            #i = -1 if matrixImagesProcessed[8] else answerList[key]
                        #if np.array_equal(matrixImagesProcessed, answerImagesProcessed):
                           answer = answerImages1[key]
                           return answer
                           print ('answer ' + matrixImagesProcessed[key])
                           break


            # if np.array_equal(pixelCountImgA, pixelCountImgB): #if imgA, imgB are the same...
            #     answerImage = pixelCountImgC #then answerImage var equals imgC pixels
            #     for index, element in enumerate(answerImagePixels): #in which case we loop over answerImagePixels
            #         if np.array_equal(answerImage, element): # if imgC pixels (via answerImage) equal answer image...
            #             print('array_equal TRUE for imgA imgB')
            #             answer = index + 1 #then answer var equals the corresponding answer image
            #             break

            print ('answer ' + str(answer))
#

        return answer
