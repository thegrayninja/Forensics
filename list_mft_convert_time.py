# github.com/thegrayninja

##
# Specifically created for list_mft.py. Can almost guarantee it will fail with anything else.
# My brain can't convert epoch time...so this script does it for me


# note: the below is information regarding the report exported
# 	from list_mft.py. No headers are included...so...good luck
#	below columns listed are physical columns.
#	-1 when reading ParsedLines
# column 1 is unknown
# column 2 is filename
# columns 3-6 are unknown
# column 7 is file size in MB (I presume)
# columns 8,9,10,11 are epoch


import datetime


def ConvertEpochToStandard(EpochTime):
    try:
        return (datetime.datetime.fromtimestamp(EpochTime).strftime('%c'))
    except:
        return EpochTime  # giving back the data it gave


def OpenFile():
    MTFFileName = raw_input("Please enter the name of your Lines_MFT export: ")
    DataFile = open(MTFFileName, "r")
    MyDataContents = DataFile.readlines()
    DataFile.close()

    return MyDataContents


def SaveFile(DataToSave):
    UpdatedMTFFileName = raw_input("\nPlease enter the name for your new file: ")
    DataFile = open(UpdatedMTFFileName, "w")
    DataFile.write(DataToSave)
    DataFile.close()

    print "\n\n%s has been saved to your current directory!\n\nThank you for using this tool. Enjoy!\n" % UpdatedMTFFileName


def ParseFile(MyDataContents):
    UpdateFile = ""
    LineCount = 1
    for i in MyDataContents:
        try:
            ParsedLines = i.split("|")
            for ParsedCount in range(7, 11):
                ParsedLines[ParsedCount] = ConvertEpochToStandard(float(ParsedLines[ParsedCount]))
            for j in range(0, 10):
                UpdateFile += "%d|%s|" % (LineCount, ParsedLines[j])
            UpdateFile += "%s\n" % (ParsedLines[10])
            LineCount += 1
        except:
            ErrorMessage = "%d|Error for { %s }.\n" % (LineCount, i)
            print(ErrorMessage)
            UpdateFile += ErrorMessage
            LineCount += 1

    SaveFile(UpdateFile)


def WelcomePage():
    print ""
    header = "\t/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\"

    print header
    print header
    print header
    print header
    print "\n\tWELCOME TO List_MFT_Convert_Time.py\n\n"


def main():
    WelcomePage()
    ParseFile(OpenFile())


if __name__ == main():
    main()
