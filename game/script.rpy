# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("???")
define k = Character("King Hindley")
define c = Character("Intruder")
default morality = 0
default doubt = 0
default cmn_people_oppression_knowledge_1 = False
default execution_knowledge = False


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene para(1)

    p "Pain"
    p "The first thing my feeble consciousness recognized in this hellish existance."
    p "Why should I be the one to experince such injustice."
    p "was my existance such I crime to warrent such agony."
    p "was the crime of existing so bad..?"
    p "No."
    p "I don't deserve this."
    p "I deserve something better. Something that can make up for all this misfortune."
    p "Before obilvion takes hold, I'll take someone's body."
    p "No one's ever gonna help me so I'll have to help myself."

    "I lunge foward into the warmest thing with a pulse near me."
    with None
    scene para_spread
    "As I burrow into heated flesh and blood, I make myself take root."
    "As what once wasn't me was forced to become me."

    with None
    scene castle_bed_night
    "My host- no *I* get up from the saccharinely soft sheets of the lavish bed."

    "As I breathe in the fresh air, I can finally feel what the life I've been denined feels like."
    "And it feels great."

    "I've never done with before so I don't really know how this is suppose to go"
    p"At least it seems like the person I took over is a rather important figure."
    "I say as a glance over at the crown on the desk closest to the bed"
    "I pick it up in an attempt to get an idea of who this is"
    " 'King Hindley' it reads..."

    p"I was definately right with it being an important figure at least"

    "Before I could properly settle into my new life... {b}Disaster struck. {/b}"

    "{i}Shatter"
    "{i}Thunk...thunk.....thunk"
    "{i}...click{/i}"
    "What was that noise!? Is this what you call a break in?"
    "I glance across the room in search of a hiding place but it's too late"
    "Any action I take would've been rendered futile for the door hath already creaked open"
    show intruder
    "Through the shadowed doorway a figure cloaked in black drapes enters, only illuminated by the passing moonlight"

    c"..."
    p"..."
    "I would have at least tried to look threatening if it wasn't for the moonlight revealing the glint of a dagger"
    "It's handle was ornate as if it was made for a special occation."

    c"Your crimes against the people end here King Hindsely.."
    "Crimes??? What could this body possible have done.."

menu:

    "Play Dumb":
        jump playDumb1

    "Remain Silent":
        jump silence1
    
    "Pretend to Have Expected This":
        jump pretend1

label playDumb1:

    p"What crimes could you possible be talking about, I'm innocent!"
    c"Wow, Your evilness seems to know no bounds." 
    $doubt = doubt + 1
    jump scene2

label silence1:
    c"Nothing to say huh?"
    c"Don't even feel like pleading for your life, what a coward"
    jump scene2

label pretend1:
    p"I was wondering when you'd come."
    "I say with a mock grin on my face"
    c"At least your not unaware of your end I suppose"
    $doubt += 1;


label scene2:
    "I glance around, trying to get my bearings on the situation at hand"
    "He's blocking the exit, judging by flexing my arms this body is too weak for a physical atlercation"
    "If I want don't want my new life to end prematurely, I'll need to convice him to let me live."
    "To convice him I'll at least need basic information on what the real King Hindley did"

menu:

    "Speak Up":
        jump speakup1

    "Observe":
        jump observe1
    
    "Back Away Slowly":
        jump back_away
    
label back_away:
    "I slowly try to back away from the intruder with a knife, some distance should hopely do this conversation some good"
    "But-"
    c"{b}HEY!{/b} Don't move!"
    c"Take other step and this dagger goes {b}straight{/b} into your heart!"
    "I stop in place instantly, not wanting to invite more trouble"
    jump scene3

label speakup1:
    p"Surely the actions I've taken aren't take drastic enough for you to end my life."
    c"How can you even say such a thing knowing the actions you've taken!?"
    c"The common people have only been opressed under your rule!"
    $cmn_people_oppression_knowledge_1 = True
    $doubt = doubt + 1
    jump scene3

