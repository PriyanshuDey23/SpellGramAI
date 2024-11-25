PROMPT="""

- Input Prompt:-Correct the spelling and grammar errors in the following text, and provide a marked version showing the original errors and their corrections.

Text: {input_text}

- Please format the output as follows:

Original Text
[Original text with errors marked]

Corrected Text
[Corrected text]

Error Corrections
[Table or list showing each error, its correction, and the location of the error in the text]"

- Example Output

Original Text
Thiss is a sentance with a speling and grammer mistake.

Corrected Text
This is a sentence with a spelling and grammar mistake.

Error Corrections(Table Format)

Error	      Correction	Location

Thiss	      This	        1st word
sentance	  sentence	    2nd word
speling	      spelling	    5th word
grammer	      grammar	    6th word

"""