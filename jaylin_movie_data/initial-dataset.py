import pandas as pd

## Making the columns
columns = [
    "scene_id",
    "movie_title",
    "release_year",
    "timestamp",
    "scene_description",
    "gender_stereotype",
    "discriminatory_action",
    "evidence",
    "reinforces_or_challenges"
]

## Adding data for Mulan
dataset = [
    {
        "scene_id": "MULAN-01",
        "movie_title": "Mulan",
        "release_year": 1998,
        "timestamp": "00:09:30–00:11:30",
        "scene_description": "The matchmaker judges whether Mulan would be a good wife.",
        "gender_stereotype": "Women should be obedient wives.",
        "discriminatory_action": ("Mulan's value is judged by her suitability for marriage."),
        "evidence": ("The matchmaker evaluates her appearance and behavior."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "MULAN-02",
        "movie_title": "Mulan",
        "release_year": 1998,
        "timestamp": "00:15:50–00:19:10",
        "scene_description": ("Mulan is prevented from joining the army because women are not allowed to become soldiers."),
        "gender_stereotype": "Women are too weak to fight.",
        "discriminatory_action": ("Mulan must disguise herself as a man to join the army."),
        "evidence": ("Only men are recruited, even though Mulan is willing and capable."),
        "reinforces_or_challenges": "Challenges"
},
    {
        "scene_id": "MULAN-03",
        "movie_title": "Mulan",
        "release_year": 1998,
        "timestamp": "00:38:10–00:41:20",
        "scene_description": ("Mulan struggles during military training but eventually completes the difficult challenges."),
        "gender_stereotype": ("Men are naturally stronger and better soldiers than women."),
        "discriminatory_action": ("Mulan can only receive military training while others believe she is a man."),
        "evidence": ("She succeeds by combining physical effort with intelligence and determination."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "MULAN-04",
        "movie_title": "Mulan",
        "release_year": 1998,
        "timestamp": "01:00:14–01:01:30",
        "scene_description": ("After Mulan is injured, the soldiers discover that she is a woman."),
        "gender_stereotype": ("A woman cannot be accepted as a legitimate soldier."),
        "discriminatory_action": ("Mulan is expelled from the army despite saving the soldiers from the Huns."),
        "evidence": ("Her achievements are dismissed once her gender is revealed."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "MULAN-05",
        "movie_title": "Mulan",
        "release_year": 1998,
        "timestamp": "01:06:34–01:07:26",
        "scene_description": ("Mulan warns the men that the Huns survived, but they refuse to listen to her."),
        "gender_stereotype": ("Women are less knowledgeable and authoritative than men."),
        "discriminatory_action": ("The men ignore Mulan's warning after learning that she is a woman."),
        "evidence": ("Mulan points out that the Huns are alive, but the male characters dismiss her information."),
        "reinforces_or_challenges": "Challenges"
    },


## Adding data for The Nightmare Before Christmas

    {
        "scene_id": "NBC-01",
        "movie_title": "The Nightmare Before Christmas",
        "release_year": 1993,
        "timestamp": "00:23:48–00:27:40",
        "scene_description": ("Dr. Finkelstein prevents Sally from leaving and expects her to obey him."),
        "gender_stereotype": ("Women should be obedient and controlled by male authority figures."),
        "discriminatory_action": ("Dr. Finkelstein restricts Sally's freedom and treats her as if she belongs to him."),
        "evidence": ("He confines Sally in his laboratory and attempts to control where she goes."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "NBC-02",
        "movie_title": "The Nightmare Before Christmas",
        "release_year": 1993,
        "timestamp": "00:37:05–00:37:51",
        "scene_description": ("Sally warns Jack that his Christmas plan will end badly, but Jack dismisses her concerns."),
        "gender_stereotype": ("Women's knowledge and warnings are less important than men's ideas."),
        "discriminatory_action": ("Jack ignores Sally's warning and continues with his plan."),
        "evidence": ("Sally explains that she had a troubling vision, but Jack does not seriously consider her concerns."),
        "reinforces_or_challenges": "Reinforces"
    },
    {
        "scene_id": "NBC-03",
        "movie_title": "The Nightmare Before Christmas",
        "release_year": 1993,
        "timestamp": "00:37:25–00:37:47",
        "scene_description": ("Jack asks Sally to make his Santa Claus outfit."),
        "gender_stereotype": ("Women are expected to perform sewing and clothing-related work."),
        "discriminatory_action": ("Sally is given a traditional domestic task while Jack leads the Christmas plan."),
        "evidence": ("Sally creates Jack's costume while he receives recognition as the leader of the project."),
        "reinforces_or_challenges": "Reinforces"
    },
    {
        "scene_id": "NBC-04",
        "movie_title": "The Nightmare Before Christmas",
        "release_year": 1993,
        "timestamp": "00:55:42–00:57:12",
        "scene_description": ("Sally uses her detached leg to distract Oogie Boogie."),
        "gender_stereotype": ("A woman's body can be used to distract or control a man."),
        "discriminatory_action": ("Oogie focuses on Sally's leg instead of treating her as a serious threat."),
        "evidence": ("He becomes distracted by the leg while Sally tries to rescue Santa."),
        "reinforces_or_challenges": "Reinforces"
    },
    {
        "scene_id": "NBC-05",
        "movie_title": "The Nightmare Before Christmas",
        "release_year": 1993,
        "timestamp": "00:27:28–00:27:40",
        "scene_description": ("Sally repeatedly escapes from Dr. Finkelstein and makes her own decisions."),
        "gender_stereotype": ("Women should remain dependent on male authority figures."),
        "discriminatory_action": ("Dr. Finkelstein tries to deny Sally independence because he believes he created and controls her."),
        "evidence": ("Sally secretly leaves the laboratory despite Dr. Finkelstein's efforts to confine her."),
        "reinforces_or_challenges": "Challenges"
    },
    ## Adding data from Frozen
    {
        "scene_id": "FROZEN-01",
        "movie_title": "Frozen",
        "release_year": 2013,
        "timestamp": "00:21:40–00:26:05",
        "scene_description": ("Anna meets Prince Hans and quickly believes that they have fallen in love."),
        "gender_stereotype": ("A princess needs romance and marriage to achieve happiness."),
        "discriminatory_action": ("Anna has learned to view marriage as one of the most important opportunities available to her as a princess."),
        "evidence": ("Anna agrees to marry Hans on the same day that she meets him."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "FROZEN-02",
        "movie_title": "Frozen",
        "release_year": 2013,
        "timestamp": "00:26:05–00:28:25",
        "scene_description": ("Elsa reveals her powers during her coronation and is accused of being a monster."),
        "gender_stereotype": ("Powerful women are dangerous and unable to control their emotions."),
        "discriminatory_action": ("The Duke of Weselton turns the crowd against Elsa and describes her as a threat."),
        "evidence": ("The Duke calls Elsa a monster after seeing her use her magical powers."),
        "reinforces_or_challenges": "Challenges"
    },
    {
    "scene_id": "FROZEN-03",
    "movie_title": "Frozen",
    "release_year": 2013,
    "timestamp": "01:03:00–01:06:30",
    "scene_description": ("The trolls try to convince Anna and Kristoff to get married."),
    "gender_stereotype": ("A woman needs marriage to solve her problems."),
    "discriminatory_action": ("The trolls mess up plan Anna's marriage without asking what she wants."),
    "evidence": ("They begin arranging a wedding even though Anna and Kristoff are not a couple."),
    "reinforces_or_challenges": "Reinforces"
    },
    {
        "scene_id": "FROZEN-04",
        "movie_title": "Frozen",
        "release_year": 2013,
        "timestamp": "01:15:15–01:17:10",
        "scene_description": ("Hans refuses to kiss Anna and reveals that he only planned to use her to gain control of the kingdom."),
        "gender_stereotype": ("A vulnerable princess can be manipulated through her desire for romance."),
        "discriminatory_action": ("Hans deceives Anna and uses the possibility of marriage to gain political power."),
        "evidence": ("Hans admits that he never loved Anna and planned to take control of Arendelle through marriage."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "FROZEN-05",
        "movie_title": "Frozen",
        "release_year": 2013,
        "timestamp": "01:26:15–01:28:05",
        "scene_description": ("Anna saves Elsa from Hans and discovers that an act of sisterly love can break the curse."),
        "gender_stereotype": ("A princess must be rescued by a male romantic partner."),
        "discriminatory_action": ("Anna is expected to depend on a man's kiss to survive instead of having the power to save herself or another person."),
        "evidence": ("Anna chooses to protect Elsa, and her own act of love breaks the curse without a prince rescuing her."),
        "reinforces_or_challenges": "Challenges"
    },
## Adding data from Shrek
    {
        "scene_id": "SHREK-01",
        "movie_title": "Shrek",
        "release_year": 2001,
        "timestamp": "00:18:06–00:20:05",
        "scene_description": ("Lord Farquaad chooses Princess Fiona as the woman he will marry so that he can become king."),
        "gender_stereotype": ("A princess's main purpose is to marry a powerful man."),
        "discriminatory_action": ("Farquaad treats Fiona as a way to gain power instead of allowing her to choose whether she wants to marry him."),
        "evidence": ("Farquaad selects Fiona from a group of princesses without meeting her or asking for her consent."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "SHREK-02",
        "movie_title": "Shrek",
        "release_year": 2001,
        "timestamp": "00:35:45–00:38:20",
        "scene_description": ("Fiona waits in a tower because she expects a brave prince to rescue her."),
        "gender_stereotype": ("Women are helpless and need men to rescue them."),
        "discriminatory_action": ("Fiona is placed in the passive role of waiting while a male hero is expected to save her."),
        "evidence": ("Fiona is surprised when Shrek does not behave like the romantic prince she expected."),
        "reinforces_or_challenges": "Reinforces"
    },{
        "scene_id": "SHREK-03",
        "movie_title": "Shrek",
        "release_year": 2001,
        "timestamp": "00:51:50–00:53:20",
        "scene_description": ("Fiona fights Robin Hood and his group by herself."),
        "gender_stereotype": ("Women are physically weak and unable to defend themselves."),
        "discriminatory_action": ("Robin Hood assumes that Fiona is helpless and needs to be rescued from Shrek."),
        "evidence": ("Fiona defeats Robin Hood and his group without assistance from Shrek or Donkey."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "SHREK-04",
        "movie_title": "Shrek",
        "release_year": 2001,
        "timestamp": "01:01:24–01:04:18",
        "scene_description": ("Fiona hides her ogre form because she thinks Shrek will reject her."),
        "gender_stereotype": ("Women must be physically beautiful to deserve love and acceptance."),
        "discriminatory_action": ("Fiona feels pressured to hide her appearance because she believes that an unattractive princess will be rejected."),
        "evidence": ("Fiona stays away from Shrek at night and describes her ogre appearance as a curse."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "SHREK-05",
        "movie_title": "Shrek",
        "release_year": 2001,
        "timestamp": "01:17:09–01:18:27",
        "scene_description": ("Farquaad insults Fiona after her permanent transformation into an ogre."),
        "gender_stereotype": ("A woman's value depends on meeting traditional standards of beauty."),
        "discriminatory_action": ("Farquaad rejects and humiliates Fiona because her appearance no longer matches his idea of a beautiful princess."),
        "evidence": ("Farquaad reacts with disgust when Fiona becomes an ogre in front of the wedding guests."),
        "reinforces_or_challenges": "Challenges"
    },
## Adding data for Aladdin
    {
    "scene_id": "ALADDIN-01",
    "movie_title": "Aladdin",
    "release_year": 1992,
    "timestamp": "00:12:40–00:15:30",
    "scene_description": "The Sultan tells Jasmine that she must choose a prince to marry.",
    "gender_stereotype": "A princess must marry a man chosen by tradition.",
    "discriminatory_action": "Jasmine is not allowed to decide whether she wants to get married.",
    "evidence": "The law requires her to marry a prince before her next birthday.",
    "reinforces_or_challenges": "Challenges"
    },
    {
    "scene_id": "ALADDIN-02",
    "movie_title": "Aladdin",
    "release_year": 1992,
    "timestamp": "00:15:30–00:17:30",
    "scene_description": "The Sultan pressures Jasmine after she rejects another prince.",
    "gender_stereotype": "A daughter should obey her father and accept a husband.",
    "discriminatory_action": "The Sultan places the marriage law above Jasmine's personal choice.",
    "evidence": "Jasmine says she does not want to be forced into marriage.",
    "reinforces_or_challenges": "Challenges"
    },
    {
    "scene_id": "ALADDIN-03",
    "movie_title": "Aladdin",
    "release_year": 1992,
    "timestamp": "00:52:30–00:54:30",
    "scene_description": "Jasmine hears Aladdin and the Sultan discussing who will marry her.",
    "gender_stereotype": "A princess is a prize that a man can win.",
    "discriminatory_action": "The men discuss Jasmine's marriage without including her in the decision.",
    "evidence": "Jasmine becomes angry and says that she is not a prize to be won.",
    "reinforces_or_challenges": "Challenges"
    },
    {
    "scene_id": "ALADDIN-04",
    "movie_title": "Aladdin",
    "release_year": 1992,
    "timestamp": "01:10:00–01:12:30",
    "scene_description": "Jafar decides that he will marry Jasmine so he can become Sultan.",
    "gender_stereotype": "A woman can be used by a man to gain power.",
    "discriminatory_action": "Jafar treats Jasmine as a way to control the kingdom.",
    "evidence": "He plans to marry her without caring about her choice or feelings.",
    "reinforces_or_challenges": "Challenges"
    },
    {
    "scene_id": "ALADDIN-05",
    "movie_title": "Aladdin",
    "release_year": 1992,
    "timestamp": "01:14:30–01:17:00",
    "scene_description": "Jafar controls Jasmine and treats her like his possession.",
    "gender_stereotype": "A powerful man is allowed to control a woman.",
    "discriminatory_action": "Jafar takes away Jasmine's freedom and forces her to serve him.",
    "evidence": "Jasmine is placed in chains and ordered to stay beside him.",
    "reinforces_or_challenges": "Challenges"
    },
## Adding data for Beauty and the Beast

    {
        "scene_id": "BATB-01",
        "movie_title": "Beauty and the Beast",
        "release_year": 1991,
        "timestamp": "00:07:00–00:08:10",
        "scene_description": "Gaston tells Belle that women should not read.",
        "gender_stereotype": "Women should not be educated or think for themselves.",
        "discriminatory_action": "Gaston criticizes Belle for reading because she is a woman.",
        "evidence": "He says that women should not read because they might start thinking.",
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "BATB-02",
        "movie_title": "Beauty and the Beast",
        "release_year": 1991,
        "timestamp": "00:08:10–00:09:10",
        "scene_description": "Gaston decides that he wants to marry Belle because she is beautiful.",
        "gender_stereotype": "A woman's appearance is more important than her personality.",
        "discriminatory_action": "Gaston treats Belle like a prize instead of caring about what she wants.",
        "evidence": "He says Belle is the best woman for him because she is the most beautiful.",
        "reinforces_or_challenges": "Reinforces"
    },
    {
        "scene_id": "BATB-03",
        "movie_title": "Beauty and the Beast",
        "release_year": 1991,
        "timestamp": "00:17:20–00:20:10",
        "scene_description": "Gaston proposes to Belle and describes the life he planned for her.",
        "gender_stereotype": "A wife should cook, clean, and take care of her husband and children.",
        "discriminatory_action": "Gaston plans Belle's future without asking what she wants.",
        "evidence": "He describes Belle cooking while taking care of their children and rubbing his feet.",
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "BATB-04",
        "movie_title": "Beauty and the Beast",
        "release_year": 1991,
        "timestamp": "00:27:20–00:30:50",
        "scene_description": "The people in the tavern praise Gaston for being strong and aggressive.",
        "gender_stereotype": "Men should be strong, aggressive, and dominant.",
        "discriminatory_action": "Gaston is praised for using strength and violence to prove that he is a man.",
        "evidence": "The song celebrates his fighting, hunting, muscles, and aggressive behavior.",
        "reinforces_or_challenges": "Reinforces"
    },
    {
        "scene_id": "BATB-05",
        "movie_title": "Beauty and the Beast",
        "release_year": 1991,
        "timestamp": "01:05:30–01:08:10",
        "scene_description": "Gaston pressures Belle to marry him by threatening her father.",
        "gender_stereotype": "A man is allowed to control a woman's choices.",
        "discriminatory_action": "Gaston uses Belle's father to pressure her into an unwanted marriage.",
        "evidence": "He offers to release her father only if Belle agrees to marry him.",
        "reinforces_or_challenges": "Challenges"
    },
## Adding data for Brave
    {
        "scene_id": "BRAVE-01",
        "movie_title": "Brave",
        "release_year": 2012,
        "timestamp": "00:08:00–00:10:00",
        "scene_description": ("Merida describes the lessons and expectations she must follow as a princess."),
        "gender_stereotype": ("A princess must be polite, proper, and prepared to behave like a traditional queen."),
        "discriminatory_action": ("Merida is given strict responsibilities and restrictions because she is a princess."),
        "evidence": ("Merida explains that she is expected to be an example and that her life has already been planned."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "BRAVE-02",
        "movie_title": "Brave",
        "release_year": 2012,
        "timestamp": "00:11:50–00:14:20",
        "scene_description": ("Merida learns that the clan leaders are bringing their sons to compete for her hand in marriage."),
        "gender_stereotype": ("A princess is expected to marry for her family's political interests."),
        "discriminatory_action": ("Merida's marriage is arranged without asking for her consent."),
        "evidence": ("Her parents announce that male suitors will compete for the right to marry her."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "BRAVE-03",
        "movie_title": "Brave",
        "release_year": 2012,
        "timestamp": "00:14:20–00:17:45",
        "scene_description": ("Queen Elinor tells Merida that accepting betrothal is part of her responsibility."),
        "gender_stereotype": ("Women must place family duty above their freedom and personal choices."),
        "discriminatory_action": ("Elinor dismisses Merida's objections and expects her to accept an unwanted marriage."),
        "evidence": ("Merida asks for freedom, but Elinor insists that she cannot escape her responsibilities."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "BRAVE-04",
        "movie_title": "Brave",
        "release_year": 2012,
        "timestamp": "00:22:47–00:26:45",
        "scene_description": ("Merida enters the archery competition and announces that she will compete for her own hand."),
        "gender_stereotype": ("Men compete while women remain passive prizes in marriage arrangements."),
        "discriminatory_action": ("The competition treats Merida as a reward for the male winner rather than as a participant."),
        "evidence": ("Merida enters the competition herself and defeats the male suitors in archery."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "BRAVE-05",
        "movie_title": "Brave",
        "release_year": 2012,
        "timestamp": "01:06:30–01:09:15",
        "scene_description": ("Merida argues that young people should choose whom they love instead of following arranged marriages."),
        "gender_stereotype": ("A princess must accept the husband selected through tradition."),
        "discriminatory_action": ("The traditional system denies Merida and the suitors control over their romantic futures."),
        "evidence": ("Merida proposes that everyone should write their own story and find love in their own time."),
        "reinforces_or_challenges": "Challenges"
    },
## Adding data for Tangled
    {
        "scene_id": "TANGLED-01",
        "movie_title": "Tangled",
        "release_year": 2010,
        "timestamp": "00:12:40–00:15:15",
        "scene_description": "Mother Gothel tells Rapunzel that she is too weak to leave the tower.",
        "gender_stereotype": "Young women are weak and cannot protect themselves.",
        "discriminatory_action": "Gothel uses Rapunzel's age and gender to make her feel helpless.",
        "evidence": "She calls Rapunzel fragile, immature, and unable to survive outside.",
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "TANGLED-02",
        "movie_title": "Tangled",
        "release_year": 2010,
        "timestamp": "00:22:55–00:23:24",
        "scene_description": "Mother Gothel refuses to let Rapunzel leave to see the floating lights.",
        "gender_stereotype": "Young women should stay home and obey their caregivers.",
        "discriminatory_action": "Gothel takes away Rapunzel's freedom and orders her to remain in the tower.",
        "evidence": "She tells Rapunzel that she is not strong enough to survive outside.",
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "TANGLED-03",
        "movie_title": "Tangled",
        "release_year": 2010,
        "timestamp": "00:26:16–00:27:25",
        "scene_description": "Flynn tries to charm Rapunzel after she captures him.",
        "gender_stereotype": "Women are easily persuaded by an attractive man.",
        "discriminatory_action": "Flynn assumes that his appearance will stop Rapunzel from questioning him.",
        "evidence": "Rapunzel ignores his attempt to charm her and continues asking questions.",
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "TANGLED-04",
        "movie_title": "Tangled",
        "release_year": 2010,
        "timestamp": "00:31:55–00:32:47",
        "scene_description": "Rapunzel feels guilty after leaving the tower.",
        "gender_stereotype": "A good daughter should always obey her caregiver.",
        "discriminatory_action": "Gothel's treatment makes Rapunzel believe that wanting freedom makes her a bad daughter.",
        "evidence": "Rapunzel celebrates being free but then feels guilty for disobeying Gothel.",
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "TANGLED-05",
        "movie_title": "Tangled",
        "release_year": 2010,
        "timestamp": "01:17:40–01:19:20",
        "scene_description": "Rapunzel learns the truth and confronts Mother Gothel.",
        "gender_stereotype": "A young woman cannot make decisions without an older person controlling her.",
        "discriminatory_action": "Gothel tries to silence Rapunzel and continue controlling her choices.",
        "evidence": "Rapunzel rejects Gothel's lies and refuses to let her use her hair again.",
        "reinforces_or_challenges": "Challenges"
    },
## Adding data for The Princess and the Frog
    {
    "scene_id": "PATF-01",
    "movie_title": "The Princess and the Frog",
    "release_year": 2009,
    "timestamp": "00:13:00–00:15:20",
    "scene_description": ("Tiana's mother tells her that she wants grandchildren."),
    "gender_stereotype": ("A woman is expected to get married and start a family."),
    "discriminatory_action": ("Tiana is pressured to focus on marriage instead of only working toward her restaurant."),
    "evidence": ("Her mother reminds her that her father wanted more for her than working all the time."),
    "reinforces_or_challenges": "Challenges"
    },
    {
    "scene_id": "PATF-02",
    "movie_title": "The Princess and the Frog",
    "release_year": 2009,
    "timestamp": "00:18:30–00:21:30",
    "scene_description": ("Naveen plans to marry a wealthy woman so he can continue living without working."),
    "gender_stereotype": ("A wealthy woman can be used by a man for her money."),
    "discriminatory_action": ("Naveen views marriage as a way to gain access to a woman's wealth."),
    "evidence": ("He plans to marry Charlotte because her family is wealthy, not because he loves her."),
    "reinforces_or_challenges": "Reinforces"
    },
    {
        "scene_id": "PATF-03",
        "movie_title": "The Princess and the Frog",
        "release_year": 2009,
        "timestamp": "00:23:20–00:24:50",
        "scene_description": ("The Fenner brothers tell Tiana that another buyer has offered more money for the restaurant property."),
        "gender_stereotype": ("A woman from Tiana's background is incapable of running a successful business."),
        "discriminatory_action": ("The businessmen question Tiana's ability to operate the restaurant and refuse to honor their original agreement."),
        "evidence": ("They call her a little woman and say that someone from her background would struggle to run a large business."),
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "PATF-04",
        "movie_title": "The Princess and the Frog",
        "release_year": 2009,
        "timestamp": "00:27:40–00:32:00",
        "scene_description": ("Naveen mistakes Tiana for a princess because she is wearing a formal dress."),
        "gender_stereotype": ("A woman wearing an elegant dress must be a princess seeking romance."),
        "discriminatory_action": ("Naveen assumes Tiana will kiss him and help him without first listening to who she is."),
        "evidence": ("Tiana explains that she is a waitress and initially refuses to kiss Naveen."),
        "reinforces_or_challenges": "Challenges"
    },
    {
    "scene_id": "PATF-05",
    "movie_title": "The Princess and the Frog",
    "release_year": 2009,
    "timestamp": "01:28:00–01:31:15",
    "scene_description": "Tiana makes the Fenner brothers sell her the property and opens her restaurant.",
    "gender_stereotype": "A woman like Tiana cannot own and manage a successful business.",
    "discriminatory_action": "The Fenner brothers try to keep the property from Tiana because they doubt her ability to run the restaurant.",
    "evidence": "Tiana proves them wrong by buying the property and opening a successful restaurant.",
    "reinforces_or_challenges": "Challenges"
    },
## Adding data for Cinderella

    {
        "scene_id": "CINDERELLA-01",
        "movie_title": "Cinderella",
        "release_year": 1950,
        "timestamp": "00:09:30–00:13:00",
        "scene_description": "Cinderella begins her day by doing chores for her stepfamily.",
        "gender_stereotype": "Women are expected to cook and clean for others.",
        "discriminatory_action": "Cinderella's stepfamily forces her to perform all the housework.",
        "evidence": "She prepares breakfast, cleans the house, and serves her stepfamily.",
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "CINDERELLA-02",
        "movie_title": "Cinderella",
        "release_year": 1950,
        "timestamp": "00:19:30–00:22:30",
        "scene_description": "Lady Tremaine gives Cinderella more chores when she asks to attend the ball.",
        "gender_stereotype": "A young woman in a lower position should obey and serve others.",
        "discriminatory_action": "Lady Tremaine uses housework to prevent Cinderella from having the same opportunity as her daughters.",
        "evidence": "She gives Cinderella a long list of work that must be finished before the ball.",
        "reinforces_or_challenges": "Challenges"
    },
    {
        "scene_id": "CINDERELLA-03",
        "movie_title": "Cinderella",
        "release_year": 1950,
        "timestamp": "00:29:30–00:32:30",
        "scene_description": "The stepsisters destroy Cinderella's dress before the ball.",
        "gender_stereotype": "Women must compete against each other for a man's attention.",
        "discriminatory_action": "The stepsisters attack Cinderella because they see her as competition for the prince.",
        "evidence": "They tear apart her dress so she cannot attend the ball.",
        "reinforces_or_challenges": "Reinforces"
    },
    {
        "scene_id": "CINDERELLA-04",
        "movie_title": "Cinderella",
        "release_year": 1950,
        "timestamp": "00:54:00–00:57:00",
        "scene_description": "The Grand Duke searches for the woman who can fit the glass slipper.",
        "gender_stereotype": "A woman's future depends on being chosen by a prince.",
        "discriminatory_action": "The search treats marriage to the prince as the main opportunity available to the women.",
        "evidence": "Every eligible woman is expected to try on the slipper for the chance to marry him.",
        "reinforces_or_challenges": "Reinforces"
    },
    {
        "scene_id": "CINDERELLA-05",
        "movie_title": "Cinderella",
        "release_year": 1950,
        "timestamp": "01:06:00–01:09:00",
        "scene_description": "Lady Tremaine locks Cinderella in her room to keep her from trying on the slipper.",
        "gender_stereotype": "A woman can control another woman's opportunities to improve her own daughters' chances.",
        "discriminatory_action": "Lady Tremaine takes away Cinderella's freedom and prevents her from meeting the Duke.",
        "evidence": "She locks the door after realizing that Cinderella is the woman the Duke is searching for.",
        "reinforces_or_challenges": "Challenges"
    },
]

data = pd.DataFrame(dataset, columns = columns)

data.to_csv("movies-data.csv", index = False)

print(data)
print("\nDataset successfully saved as movies-data.csv")
print(f"Number of rows: {len(data)}")