text = "X-DSPAM-Confidence:    0.8475"
sval_1 = text.find('0')
sval_2 = text [sval_1:]
number = float(sval_2)
print(number)
