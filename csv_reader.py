def get_joint_angles(file_name):
    J1 = []
    J2 = []
    J3 = []
    try:
        openFile = open(file_name, 'r')
    except:
        print("Please either change the file name in the variable named filename or move the data file into the "
              "directory of this program")
        raise KeyboardInterrupt
    # read the lines of the file, saved in a list
    lines = openFile.readlines()
    for line in lines:
        # split csv based on commas
        splitLine = line.split(",")
        # if there is only one data point, we need to just move on
        if len(splitLine) < 4:
            continue
        # only take first two data points in the line
        split2 = [splitLine[0], splitLine[1], splitLine[2], splitLine[3]]
        # remove all whitespace in the data
        split2[0] = (split2[0].strip()).replace(" ", "")
        split2[1] = (split2[1].strip()).replace(" ", "")
        split2[2] = (split2[2].strip()).replace(" ", "")
        # now, we want to try and convert each data point into a float.  If this throws an error, throw out the line.
        # if not, append the data to the end of each of their respective lists
        try:
            split2[0] = float(split2[0])
            split2[1] = float(split2[1])
            split2[2] = float(split2[2])

        except:
            continue
        else:
            J1.append(split2[0])
            J2.append(split2[1])
            J3.append(split2[2])
        finally:
            continue
    # return the joint angles in a tuple
    return J1, J2, J3
if __name__=="__main__":
    J1, J2, J3 = get_joint_angles("maneuver_3.csv")
    print(J1)
    print(J2)
    print(J3)