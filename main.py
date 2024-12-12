def Word_Spliter(test_text):
    for word in  test_text.split():
        yield word
test_text = "Съешь еще этих мягких французских булок да выпей чаю"
for word in Word_Spliter(test_text):
    print(word)