# Boardman 

def main():
  while True:

    print("Welcome junior! I am Coach Casey, but most people just call my Coach C. I am the head coach of the Christansen High Cheetah's Varsity Basketball Team. Lucky you, you were our last walk-on. However, that means that you will have to prove yourself off the bench. But, through hard work, concentration, and good decision-making, I am sure you will peform to the best of your ability. Let's get started! ")

    print()

    name = input("Please enter your player name: ")
    number = int(input("Please enter your player number: "))

    if number <= 99:
      pass

    elif number >= 99:
      print("That is not a valid number.")
      break

    print()

    print(f"Welcome, {name}! Your number is {number}.")

    print()

    print(f"""Game 1 of Regular Season
  
                  Record: 0-0
                  Opponent: Darwin Lake Demons
                  Score: 55-36
                  Time: 1:49 left in 4Q
                  {name}'s Playing Status: Bench   """)

    print()

    print("Coach C: Alright junior, we're up 55-36 with less than 2 minutes left to play. Get on the floor and close out the game for us! ")

    print()

    print(f"""[The Substitution Buzzer sounds]
          Referee: Alright, Christansen number 7 off, 
          Christansen number {number} on. """)

    print()

    try:
      darwin = int(input("""You are playing the position of point guard. The Cheetah power forward, DeAndrey Ayton, comes over and sets a screen for you. Do you:
  
    [1] Run the pick and roll with Ayton
    [2] Use the screen to your advantage and drive to the basket
    [3] Put up a three-pointer
  
    Please enter the number of your choice: """))
      print()

    except ValueError:
      print("Not valid")
      break
  
    print()

    if darwin == 1:
      print("""You feed a nice pass to Ayton who flushes the bucket with ease.
      Coach C: Good play junior! 
      Ayton: Nice call, rookie. """)

    elif darwin == 2:
      print("""You drive to the basket hard and rise up  for the layup. However, one of the Demons players rises up to meet you and blocks your shot. 
      Coach C: Nice try, junior.""")

    elif darwin == 3: 
        print("""You pull up from way beyond the arc and   give the shot an expert release. SWISH. Nothing but net.
        Bench: Buckets! 
        Coach C: COME ON JUNIOR, DON'T TAKE DIFFICULT SHOTS LIKE THAT!""")

    print()

    try:
      darwin2 = int(input("""The shooting guard, Troy Nordstrom, is just outside the key. The opposition knows he is a scoring threat, and your defender is drifting away from you to double team Troy. Do you: 
  
    [1] Run to face him and take a three-pointer
    [2] Go for a backdoor cut and drive to the basket
    [3] Just stand a watch
  
    Please enter the number of your choice: """))
      print()

    except ValueError:
      print("Not valid")
      break
  
      print()

    else:
      if darwin2 == 1:
        print("""Troy feeds you a risky bounce pass through the legs of the defender. You pull up for three but it hits the rim and out.
      Coach C: Hustle back rookie to play D!""")

      elif darwin2 == 2:
        print(f"""Troy gives a nifty little bounce pass behind his back and you drive to the basket and lay it in, uncontested.
        Troy: Good call, {name}
        Coach C: Good play!""")

      elif darwin2 == 3:
        print("""Troy is double teamed and forced to hold onto it for a held ball call.
        Troy: Help me out!
        Coach C: Come on, {name}, don't just ball watch!""") 

    print()

    try:
      darwin3 = int(input("""There is 10.3 seconds left on the game clock and the score is 60-42. Do you:
    
      [1] Dribble out the clock
      [2] Play with the opposition and go up for the buzzer beater for three
    
      Please enter the number of your choice: """))

      print()

    except ValueError:
      print("Not valid")
      break

      print()

    else:
      if darwin3 == 1:
        print("""You just dribble out the ball. The buzzer sounds and the ref's whistle blows for the game.
        Coach C: Good sportmanship, junior!""")

      elif darwin3 == 2:
        print("""You pull up for the three just as the buzzer sounds, but it is heavily contested by the defender and blocked. You fall and he stands over you.
        Demons Player: Classless""")

    print()

    print("""You spend the next 5 games of the season playing primarily off the bench. You accumulate a total of 23 points, 15 assists, and 10 rebounds over 21 minutes over the 5 games. This is until the second-last game of the regular season when disaster strikes the team. Your star point guard and team captain, Kawai Lenerd goes down with an ACL tear with 2:23 left in a crucial game. If your team wins this game, you are guaranteed first in the league. Coach C puts you on as you are the backup point guard.""")

    print()

    print(f"""Game 7 of Regular Season
    
                Record: 6-0
                Opponent: Huntington Hounds
                Score: 62-64
                Time: 2:23 left in 4Q
                {name}'s Playing Status: Emergency Subsitution""")

    print()

    print("Coach C: Alright junior. We will run the pick and rolls with Ayton. There is no need to rush; there is plenty of time left. If the pick and roll is not possible, play the high ball screens and the split, and try to make open shots. Alright? You got this junior. Ready?! Cheetah on me, Cheetah on 3!")

    print()

    print(f"""[The Substitution Buzzer Sounds]
          Referee: Two timeouts left for Christansen. Christansen 2 off, Christansen {number} on.""")

    print()

    try: 
      hunt = int(input("""You dribble the ball up the court. The defence seems to anticipate the pick and roll coming, and thus they play a box-and-one defence. You have no choice but to start moving the ball. Do you:
      
      [1] Give a high lob down to Ayton in the post
      [2] Feed Nordstrom a quick pass for a pull up shot
      [3] Drive the bucket and try to draw a foul
      
      Please enter the number of your choice: """))
      print()

    except ValueError:
      print("Not valid")
      break

      print()

    else:
      if hunt == 1:
        print(f"""Your lob is well read by the defence and they deflect it and get a steal.
        Coach C: Come on rookie! Play short passes!
        Ayton: Hustle back, {name}!""")

      elif hunt == 2:
        print("""You give a good pass to Nordstrom as he runs towards you. He pulls up and drains the three.
        Bench: Trey!!!""")

      elif hunt == 3:
        print(f"""You rush the bucket, and a defender steps in your way. You both knock into each other and fall hard to the grouond. The ref's whistle blows. 
        Referee: Charging, Christansen {number}! 1st personal, 3rd team!
        Coach C: Are you kidding me ref?!""")

    print()

    try:
      hunt2 = int(input("""There are 1:19 left in the 4th quarter. The score is against your favour, 68-70. Ayton is at the line, shooting two free throws. He makes the first one. 69-70. However, he misses the second one, and there is a scramble for the rebound. Do you: 
      
      [1] Take a position at the point and hope for an outbound pass
      [2] Run into the scramble for the rebound
      
      Please enter the number of your choice: """))
      print()

    except ValueError:
      print("Not valid")
      break

      print()

    else:
      if hunt2 == 1:
        hunt2o = int(input("""The small forward, Andre Iverson, gets the rebound for the Cheetah and throws an outbound pass to you. Do you: 
        [1] Take a quick 3-point shot
        [2] Drive back into the paint and look for someone to pass to
        [3] Take a shot fake, dribble to the right, and take the 3-point shot
        
        Please enter the number of your choice: """))
        print()

        if hunt2o == 1:
          print("You take a quick three point shot but it hits the back of the rim and bounces back out.")

        elif hunt2o == 2:
          print("You go back into the paint and look to pass. You spot Ayton down in the post and pass it to him. He attempts a diffcult right hook but it bounces off the rim.")

        elif hunt2o == 3:
          print("""You fake the shot and take one dribble to your right. Through the corner of your eye, you can see that the defender took the fake and they fly past you. You set your feet and put it up from downtown. It bounces off the front of the rim, goes up, then falls back down into the basket. 
          Bench: HE'S A SHOOTER!""")

      elif hunt2 == 2:
        print("You run into the paint, looking for the rebound. However, there are too many bodies and you lose your sense of surrounding. The Hounds rebound the ball and run back the other way for a fast-break point.")

    print()

    try: 
      hunt3 = int(input(f"""There are 6.3 seconds left on the game clock and you guys are down 73-75. Coach C calls your last timeout.
      Referee: Christansen, last timeout charged
      Coach C: Alright, listen up! Bogut, you'll inbound the ball. I want Ayton down low to possibly get a pass down into the post. Iverson, stay high so you can set a screen for a possible long shot. Try to open up room for Troy; we'll pass to either him or {name}. {name}, stay on the right point and get ready to take the shot. Alright?! We can do this! Cheetah on me, Cheetah on 3!
      [The Substitution Buzzer sounds]
      Bogut has the ball in his hands. He finds a slightly open Troy and gives it to him. However, Troy is almost immediately double teamed. Do you: 
      [1] Run over to him and set your feet for the feed
      [2] Cut towards the basket
      
      Please enter the number of your choice: """ ))

      print()

    except ValueError:
      print("Not valid")
      break

    else:
      if hunt3 == 1:
        print("""Troy manages to thread a pass through the legs of the defender to you as you set your feet. You pull up for the shot. The ball flies through the air as time expires.
        Time seems to stand still.
        The ball is still flying with backspin.
        It hits the rim.
        And bounces off.""")

      if hunt3 == 2 :
        print("You cut towards the net. Troy somehow manages to get a desperate bounce pass to you. There's no time left for a dribble. You put up a high floater, but one of the defenders gets a finger tip on it.")

    print()

    print(f"""Final Game of Regular season
    
                Record: 6-1
                Opponent: Albany Blades
                Score: 0-0
                Time: 12:00 left in 1Q
                {name}'s Playing Status: Starter""")

    print()

    print("""With Lenerd out, you are now thrown into the starting position. You have been working with Coach C lately to improve your game. This game is crucial. You are playing your archrival in Albany, and they are tied with you for first with a record of 6-1. Whoever wins this game will secure a bye in the Quarterfinals and automically move on to the Semifinals.
    Coach C: Alright gentlemen, we know what is at stake here. A ticket to the Semifinals, and not having to play a difficult Quarterfinal match. More importantly, this is Albany we're playing. This is about pride. We all know the pain of the loss last year. Let's redeem ourselves this year! Alright?! I have faith in this group. Ready?! Cheetah on me, Cheetah on 3!""")

    print()

    try:
      alb = int(input("""You guys start off strong and take a solid 9-point lead going into halftime. However, the Blades battle back and go on an 11-0 round to start the second half, and now the Cheetah trail by 2. You must stop their momentum flow. You dribble the ball up the court. Do you: 
      
      [1] Drive straight to the basket and try to draw the foul
      [2] Try the pick and roll with Ayton
      [3] Pass to Iverson
      
      Please enter the number of your choice: """))
      print()

    except ValueError:
      print("Not valid")
      break

    else:
      if alb == 1:
        print("""You drive to the basket and euro step around the defender. There is plenty of contact, but you fight through and lay it up and in. The referee's whistle blows for a defensive blocking foul.
        Bench: AND ONE!""")

      elif alb == 2:
        print("""You call for the pick from Ayton. He sets the screen and you drive to the basket, then give a nice pass to him. He flushes the basket for two.
        Coach C: Good call, junior!""")

      elif alb == 3:
        albo = int(input("""You give the pass to Iverson who drives to the net. However, his layup is too heavily contested, and he throws a pass back to you. There are 6 seconds left on the shot clock. Do you: 
        
        [1] Pull up for the three-pointer
        [2] Drive up and put up a floater or pull up jumpshot
        
        Please enter the number of your choice: """))

        if albo == 1:
          print("""You put up a long three as the shotlock ticks down. This is something you worked with Coach C on. SWISH. Nothing but net.
          Bench: TREY!""")

        elif albo == 2:
          print("You drive to the basket and put up a heavily contested floater as time expires. The ball hits the front of the rim, but you get the shooter's bounce and it drops in.")

    print()

    try:
      alb2 = int(input("""The score is 68-68 with 2:00 left in the game. This is a crucial possession for your team. The ball is in your hands. Do you: 
      
      [1] Drive to the foul line, cross back, and fade for the 3-pointer
      [2] Wait at the point and wait for the pick and roll
      [3] Hand it off to Nordstrom
      
      Please enter the number of your choice: """))
      print()

    except ValueError:
      print("Not valid")
      break

    else:
      if alb2 == 1:
        print("""You bring out to the nifty moves, cross over, and fade back for the difficult three. SWISH. Nothing but the bottom of the net. You are on absolute fire!
        Bench: HE'S A SHOOTER!""")

      elif alb2 == 2:
        print("You signal for the pick. Iverson comes over and sets the screen. You flip it over to him and he flushes it with the and 1.")

      elif alb2 == 3:
        print("You signal to Troy to come over. He comes by and you set the screen for him. He pulls up, heavily off balance, but it doesn't matter. He swishes it for 3 points.")

    print()

    try:
      alb3 = int(input("""It is the dying seconds of the game. There are 3.2 seconds left on the game clock and the score is in your favour, 80-79. You must get a stop, as it is Blades ball. They inbound the ball to their sharpshooter, Wong. He is automatically double teamed by Nordstrom and Iverson. He throws a desperate past to the center Steiner. He only has enough time to take a quick 3-pointer. You are closest one to defend him. Do you:
      
      [1] Put a hand in front of his face to obscure his vision
      [2] Fly up and forwards to make contact with the ball
      
      Please enter the number of your decision: """))
      print()

    except ValueError:
      print("Not valid")
      break 

    else:
      if alb3 == 1:
        print("You put your hand up in his face. He puts up the shot...and bricks it. It's over! Your team finishes first in the conference and secures a Quarterfinals bye!")

      elif alb3 == 2:
        print("""You fly towards him to make contact to the ball. Steiner is just about to release when he knock it out of his hands. Time expires. CONGRATULATIONS! You have just secured your team a Quarterfinals bye!
        Coach C: GREAT DEFENSIVE PLAY!
        Bench: GET THAT GARBAGE OUTTA HERE!""")

    print()

    print("So, your team awaits the winner of the Quarterfinals match between Almadea and Holy Cross to see who you will play in the Semifinals. Almadea lead by as much as 15 points, but Holy Cross came storming back in the second half to win the game 89-86.")

    print()

    print(f"""Semifinals
    
                Record: 7-1 (1st in Western Conference)
                Opponent: Holy Cross (5-3, 3rd Western Conference)
                Score: 53-50
                Time: 12:00 left in 3Q
                {name}'s Playing Status: Bench """)

    print()

    print("Coach C makes the decision to bench you as you are suffering from heavy fatigue having played those big minutes the game before.")

    print()

    print(f"Coach C: Alright {name}! Ford is getting pretty tired right now, so time for you to go on. This game is back and forth, so every possession is crucial. Let your training speak for you. Alright?! Now go get it!")

    print()

    print(f"""[The Substitution Buzzer sounds]
          Referee: Christansen 18 off, Christansen {number}on.""")

    print()

    try:
      hc = int(input("""The score is now 66-60 in your favour with 4:53 left in the fourth. Time cannot tick any faster. Iverson inbounds the ball to you and you dribble it up the court. The play is set as a pick and roll. Do you:
      
      [1] Start the pick and roll with Iverson
      [2] Entertain the cut by Ayton
      [3] Set up Troy
      
      Please enter the number of your choice: """))
      print()

    except ValueError:
      print("Not valid")
      break

    else:
      if hc == 1:
        print("You start the pick with Iverson. He rushes up the lane and plays through the contact for the bucket and 1.")

      elif hc == 2:
        print("Ayton starts cutting to the net, and you feed him a nice bounce pass. However, the Holy Cross defender somehow read the play and feel backwards to intercept the pass.")

      elif hc == 3:
        print("""You hand the ball off the Troy Nordstrom and set the screen for him. He pulls up from almost the logo and splashes it for 3.
        Bench: SNIPER!""")

    print()

    try:
      hc2 = int(input("""There are only 10.1 seconds left on the clock, and you trail the game 76-77. It is your possession. Coach C calls your second-last timeout.
      Referee: Christansen charged with sixth timeout.
      Coach C: Okay, so we're down one. Try to be aggressive with the ball. Play it in the paint and only pass to the perimetre if their is no other option. Try to get a foul. Alright?! Let's punch our ticket to the finals! CHEETAH ON ME, CHEETAH ON 3!
      
      [The Substitution Buzzer sounds]
      
      Bogut inbounds the ball to Nordstrom. However, it goes off Troy's fingers weirdly and bounces away. There is a scramble for the ball, and time is ticking away! You see that Iverson almost has possession. Do you:
      
      [1] Join in the scramble
      [2] Signal for a timeout
      
      Please enter the number of your choice: """))
      print()

    except ValueError:
      print("Not valid")
      break

    else:
      if hc2 == 1:
        print("You help secure possession with Iverson, and look desperately for a play. Luckily, Nordstrom calls for a timeout with 3.5 seconds left.")

      elif hc2 == 2:
        print("You signal to the ref for timeout as you see Iverson's hands secure the ball. He blows his whistle. There are 4.3 seconds left on the clock.")

    print()

    print("""Referee: Christansen charged with last timeout. 
    Coach C: Alright, there is still enough time to get a pass and even a dribble. Set up screens for Troy; he'll be the best option to take the shot. Say a prayer to our heavenly father, and have faith in yourselves. Alright?! CHEETAH ON ME, CHEETAH ON 3!
    
    [The Substitution Buzzer sounds]
    
    You watch as Bogut inbounds the ball. Iverson sets up two screens to give Troy just enough space to work. 
    He pulls up.
    The ball spins through the air.
    Time and space seems to stop. 
    SPLASH.""")

    print()

    print(f"""Prefecture finals
    
              Record: 7-1 (1st in Western Conference)
              Opponent: St. Francis (8-0, 1st Overall)
              )
              Score: 0-0
              Time: 12:00 left in 1Q
              {name}'s Playing Status: Starter""")

  








if __name__ == "__main__":
  main()
