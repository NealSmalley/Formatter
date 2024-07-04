import re

#Scripture List:
scripture_list = ["Genesis","Exodus", "Ex.","Leviticus","Numbers","Deuteronomy", "Deut.","Joshua","Judges","Ruth","1 Samuel", "1 Sam.","2 Samuel", "2 Sam.", "1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms", "Psalm","Proverbs","Ecclesiastes", "Song of Solomon", "Isaiah", "Isa.", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "1 Cor.", "JST 1 Corinthians" "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Philip.", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Philem.", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation", "1 Nephi", "1 Ne.", "2 Nephi", "2 Ne.", "Jacob", "Enos", "Jarom", "Omni", "Words of Mormon", "Mosiah", "Alma", "Helaman", "3 Nephi", "4 Nephi", "Mormon", "Ether", "Moroni","Moro.", "Book of Moses", "Book of Abraham", "Joseph Smith—Matthew", "Joseph Smith—History", "Articles of Faith", "Doctrine and Covenants","Doctrine & Covenants", "Bible", "Pearl of Great Price", "D&C", "Old Testament", "New Testament"]

def clean_text(text):
    """Clean and prepare the text for processing."""
    return text.replace("-", "").replace("–", "").replace("—", "").replace("\n", ",").strip()

def extract_scriptures(text):
    patterns = [
        #r'(Doctrine and Covenants\s?\d+)',
        r'\b([1-3]?\s*[A-Za-z]+\.)$',
        r'\b([1-3]\s*[A-Za-z]+\b\.?)',
        r'\b([1-3]?\s*[A-Za-z]+\.\s*\d+)\b',
        r'([1-3]?\s?[a-zA-Z]+&?[a-zA-Z]+\.?\s*\d+),?',
        r'(JST\s+[1-3]?\s?[a-zA-Z]+\.?\s*(?:\d+)?)',
        r'(Section \d+ of \s?Doctrine and Covenants)',
        r'(section \d+ of \s?Doctrine and Covenants)',
        r'([1-3]\s\s[1-3]?\s?\w+\.?\s*\d+),?'
    ]


    all_matches = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        all_matches.extend(matches)
    return all_matches




