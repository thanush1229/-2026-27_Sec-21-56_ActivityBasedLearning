# Case Study 35: Text Compression Using Character Runs

## 1. Problem Statement
Run-length encoding replaces each group of consecutive repeated characters with the character and its count (for example aaabb becomes a3b2). The program encodes a string, compares the original and encoded lengths and says whether compression is beneficial.

## 2. Objectives
- Traverse a string with a loop and compare neighbouring characters.
- Build a new string using concatenation and str().
- Handle the final run of characters after the loop.
- Compare lengths and decide whether the encoding helps.
- Validate empty input and input containing digits.

## 3. Assumptions
- Every run is written as character + count, even when the count is 1.
- Input must not contain digits, because digits would be confused with counts.
- Comparison is case-sensitive (A and a are different characters).
- Compression is beneficial only if the encoded text is strictly shorter.

## 4. Algorithm
1. Read the text.
2. If it is empty, or contains a digit, print an error and stop.
3. Set encoded = empty string and count = 1.
4. For i from 1 to length-1: if text[i] equals text[i-1], increase count; otherwise append text[i-1] and count to encoded and reset count to 1.
5. After the loop append the last character and its count.
6. Print both strings and their lengths.
7. If encoded is shorter, print BENEFICIAL with the saving; otherwise print NOT beneficial.

## 5. Pseudocode
```text
START
READ text
IF text is empty THEN PRINT error ; STOP
IF text contains a digit THEN PRINT error ; STOP
encoded <- "" ; count <- 1
FOR i <- 1 TO length(text)-1
    IF text[i] = text[i-1] THEN
        count <- count + 1
    ELSE
        encoded <- encoded + text[i-1] + count
        count <- 1
    END IF
END FOR
encoded <- encoded + text[last] + count
PRINT text, encoded, both lengths
IF length(encoded) < length(text) THEN PRINT "BENEFICIAL" ELSE PRINT "NOT beneficial"
END
```

## 6. Flowchart
![Flowchart for Case Study 35](images/case35_flowchart.png)

## 7. Python Source Code
File: `programs/case35_text_compression.py`

```python
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
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | aaabbc | a3b2c1 (6 vs 6) - NOT beneficial |
| T2 | aaaabbbcc | a4b3c2 (9 vs 6) - BENEFICIAL, saved 3 |
| T3 | zzzzzzzz | z8 (8 vs 2) - BENEFICIAL, saved 6 |
| T4 | a | a1 (1 vs 2) - NOT beneficial |
| T5 | AAaa | A2a2 (4 vs 4) - NOT beneficial (case-sensitive) |
| T6 | (empty) | Error: empty input |
| T7 | ab1 | Error: digits are not allowed |

*Run the program and type the input shown in the table.*

## 9. Sample Output
Full output saved in `outputs/case35_text_compression_output.txt`.

```text
--- Input: aaabbc ---
Enter text to compress (no digits): Original : aaabbc (length 6 )
Encoded  : a3b2c1 (length 6 )
Compression is NOT beneficial: keep the original text

--- Input: aaaabbbcc ---
Enter text to compress (no digits): Original : aaaabbbcc (length 9 )
Encoded  : a4b3c2 (length 6 )
Compression is BENEFICIAL: saved 3 characters

--- Input: zzzzzzzz ---
Enter text to compress (no digits): Original : zzzzzzzz (length 8 )
Encoded  : z8 (length 2 )
Compression is BENEFICIAL: saved 6 characters

--- Input: a ---
Enter text to compress (no digits): Original : a (length 1 )
Encoded  : a1 (length 2 )
Compression is NOT beneficial: keep the original text

--- Input: AAaa ---
Enter text to compress (no digits): Original : AAaa (length 4 )
Encoded  : A2a2 (length 4 )
Compression is NOT beneficial: keep the original text

--- Input:  ---
Enter text to compress (no digits): Error: empty input

--- Input: ab1 ---
Enter text to compress (no digits): Error: digits are not allowed (they would be confused with counts)
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case35_text_compression_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case35_text_compression_output.png)`

## 11. Conclusion
The program shows that compression only helps when the text has long runs: strings with few repeats become longer. Checking the length before deciding is therefore an important part of the solution.
