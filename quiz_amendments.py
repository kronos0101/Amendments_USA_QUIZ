import random

def amendments_quiz():
    # Simple format for questions
    questions = {
    1: "Freedom of speech, religion, press, assembly, and petition (1791) - \nJames Madison - Most impacted: All U.S. citizens, especially activists and minorities.\ ",
    2: "Right to keep and bear arms (1791) - \nJames Madison - Most impacted: Gun owners and advocates for self-defense.\ ",
    3: "No quartering of soldiers in private homes without consent (1791) - \nJames Madison - Most impacted: Private homeowners.\ ",
    4: "Protection against unreasonable searches and seizures (1791) - \nJames Madison - Most impacted: Individuals involved in legal or criminal justice matters.\ ",
    5: "Protection against self-incrimination, double jeopardy; guarantees due process (1791) - \nJames Madison - Most impacted: Defendants in criminal cases.\ ",
    6: "Right to a speedy and public trial by an impartial jury (1791) - \nJames Madison - Most impacted: Defendants in criminal trials.\ ",
    7: "Right to trial by jury in civil cases (1791) - \nJames Madison - Most impacted: Civil litigants seeking justice.\ ",
    8: "Protection against cruel and unusual punishment (1791) - \nJames Madison - Most impacted: Inmates and criminal defendants.\ ",
    9: "Rights retained by the people, even if not specifically enumerated in the Constitution (1791) - \nJames Madison - Most impacted: All U.S. citizens, especially those concerned about overreach.\ ",
    10: "Powers not delegated to the federal government are reserved to the states or the people (1791) - \nJames Madison - Most impacted: State governments and individuals.\ ",
    11: "Limits lawsuits against states (1795) - \nJohn Marshall - Most impacted: State governments.\ ",
    12: "Revises presidential election procedures (1804) - \nThomas Jefferson - Most impacted: Presidential candidates and voters.\ ",
    13: "Abolition of slavery (1865) - \nAbraham Lincoln - Most impacted: Enslaved individuals.\ ",
    14: "Equal protection under the law and due process for all citizens (1868) - \nJohn Bingham - Most impacted: Minorities and historically marginalized groups.\ ",
    15: "Right to vote cannot be denied based on race, color, or previous servitude (1870) - \nUlysses S. Grant - Most impacted: African Americans and minorities.\ ",
    16: "Congress can levy an income tax (1913) - \nWilliam Howard Taft - Most impacted: Taxpayers.\ ",
    17: "Establishes the direct election of U.S. Senators by popular vote (1913) - \nWoodrow Wilson - Most impacted: Voters.\ ",
    18: "Prohibition of alcohol (1919, repealed by the 21st Amendment in 1933) - \nWayne Wheeler - Most impacted: Alcohol producers and consumers.\ ",
    19: "Women's right to vote (1920) - \nSusan B. Anthony - Most impacted: Women.\ ",
    20: "Changes the dates of congressional and presidential terms (1933) - \nGeorge Norris - Most impacted: Congress and the president.\ ",
    21: "Repeal of Prohibition (18th Amendment) (1933) - \nFiorello La Guardia - Most impacted: Alcohol producers and consumers.\ ",
    22: "Limits the President to two terms in office (1951) - \nHarry S. Truman - Most impacted: Presidential candidates.\ ",
    23: "Gives residents of Washington D.C. the right to vote for representatives in the Electoral College (1961) - \nEleanor Holmes Norton - Most impacted: D.C. residents.\ ",
    24: "Abolishes poll taxes (1964) - \nLyndon B. Johnson - Most impacted: Low-income voters.\ ",
    25: "Addresses presidential succession and disability (1967) - \nBirch Bayh - Most impacted: Presidential officeholders and their staff.\ ",
    26: "Voting age lowered to 18 (1971) - \nJennings Randolph - Most impacted: Young voters.\ ",
    27: "Delays laws affecting Congressional salary from taking effect until after the next election of representatives (1992) - \nGregory Watson - Most impacted: Members of Congress.\ "
}


    # Detailed answers
    answers = {
        1: "Freedom of speech, religion, press, assembly, and petition (1791) - James Madison - Most impacted: All U.S. citizens, especially activists and minorities. Trick: 1 mouth, 1 voice.",
        2: "Right to keep and bear arms (1791) - James Madison - Most impacted: Gun owners and advocates for self-defense. Trick: 2 arms to bear arms.",
        3: "No quartering of soldiers in private homes without consent (1791) - James Madison - Most impacted: Private homeowners. Trick: 3's a crowd (no soldiers in homes).",
        4: "Protection against unreasonable searches and seizures (1791) - James Madison - Most impacted: Individuals involved in legal or criminal justice matters. Trick: 4 walls protect your privacy.",
        5: "Protection against self-incrimination, double jeopardy; guarantees due process (1791) - James Madison - Most impacted: Defendants in criminal cases. Trick: Take the 5th (remain silent).",
        6: "Right to a speedy and public trial by an impartial jury (1791) - James Madison - Most impacted: Defendants in criminal trials. Trick: Speedy trial gets you home by 6.",
        7: "Right to trial by jury in civil cases (1791) - James Madison - Most impacted: Civil litigants seeking justice. Trick: 7 rhymes with 'heaven'—fair civil trials.",
        8: "Protection against cruel and unusual punishment (1791) - James Madison - Most impacted: Inmates and criminal defendants. Trick: Sideways 8 looks like handcuffs.",
        9: "Rights retained by the people, even if not specifically enumerated in the Constitution (1791) - James Madison - Most impacted: All U.S. citizens, especially those concerned about overreach. Trick: 9 makes sure you’re fine.",
        10: "Powers not delegated to the federal government are reserved to the states or the people (1791) - James Madison - Most impacted: State governments and individuals. Trick: Federal power ends at 10.",
        11: "Limits lawsuits against states (1795) - John Marshall - Most impacted: State governments. Trick: 1-on-1 disputes between citizens and states.",
        12: "Revises presidential election procedures (1804) - Thomas Jefferson - Most impacted: Presidential candidates and voters. Trick: 1 vote for president, 2 for VP.",
        13: "Abolition of slavery (1865) - Abraham Lincoln - Most impacted: Enslaved individuals. Trick: Unlucky 13 turned lucky for freedom.",
        14: "Equal protection under the law and due process for all citizens (1868) - John Bingham - Most impacted: Minorities and historically marginalized groups. Trick: 1 nation 4 equality.",
        15: "Right to vote cannot be denied based on race, color, or previous servitude (1870) - Ulysses S. Grant - Most impacted: African Americans and minorities. Trick: 15 freed votes.",
        16: "Congress can levy an income tax (1913) - William Howard Taft - Most impacted: Taxpayers. Trick: Sweet 16, but now you pay taxes.",
        17: "Establishes the direct election of U.S. Senators by popular vote (1913) - Woodrow Wilson - Most impacted: Voters. Trick: 17 senators closer to heaven (elected by people).",
        18: "Prohibition of alcohol (repealed by the 21st Amendment) (1919) - Wayne Wheeler - Most impacted: Alcohol producers and consumers. Trick: 18 is too young to drink.",
        19: "Women's right to vote (1920) - Susan B. Anthony - Most impacted: Women. Trick: 19 suffragettes on the march.",
        20: "Changes the dates of congressional and presidential terms (1933) - George Norris - Most impacted: Congress and the president. Trick: Jan 20 starts a new term.",
        21: "Repeal of Prohibition (18th Amendment) (1933) - Fiorello La Guardia - Most impacted: Alcohol producers and consumers. Trick: 21 means you can drink.",
        22: "Limits the President to two terms in office (1951) - Harry S. Truman - Most impacted: Presidential candidates. Trick: 2 terms for 22.",
        23: "Gives residents of Washington D.C. the right to vote for representatives in the Electoral College (1961) - Eleanor Holmes Norton - Most impacted: D.C. residents. Trick: 2-3 votes for D.C.",
        24: "Abolishes poll taxes (1964) - Lyndon B. Johnson - Most impacted: Low-income voters. Trick: 24 stops taxing at the door.",
        25: "Addresses presidential succession and disability (1967) - Birch Bayh - Most impacted: Presidential officeholders and their staff. Trick: 25 keeps the presidency alive.",
        26: "Voting age lowered to 18 (1971) - Jennings Randolph - Most impacted: Young voters. Trick: 2+6 = 18 to vote.",
        27: "Delays laws affecting Congressional salary from taking effect until after the next election of representatives (1992) - Gregory Watson - Most impacted: Members of Congress. Trick: 27 waits till the next election."
    }

    score = 0
    print("\nWelcome to the Amendments Quiz!")
    print("You will be given 10 descriptions of amendments. Your task is to enter the amendment number that matches the description.\n")
    
    for _ in range(10):  # Ask 10 random questions
        amendment, description = random.choice(list(questions.items()))
        try:
            answer = int(input(f"Which amendment is described as: \"{description}\"? Enter the amendment number: "))
            if answer == amendment:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is Amendment {amendment}.")
                print(f"Details: {answers[amendment]}")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"\nYour final score: {score}/10")
    if score == 10:
        print("Excellent! You know your amendments well!")
    elif score >= 7:
        print("Good job! A little more study and you'll be a pro.")
    else:
        print("Keep learning! The Constitution is worth knowing.")

# Call the function to start the quiz
amendments_quiz()
