#!/usr/bin/env python3
# Since web scraping has navigation issues, let me create a manual solution
# Using the WebFetch results that worked earlier

# From the WebFetch, I can see Tobit 1:1 starts with:
# "This book tells the story of Tobit, son of Tobiel, son of Hananiel..."

tobit_verses = [
    # Chapter 1
    (1, 1, "This book tells the story of Tobit, son of Tobiel, son of Hananiel, son of Aduel, son of Gabael, son of Raphael, son of Raguel, of the family of Asiel and the tribe of Naphtali."),
    (1, 2, "During the days of Shalmaneser, king of the Assyrians, he was taken captive from Thisbe, which is south of Kedesh Naphtali in upper Galilee, above and to the west of Asher, north of Phogor."),
    (1, 3, "I, Tobit, have walked all the days of my life on paths of fidelity and righteousness. I performed many charitable deeds for my kindred and my people who had been taken captive with me to Nineveh, in the land of the Assyrians."),
    (1, 4, "When I lived as a young man in my own country, in the land of Israel, the entire tribe of my ancestor Naphtali broke away from the house of David, my ancestor, and from Jerusalem, the city that had been singled out of all Israel's tribes that all Israel might offer sacrifice there. It was the place where the temple, God's dwelling, had been built and consecrated for all generations to come."),
    (1, 5, "All my kindred, as well as the house of Naphtali, my ancestor, used to offer sacrifice on every hilltop in Galilee to the calf that Jeroboam, king of Israel, had made in Dan."),
    (1, 6, "But I alone used to go often to Jerusalem for the festivals, as was prescribed for all Israel by longstanding decree. Bringing with me the first fruits of crops, the firstlings of the flock, the tithes of livestock, and the first shearings of sheep, I used to hasten to Jerusalem"),
    (1, 7, "and present them to the priests, Aaron's sons, at the altar. To the Levites ministering in Jerusalem I used to give the tithe of grain, wine, olive oil, pomegranates, figs, and other fruits. Six years in a row, I used to give a second tithe in money, which each year I would go to pay in Jerusalem."),
    (1, 8, "The third-year tithe I gave to orphans, widows, and converts who had joined the Israelites. Every third year I would bring them this offering, and we ate it in keeping with the decree laid down in the Mosaic law concerning it, and according to the commands of Deborah, the mother of my father Tobiel; for my father had died and left me an orphan."),
    (1, 9, "When I reached manhood, I married Anna, a woman of our ancestral family. By her I had a son whom I named Tobiah."),
    (1, 10, "Now, after I had been deported to the Assyrians and came as a captive to Nineveh, all my kindred and my people used to eat the food of the Gentiles,"),
    (1, 11, "but I refrained from eating that Gentile food."),
    (1, 12, "Because I was mindful of God with all my heart,"),
    (1, 13, "the Most High granted me favor and status with Shalmaneser, so that I became purchasing agent for all his needs."),
    (1, 14, "Until he died, I would go to Media to buy goods for him there. I also deposited pouches of silver worth ten talents in trust with my kinsman Gabael, son of Gabri, who lived at Rages, in the land of Media."),
    (1, 15, "When Shalmaneser died and his son Sennacherib came to rule in his stead, the roads to Media became unsafe, so I could no longer go to Media."),
    (1, 16, "In the days of Shalmaneser I had performed many charitable deeds for my kindred, members of my people."),
    (1, 17, "I would give my bread to the hungry and clothing to the naked. If I saw one of my people who had died and been thrown behind the wall of Nineveh, I used to bury him."),
    (1, 18, "I also buried those who were killed by Sennacherib when he returned fleeing from Judea during the days of the judgment executed upon him by the King of Heaven for his blasphemies. For in his rage he killed many Israelites, but I used to take their bodies by stealth and bury them; so when Sennacherib looked for them, he could not find them."),
    (1, 19, "But a certain Ninevite went and informed the king about me, that I was burying them, and I went into hiding. When I realized that the king knew about me and that I was being hunted to be put to death, I became afraid and took flight."),
    (1, 20, "All my property was confiscated; I was left with nothing. All that I had was taken to the king's palace, except for my wife Anna and my son Tobiah."),
    (1, 21, "But forty days did not pass before two of the king's sons assassinated him and fled to the mountains of Ararat. A son of his, Esarhaddon, succeeded him as king. He put Ahiqar, my kinsman Anael's son, in charge of all the credit accounts of his kingdom, and he took control over the entire administration."),
    (1, 22, "Then Ahiqar interceded on my behalf, and I returned to Nineveh. Ahiqar had been chief cupbearer, keeper of the signet ring, treasury accountant, and credit accountant under Sennacherib, king of the Assyrians; and Esarhaddon appointed him as Second to himself. He was, in fact, my nephew, of my father's house, and of my own family.")
]

def create_html_file():
    """Create HTML file from the verse data"""
    html_content = "<h1 class='et'>Tobit</h1>\n<BR>\n"
    html_content += "<div id=\"contenten\" style=\"position:relative; top:0px; left:0px; overflow:auto\"><table cellpadding=0 cellspacing=0 border=0>\n"
    
    for chapter, verse, text in tobit_verses:
        clean_text = text.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
        html_content += f"<tr><td class=\"vn\">{chapter}:{verse}</td><td class=\"vn\">&nbsp;&nbsp;</td><td class=\"v en\">{clean_text}</td></tr>\n"
    
    html_content += "</table></div>"
    
    output_file = "/Users/suganolab/web/bibleweb/public/static/html/en/tobit.htm"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Created {output_file} with {len(tobit_verses)} verses")
    print("This is just Chapter 1 - we'll need to add the remaining chapters")

if __name__ == "__main__":
    create_html_file()