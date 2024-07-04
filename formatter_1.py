import re

text = """ s 

 3 Nephi,  3 Ne. 8:9, 14; 9:4, 7; 10:13
 3 Nephi 9:6
 3 Nephi 8:19"""

text = text.replace("-", "").replace("–", "").replace("—", "").replace("\n", ",")
#print(text)
#modified_text = re.sub(r':[^,\n]*', '', text)
#print(modified_text)
#subtracted_text = text.replace(":", "", 1)
#subtracted_modified_text = re.sub(r':[^,\n]*', '', subtracted_text)
#print(subtracted_modified_text)
#modified_text_newline = modified_text.replace("\n", ",").strip()

scripture_list = ["Genesis","Exodus", "Ex.","Leviticus","Numbers","Deuteronomy", "Deut.","Joshua","Judges","Ruth","1 Samuel", "1 Sam.","2 Samuel", "2 Sam.", "1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms", "Psalm","Proverbs","Ecclesiastes", "Song of Solomon", "Isaiah", "Isa.", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "1 Cor.", "JST 1 Corinthians" "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Philip.", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Philem.", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation", "1 Nephi", "1 Ne.", "2 Nephi", "2 Ne.", "Jacob", "Enos", "Jarom", "Omni", "Words of Mormon", "Mosiah", "Alma", "Helaman", "3 Nephi", "3 Ne.","4 Nephi", "4 Ne.", "Mormon", "Ether", "Moroni","Moro.", "Book of Moses", "Book of Abraham", "Joseph Smith—Matthew", "Joseph Smith—History", "Articles of Faith", "Doctrine and Covenants","Doctrine & Covenants", "Bible", "Pearl of Great Price", "D&C", "Old Testament", "New Testament"]
vague_scriptures_list_new = []
matching_scriptures = ""
final_unique = []
extra_unique_string = ""
matching_scriptures_list = []

pattern = r'([1-3]?\s?[a-zA-Z]+&?[a-zA-Z]+\.?\s*\d+),?'
pattern2 = r'\b([1-3]?\s*[A-Za-z]+\.\s*\d+)\b'
pattern_JST = r'(JST\s+[1-3]?\s?[a-zA-Z]+\.?\s*(?:\d+)?)'
pattern_DC_sections = r'(Section \d+ of \s?Doctrine and Covenants)'
pattern_extra_number = r'([1-3]\s\s[1-3]?\s?\w+\.?\s*\d+),?'

clean_extra_number_list = []
scriptures_list = []
book_of_mormon_item = []

matches_extra_number = re.findall(pattern_extra_number, text)
matches2 = re.findall(pattern2, text)
matches_pattern_JST = re.findall(pattern_JST, text, re.IGNORECASE)
matches_DC_sections = re.findall(pattern_DC_sections, text)


# Obsolete: Pattern and Matches colon
#colon_pattern = r':'
#matches_colon = re.findall(colon_pattern, text)

if matches_DC_sections:
     matches_DC_sections_string = ", ".join(matches_DC_sections)
     #print(matches_DC_sections_string)

if matches_pattern_JST:
    #print(matches_pattern_JST)
    matches_pattern_JST_string = ", ".join(matches_pattern_JST)
    #print(matches_pattern_JST_string)
    text_without_JST = text.replace(matches_pattern_JST_string, "")
    #print(text_without_JST)
if matches_pattern_JST == []:
     text_without_JST = text
    
matches = re.findall(pattern, text_without_JST)

if matches:
        #print(matches)
        #print("matches statement runs")
        scriptures2 = matches2
        scriptures = matches
        #print(scriptures)
        for j in scriptures:
            j = j.strip()
            scriptures_list.append(j)
        #print(scriptures_list)
