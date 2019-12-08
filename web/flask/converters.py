def ConvertBooleanToText(booleanValue):
    if booleanValue: 
        return 'Yes'
    else:
        return 'No'
    pass

def ConvertToTwoDecimals(decimalValue):
    return '%.2f' % decimalValue

def ConvertEnumBookTypeToDescription(bookType):
    if bookType == 0:
        bookTypeDescription = 'Fiction'
    else:
        if bookType == 1:
            bookTypeDescription = 'Non-fiction'
        else:
            if bookType == 2:
                bookTypeDescription = 'Eductional'
            else:
                bookTypeDescription = 'Unknown'
    return bookTypeDescription + ' (' + str(bookType) + ')'