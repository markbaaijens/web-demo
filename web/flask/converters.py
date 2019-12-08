from enums import BookType

def ConvertBooleanToText(booleanValue):
    if booleanValue: 
        return 'Yes'
    else:
        return 'No'
    pass

def ConvertToTwoDecimals(decimalValue):
    return '%.2f' % decimalValue

def ConvertEnumBookTypeToDescription(bookType):
    if bookType == BookType.Unknown:
        bookTypeDescription = 'Unknown'
    else:
        if bookType == BookType.Fiction:
            bookTypeDescription = 'Fiction'
        else:
            if bookType == BookType.NonFiction:
                bookTypeDescription = 'Non-fiction'
            else:
                if bookType == BookType.Educational:
                    bookTypeDescription = 'Educational'
    return bookTypeDescription + ' (' + str(bookType) + ')'