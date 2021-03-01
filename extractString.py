myStr = 'X-DSPAM-Confidence: 0.8475 '

search = myStr.find(':')

countFloat = myStr[search+2:26]

#print(search)
print(float(countFloat))