if text is not []:
    #print("elif is working")
    not_specific_scriptures = text.replace("\n", ",").strip()
    vague_scriptures_list = not_specific_scriptures.split(',')
    for vague_scripture in vague_scriptures_list:
        #print("working?")
        #print(vague_scripture)
        if "Book of Mormon" in vague_scripture:
            for vague_scripture in vague_scriptures_list:
                vague_scripture = vague_scripture.strip()
                vague_scripture = vague_scripture.replace("Book of Mormon", "")
                vague_scriptures_list_new.append(vague_scripture)
                book_of_mormon_item.append("Book of Mormon")
                #print(book_of_mormon_item)
            #print(vague_scriptures_list_new)
        else:
             vague_scripture = vague_scripture.strip()
             vague_scriptures_list_new.append(vague_scripture)

        for scripture_title in scripture_list:
            #print("for loop works")
            if scripture_title in vague_scripture:
                #print("if 1 works")
                #print(vague_scripture)
                matching_scriptures = scripture_title
                if matching_scriptures == "":
                    #print("if 2 works")
                    #print(matching_scriptures)
                    pass
                if matching_scriptures != "":
                    matching_scriptures_list.append(matching_scriptures)
                    #print(matching_scriptures_list)
                #else:
                    #print("else works")
                    #matching_scriptures_string_list = matching_scriptures + "," + scripture_title
                    #print(matching_scriptures_string_list) 
    #print(matching_scriptures_list)
    matching_scriptures_string = ', '.join(matching_scriptures_list)
    if matching_scriptures_string != "":
        #print(matching_scriptures_string)
        pass
    else:
        #print("No scriptures")   
        pass            
else:
    print("No scriptures")
    


    #print(scriptures_list)
big_scriptures = scriptures_list + clean_extra_number_list + matches_pattern_JST+matches_DC_sections + matching_scriptures_list + book_of_mormon_item
#print(big_scriptures)
#print("working big_scriptures")
if big_scriptures != []:
        def remove_duplicates_with_loop(big_scriptures):
            unique_items = ""
            seen = set()
            for item in big_scriptures:
                if item not in seen:
                    if big_scriptures[0] == item:
                        unique_items = item
                    else:
                        unique_items = unique_items+","+item
                    seen.add(item)
            return unique_items
        unique_list = remove_duplicates_with_loop(big_scriptures)
        #print([unique_list])
        if len([unique_list]) == 1:
            #print("unique_list == 1 is running")
            if "Doctrine and Covenants" not in unique_list:
                    if "Covenants" in unique_list:  
                        #print("DC_check if 1 is running")
                        unique_list_fixed_DC = unique_list.replace("Covenants", "Doctrine and Covenants")
                        #print(unique_list_fixed_DC)
                    else:
                        #print("first else statement ran")
                        unique_list_fixed_DC = unique_list
                        #print(unique_list_fixed_DC)
        #This is commented because the list will always be one item:
        # if len([unique_list]) > 1:
        #     #print("unique_list > 1 is running")
        #     for DC_check in unique_list:
        #         #print(DC_check)
        #         if "Doctrine and Covenants" not in DC_check:
        #             if "Covenants" in DC_check:  
        #                 print("DC_check if 2 is running")
        #                 unique_list_fixed_DC = unique_list.replace("Covenants", "Doctrine and Covenants")
        #             else:
        #                 unique_list_fixed_DC = unique_list
        #                 unique_list_fixed_DC = unique_list_fixed_DC.split(",")
        #         else:
        #             unique_list_fixed_DC = unique_list
        #             unique_list_fixed_DC = unique_list_fixed_DC.split(",")
        #     #print(unique_list_fixed_DC)
            if unique_list_fixed_DC:
                    unique_list_fixed_DC_array = unique_list_fixed_DC.split(",")
                    #print(unique_list_fixed_DC_array)
                    for unique_item in unique_list_fixed_DC_array:
                            #print(unique_item)
                            for scripture_title in scripture_list:
                                if scripture_title in unique_item:
                                    final_unique.append(unique_item)
                    #print(final_unique)
                    
            if len(final_unique) > 0:
                            extra_unique_string = final_unique[0]
                            #print(extra_unique_string)
                            for super_unique_item in final_unique[1:]:
                                extra_unique_string = extra_unique_string+","+super_unique_item
                            print(extra_unique_string)
elif big_scriptures == []:
        print("No scriptures")
        
        #print(final_unique)
                    #    final_unique = unique_item[0]
                    #else:
                    #    final_unique = final_unique+","+unique_item
        #print(final_unique)
        #print(unique_list_fixed_DC)
        #print(unique_items)



#print(modified_text_newline)

if matches_extra_number:
        #matches_extra_number_string = ', '.join(matches_extra_number)
        for extra_number_item in matches_extra_number:
            #print(extra_number_item)
            pattern_without_extra_number = re.sub(r'\d+', '', extra_number_item, count=1)
            #print(pattern_without_extra_number)
            clean_extra_number_list.append(pattern_without_extra_number.strip())
        #print(clean_extra_number_list)




#add a replace function that trades out Psalm with Psalms