# Case Study 35: Text Compression Using Character Runs (Run-Length Encoding)
# Uses: strings, loops, conditionals

text = input("Enter text to compress (no digits): ")

has_digit = False
for ch in text:
    if ch.isdigit():
        has_digit = True

if len(text) == 0:
    print("Error: empty input")
elif has_digit:
    print("Error: digits are not allowed (they would be confused with counts)")
else:
    encoded = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count = count + 1                       # same character -> extend run
        else:
            encoded = encoded + text[i - 1] + str(count)
            count = 1                               # new run starts
    encoded = encoded + text[len(text) - 1] + str(count)   # write the last run

    print("Original :", text, "(length", len(text), ")")
    print("Encoded  :", encoded, "(length", len(encoded), ")")
    if len(encoded) < len(text):
        print("Compression is BENEFICIAL: saved", len(text) - len(encoded), "characters")
    else:
        print("Compression is NOT beneficial: keep the original text")