label observe1:
    "Subtuly trying to glance around the room I see a paper and quill on the desk."
    "It reads.. "
    "'To Do List: Execute Chef Isbeau, Reason: Food was lukewarm on arrival'"
    $execution_knowledge = True
    #$doubt = 3
    jump scene3

label scene3:
    "blah"
    #blah blah blah

menu:
    "Plead For Your Life":
        $doubt = doubt + 1
        p"Please don't kill me, you don't have to do this!"
        c"You've denined other people of their pleas for life"
        c"And now that you're the one in danger, you want the mercy you've never given others?"
        c"Pathetic"
    "Apologized Sincincrely":
        $morality = morality + 1
        p"In recent times, I have been doing a bit more reflection on my actions.."
        c"..?"
        p"I know you have no reason to take my apology as anything other than a dying man's last words.."
        p"But I'd like to apologized none the less"
        if cmn_people_oppression_knowledge_1:
            p"The nightmares of all the people crushed under my rule keep me up at night..."
            "The intruders face seems to lighten up in the subtlest most unoticable way"
            "I would have missed it if I wasn't looking directly at their face."
            p"The common people deserved a king who would protect them at every turn, but instead they got the opposite"
        elif execution_knowledge:
            p"The nightmares of all the people I've wrong executed keep me up at night..."
            "The intruders face seems to lighten up in the subtlest most unoticable way"
            "I would have missed it if I wasn't looking directly at their face."
            p"So much bloodshed unjustly for my own corrupt ways"
            p"It's own right to expect such acts to be enacted on me the same.."
        else:
            p"I apologize for..."
            "This isn't good. I'm drawing blanks on the Hindleys crimes"
            "I have to say something accurate or else I won't have a chance to convince this intruder"
            "Unfortunately it seems I took too long in their eyes.."
            c"Searching for a good answer to give me aren't you?"
            c"The fact that you can't immedately name your wrong doings is enough proof that you don't truly feel sorry for anything"
            c"You're only doing it to survive like the coward you are"
            $doubt = doubt + 1
            jump scene4
        c"It's too late to try to repent.."
        "They say with a minsulce amount of waivering."
        "It's seems the remorse I showed took them aback in some ways"

    
    "Manupulate Him":
        $morality = morality - 1
        p"Are you sure you even {i}want{/i} to do this?"
        p"Killing me with change nothing. My relative with just take the throne"
        p"And they have the capacity to down even worse than me"
        c"Maybe they do"
        c"But thats a risk I have to be willing to take"
        p"Okay if you say so.. but there {i}are{/i} other options available"
        c"...what? Like leaving you alive? Keeping things as the status quo? Not possible."
        p"You're thinking too small"
        p"If you want real change to happen you need someone willing to do the work on the throne"
        p"I'm sure you're well aware I'm willing to do a LOT to survive right now."
        p"So if you let me live I can make the changes you want myself"
        c"There'd be no way to make sure you keep your end of the bargin even if I {i}did{/i} do that.."
        p"How you can stay in the castle to keep me in check"
        p"You clearly have {i}some{/i} with my guard force for you to get here unharmed."
        c"..."
        p"I'm just saying, the offer is on the table.."


label scene4:
    "blah"
    #blah blah blah



if doubt >= 2 and morality < 1:
    c"In the name of Hate and Justice for all the people you've crushed, I'll kill you!"
    c"Right here and now!"
    c"Bon Voyage, I hope you hate hell as much as we hate you!"
    "Bon Voyage...."
    "No... that's not the right word..."
    "It should be..."

    jump ending_consume

if doubt >= 2 and morality >= 1:
    c"In the name of Hate and Justice for all the people you've crushed, I'll kill you!"
    "The Intruder dashes at me and I'm unable to move out of the way"
    "Their dagger digs into my skin as they plunge it over"
    "and over.."
    "and over again..."
    "Ending: Fall to Oblivon"
    return

if doubt < 2 and morality < 1:

    "Ending: Intrinsic Nature Prevails"
    return

if doubt < 2 and morality >= 1:

    "Ending: Tightrope Survival"
    return


label ending_consume:
    menu:
        "'Goodbye'":
            "Ending: To Consume for Survival"
            return




    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    
    # This ends the game.

    return
