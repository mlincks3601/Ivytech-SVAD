Set target_Word = "logic"
Open dictionary to a random page

WHILE word_On_Page is not target_Word
    IF word_On_Page comes before target_Word alphabetically
        Go forward a few pages and examine
    ELSE IF word_On_Page comes after target_Word alphabetically
        Go back a few pages and examine
    END IF
    Look at new word_On_Page
END WHILE

Print "You found the word!"