def replace_abbreviations(unique_items):
    replaced_unique_items = []
    patterns_abreviation = r'\b([1-3]?\s*[A-Za-z]+\.)$'
    #print(unique_items)
    for unique_item in unique_items:
        unique_item = unique_item.strip()
        #print(unique_item)
        matches_abreviation = re.findall(patterns_abreviation, unique_item)
        #print(matches_abreviation)
        if matches_abreviation:
            unique_item = unique_item.replace("Gen.", "Genesis")
            unique_item = unique_item.replace("Ge.", "Genesis")
            unique_item = unique_item.replace("Gn.", "Genesis")
            unique_item = unique_item.replace("Exod.", "Exodus")
            unique_item = unique_item.replace("Exo.", "Exodus")
            unique_item = unique_item.replace("Ex.", "Exodus")
            unique_item = unique_item.replace("Lev.", "Leviticus")
            unique_item = unique_item.replace("Le.", "Leviticus")
            unique_item = unique_item.replace("Lv.", "Leviticus")
            unique_item = unique_item.replace("Num.", "Numbers")
            unique_item = unique_item.replace("Nu.", "Numbers")
            unique_item = unique_item.replace("Nm.", "Numbers")
            unique_item = unique_item.replace("Nb.", "Numbers")
            unique_item = unique_item.replace("Deut.", "Deuteronomy")
            unique_item = unique_item.replace("De.", "Deuteronomy")
            unique_item = unique_item.replace("Dt.", "Deuteronomy")
            unique_item = unique_item.replace("Josh.", "Joshua")
            unique_item = unique_item.replace("Jos.", "Joshua")
            unique_item = unique_item.replace("Jsh.", "Joshua")
            unique_item = unique_item.replace("Josh.", "Joshua")
            unique_item = unique_item.replace("Rth.", "Ruth")
            unique_item = unique_item.replace("Ru.", "Ruth")
            unique_item = unique_item.replace("1 Sam.", "1 Samuel")
            unique_item = unique_item.replace("1 Sa.", "1 Samuel")
            unique_item = unique_item.replace("1 S.", "1 Samuel")
            unique_item = unique_item.replace("1 Sm.", "1 Samuel")
            unique_item = unique_item.replace("2 Sam.", "2 Samuel")
            unique_item = unique_item.replace("2 Sa.", "2 Samuel")
            unique_item = unique_item.replace("2 S.", "2 Samuel")
            unique_item = unique_item.replace("2 Sm.", "2 Samuel")
            unique_item = unique_item.replace("1 Kgs.", "1 Kings")
            unique_item = unique_item.replace("1Kgs.", "1 Kings")
            unique_item = unique_item.replace("1 Ki.", "1 Kings")
            unique_item = unique_item.replace("1Ki.", "1 Kings")
            unique_item = unique_item.replace("1Kin.", "1 Kings")
            unique_item = unique_item.replace("1K.", "1 Kings")
            unique_item = unique_item.replace("2 Kgs.", "2 Kings")
            unique_item = unique_item.replace("2Kgs.", "2 Kings")
            unique_item = unique_item.replace("2 Ki.", "2 Kings")
            unique_item = unique_item.replace("2Ki.", "2 Kings")
            unique_item = unique_item.replace("2Kin.", "2 Kings")
            unique_item = unique_item.replace("2K.", "2 Kings")
            unique_item = unique_item.replace("2 Chron.", "1 Kings")
            unique_item = unique_item.replace("2 Ch.", "1 Kings")
            unique_item = unique_item.replace("2Ch.", "1 Kings")
            unique_item = unique_item.replace("2Chr.", "1 Kings")
            unique_item = unique_item.replace("2Chron.", "1 Kings")
            unique_item = unique_item.replace("Ezr.", "Ezra")
            unique_item = unique_item.replace("Ez.", "Ezra")
            unique_item = unique_item.replace("Jb.", "Job")
            unique_item = unique_item.replace("Psalm.", "Psalms")
            unique_item = unique_item.replace("Pslm.", "Psalms")
            unique_item = unique_item.replace("Ps.", "Psalms")
            unique_item = unique_item.replace("Psa.", "Psalms")
            unique_item = unique_item.replace("Psm.", "Psalms")
            unique_item = unique_item.replace("Pss.", "Psalms")
            unique_item = unique_item.replace("Prov.", "Proverbs")
            unique_item = unique_item.replace("Pro.", "Proverbs")
            unique_item = unique_item.replace("Pr.", "Proverbs")
            unique_item = unique_item.replace("Prv.", "Proverbs")
            unique_item = unique_item.replace("Eccles.", "Ecclesiastes")
            unique_item = unique_item.replace("Eccle.", "Ecclesiastes")
            unique_item = unique_item.replace("Ecc.", "Ecclesiastes")
            unique_item = unique_item.replace("Ec.", "Ecclesiastes")
            unique_item = unique_item.replace("Qoh.", "Ecclesiastes")
            unique_item = unique_item.replace("Song of Songs.", "Song of Solomon")
            unique_item = unique_item.replace("Song.", "Song of Solomon")
            unique_item = unique_item.replace("So.", "Song of Solomon")
            unique_item = unique_item.replace("SOS.", "Song of Solomon")
            unique_item = unique_item.replace("Canticle of Canticles.", "Song of Solomon")
            unique_item = unique_item.replace("Canticles.", "Song of Solomon")
            unique_item = unique_item.replace("Cant", "Song of Solomon")
            unique_item = unique_item.replace("Isaiah.", "Isa")
            unique_item = unique_item.replace("Isaiah", "Is")
            unique_item = unique_item.replace("Jeremiah.", "Jer")
            unique_item = unique_item.replace("Jeremiah", "Je")
            unique_item = unique_item.replace("Jeremiah.", "Jr")
            unique_item = unique_item.replace("Lam.", "Lamentations")
            unique_item = unique_item.replace("La.", "Lamentations")
            unique_item = unique_item.replace("Ezek.", "Ezekiel")
            unique_item = unique_item.replace("Eze.", "Ezekiel")
            unique_item = unique_item.replace("Ezk.", "Ezekiel")
            unique_item = unique_item.replace("Dan.", "Daniel")
            unique_item = unique_item.replace("Da.", "Daniel")
            unique_item = unique_item.replace("Dn.", "Daniel")
            unique_item = unique_item.replace("Hos.", "Hosea")
            unique_item = unique_item.replace("Ho.", "Hosea")
            unique_item = unique_item.replace("Joe.", "Joel")
            unique_item = unique_item.replace("Jl.", "Joel")
            unique_item = unique_item.replace("Jl.", "Joel")
            unique_item = unique_item.replace("Am.", "Amos")
            unique_item = unique_item.replace("Obad.", "Obadiah")
            unique_item = unique_item.replace("Ob.", "Obadiah")
            unique_item = unique_item.replace("Jnh.", "Jonah")
            unique_item = unique_item.replace("Jon.", "Jonah")
            unique_item = unique_item.replace("Micah.", "Micah")
            unique_item = unique_item.replace("Mic.", "Micah")
            unique_item = unique_item.replace("Mc.", "Micah")
            unique_item = unique_item.replace("Nah.", "Nahum")
            unique_item = unique_item.replace("Na.", "Nahum")
            unique_item = unique_item.replace("Hab.", "Habakkuk")
            unique_item = unique_item.replace("Hb.", "Habakkuk")
            unique_item = unique_item.replace("Zech.", "Zechariah")
            unique_item = unique_item.replace("Zec.", "Zechariah")
            unique_item = unique_item.replace("Zc.", "Zechariah")
            unique_item = unique_item.replace("Mal.", "Malachi")
            unique_item = unique_item.replace("Ml.", "Malachi")
            unique_item = unique_item.replace("1 Ne.", "1 Nephi")
            unique_item = unique_item.replace("2 Ne.", "2 Nephi")
            unique_item = unique_item.replace("Jacob.", "Jacob")
            unique_item = unique_item.replace("Enos.", "Enos")
            unique_item = unique_item.replace("Jarom.", "Jarom")
            unique_item = unique_item.replace("Omni.", "Omni")
            unique_item = unique_item.replace("W of M", "Words of Mormon")
            unique_item = unique_item.replace("Mosiah.", "Mosiah")
            unique_item = unique_item.replace("Alma.", "Alma")
            unique_item = unique_item.replace("Hel.", "Helaman")
            unique_item = unique_item.replace("3 Ne.", "3 Nephi")
            unique_item = unique_item.replace("4 Ne.", "4 Nephi")
            unique_item = unique_item.replace("Morm", "Mormon")
            unique_item = unique_item.replace("Ether.", "Ether")
            unique_item = unique_item.replace("Moro.", "Moroni")

            replaced_unique_items.append(unique_item)
        else:
            replaced_unique_items.append(unique_item)
    return replaced_unique_items

