class QuotesPageLocators:
    QUOTE = 'div.quote'
    AUTHOR_DROPDOWN = 'select#author'
    # AUTHOR_DROPDOWN = 'select[name = "author"]'
    TAG_DROPDOWN = 'select#tag'
    SEARCH_BUTTON = 'input[name="submit_button"]'
    # folosit la wait - inseamna tag select cu id tag care are un option   si acel option are o valoare ( nu merge <option>-----</option>
    TAG_DROPDOWN_VALUE_OPTION = "select#tag option[value]"
