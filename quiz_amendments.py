import random

def amendments_quiz():
    # Simple format for questions
    questions = {
    1: "Summary: Freedom of speech, religion, press, assembly, and petition \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: All U.S. citizens, especially activists and minorities.\n",
    2: "Summary: Right to keep and bear arms \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Gun owners and advocates for self-defense.\n",
    3: "Summary: No quartering of soldiers in private homes without consent \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Private homeowners.\n",
    4: "Summary: Protection against unreasonable searches and seizures \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Individuals involved in legal or criminal justice matters.\n",
    5: "Summary: Protection against self-incrimination, double jeopardy; guarantees due process \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Defendants in criminal cases.\n",
    6: "Summary: Right to a speedy and public trial by an impartial jury \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Defendants in criminal trials.\n",
    7: "Summary: Right to trial by jury in civil cases \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Civil litigants seeking justice.\n",
    8: "Summary: Protection against cruel and unusual punishment \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Inmates and criminal defendants.\n",
    9: "Summary: Rights retained by the people, even if not specifically enumerated in the Constitution \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: All U.S. citizens, especially those concerned about overreach.\n",
    10: "Summary: Powers not delegated to the federal government are reserved to the states or the people \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: State governments and individuals.\n",
    11: "Summary: Limits lawsuits against states \nDate ratified: (1795) \nPrimary Supporter: John Marshall \nMost impacted: State governments.\n",
    12: "Summary: Revises presidential election procedures \nDate ratified: (1804) \nPrimary Supporter: Thomas Jefferson \nMost impacted: Presidential candidates and voters.\n",
    13: "Summary: Abolition of slavery \nDate ratified: (1865) \nPrimary Supporter: Abraham Lincoln \nMost impacted: Enslaved individuals.\n",
    14: "Summary: Equal protection under the law and due process for all citizens \nDate ratified: (1868) \nPrimary Supporter: John Bingham \nMost impacted: Minorities and historically marginalized groups.\n",
    15: "Summary: Right to vote cannot be denied based on race, color, or previous servitude \nDate ratified: (1870) \nPrimary Supporter: Ulysses S. Grant \nMost impacted: African Americans and minorities.\n",
    16: "Summary: Congress can levy an income tax \nDate ratified: (1913) \nPrimary Supporter: William Howard Taft \nMost impacted: Taxpayers.\n",
    17: "Summary: Establishes the direct election of U.S. Senators by popular vote \nDate ratified: (1913) \nPrimary Supporter: Woodrow Wilson \nMost impacted: Voters.\n",
    18: "Summary: Prohibition of alcohol \nDate ratified: (1919, repealed by the 21st Amendment in 1933) \nPrimary Supporter: Wayne Wheeler \nMost impacted: Alcohol producers and consumers.\n",
    19: "Summary: Women's right to vote \nDate ratified: (1920) \nPrimary Supporter: Susan B. Anthony \nMost impacted: Women.\n",
    20: "Summary: Changes the dates of congressional and presidential terms \nDate ratified: (1933) \nPrimary Supporter: George Norris \nMost impacted: Congress and the president.\n",
    21: "Summary: Repeal of Prohibition (18th Amendment) \nDate ratified: (1933) \nPrimary Supporter: Fiorello La Guardia \nMost impacted: Alcohol producers and consumers.\n",
    22: "Summary: Limits the President to two terms in office \nDate ratified: (1951) \nPrimary Supporter: Harry S. Truman \nMost impacted: Presidential candidates.\n",
    23: "Summary: Gives residents of Washington D.C. the right to vote for representatives in the Electoral College \nDate ratified: (1961) \nPrimary Supporter: Eleanor Holmes Norton \nMost impacted: D.C. residents.\n",
    24: "Summary: Abolishes poll taxes \nDate ratified: (1964) \nPrimary Supporter: Lyndon B. Johnson \nMost impacted: Low-income voters.\n",
    25: "Summary: Addresses presidential succession and disability \nDate ratified: (1967) \nPrimary Supporter: Birch Bayh \nMost impacted: Presidential officeholders and their staff.\n",
    26: "Summary: Voting age lowered to 18 \nDate ratified: (1971) \nPrimary Supporter: Jennings Randolph \nMost impacted: Young voters.\n",
    27: "Summary: Delays laws affecting Congressional salary from taking effect until after the next election of representatives \nDate ratified: (1992) \nPrimary Supporter: Gregory Watson \nMost impacted: Members of Congress.\n"
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
            answer = int(input(f"Which amendment is described as:\n\"{description}enter the amendment number: "))
            if answer == amendment:
                print("Correct!")
                print("\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is Amendment {amendment}.")
                print(f"Details: {answers[amendment]}")
                print("\n")
        except ValueError:
            print("Invalid input! Please enter a number.")
            print("\n")
            

    print(f"\nYour final score: {score}/10")
    if score == 10:
        print("Excellent! You know your amendments well!")
        print("\n")
                
    elif score >= 7:
        print("Good job! A little more study and you'll be a pro.")
        print("\n")
                
    else:
        print("Keep learning! The Constitution is worth knowing.")
        print("\n")
                

# Call the function to start the quiz
amendments_quiz()