def remove_duplicates(items):
    """Remove duplicate items from a list."""
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)
    return unique_items


def process_scriptures(text):
    """Main processing function to clean text and extract scriptures."""
    cleaned_text = clean_text(text)
    scriptures = extract_scriptures(cleaned_text)
    replace_abbreviations_scriptures = replace_abbreviations(scriptures)
    unique_scriptures = remove_duplicates(replace_abbreviations_scriptures)
    return unique_scriptures

#Text
text = """s    first   is section 20 of  Doctrine and Covenants,  describes God as  infinite and eternal.  Or s   from  Book of Mormon such as 2 Nephi 1:10 and Alma 34:1014  describe God as infinite.

In addition to specific s,  discussions about  concept of scripture in both  Evangelical and LDS faiths.    differing views on scripture between Evangelicals, who confine ir definition to  Bible and certain creeds, and Latterday Saints, who  additional modern prophetic statements and individual revelation as additional sources of scripture.

Overall, scripture plays a significant role in  discussions about key doctrinal issues like Godhood, deification, Christ,  Trinity, and salvation. Different interpretations of scripture and its authority contribute to  differences and similarities between  two faith traditions explored in  book."""

scriptures = process_scriptures(text)
filtered_scriptures = [scripture for scripture in scriptures if scripture]
filtered_scriptures_string = ", ".join(filtered_scriptures)
print(filtered_scriptures_string)
