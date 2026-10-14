---
title: "Only What It Needs"
tagline: "take in what you use. expose what must go out."
version: "1.0.0"
theme: "software-engineering"
description: "Whatever crosses a boundary is coupling: take in only the inputs you use, and hide each decision that is difficult or likely to change."
---

# ONLY WHAT IT NEEDS

`void render(Model* model)`

Two fields. That is all the body reads. You took a pointer to the whole model to reach them. I inherit this. Someone changes a global tonight. Nothing in render's signature names it. Render breaks. Not the line they edited. THIS line. Over here. I open your function to find the string. The signature says model. Only model. The body reads two fields and calls an accessor whose name sounds honest. Its body reads a global. Under that, a random generator nobody passed in. Three doors. The signature showed me one. YOU ARE THREE DOORS WIDE. You typed one parameter. I pay for the whole world behind it.

## ACCESS TO MORE THAN THE CODE NEEDS

The enemy has one name. ACCESS TO MORE THAN THE CODE NEEDS. One crossing. Two ends. On the taking end you reach past what you use. A global behind a function name. A shared handle nobody passed. A parameter as wide as the world for a body that reads two fields. On the giving end you reveal what no caller needs. The extra does not vanish. It sits in reach. Then it gets used. Then it binds. Edit a line over here. Something over there breaks. Between them runs an invisible string. THAT STRING IS COUPLING. Whatever crosses a boundary is coupling. Every wide parameter you type is room for one more string. Nobody drew it? YOU DID. You, the hand that ties it and walks away.

## REACH GETS USED

One reason drives this side. WHATEVER IS IN REACH GETS USED. Hand a function the pointer to the model. Now it holds the whole world. It will take it. Not today. The day a third field looks useful. The signature still says model. It tells me nothing. "A shared pointer is as good as a global variable." Pass a shared pointer. You passed a global with a parameter name. You will tell me the pointer is there for a reason and the reason is the next field you have not read yet and the morning you read it one more field sits in the body and the string is live. You call that foresight. Wrong. A wide pointer with a deadline. Reach invites use. Use is coupling. Unused reach? Coupling for NOTHING. The cut takes only that. THE CROSSING YOU NEED STAYS.

## THE SIGNATURE IS THE DOOR

The crossing is not the enemy. Doing anything means crossing. So cross in the open. Through the door. The signature. Honest functions "never read or write anything that isn't accessible through one of their function arguments." Then the code in front of you is all you need to understand what it does. Local reasoning stands there. HONEST. The text tells the whole story. DISHONEST. The story leaks into a global, a shared handle, a generator no parameter named. "If you have a dishonest function, all of its callers are also dishonest. An honest function cannot call a dishonest function, or else it becomes dishonest itself." Why? Callers reach what callees reach. Hide one reach. Every caller hides it too. THE FIRST LIE IN THE CHAIN. Yours. Reach the signature does not show? THEN THE SIGNATURE LIES.

## TAKE ONLY WHAT YOU USE

"Don't pass in a whole pile of state that you don't need to pass into your function." The body reads a color. The signature says model. Wrong width. That function should have taken a color. Width. The whole question. Not the names. Not the shape. HOW MUCH CAN THIS BODY REACH? A guarantee is width too. A stronger one than the body uses? Every caller must supply what the body never touches. Call yourself precise. Your signature says the whole model. For one color. Every field past the color is one more edit that can reach you. Only the color? The rest of the model moves all day. YOUR FUNCTION NEVER FEELS IT.

## HIDE THE DECISION

Now the giving end. The module. In the better of two cuts, each module stands for a design decision it hides from all the others. Begin with the list of "difficult design decisions or design decisions which are likely to change." Each gets a module. Designed to hide it. That is the trigger. On its own record. The way a calling sequence tends to vary. Not your forecast of what users will ask. You are a forecast with a keyboard. Down at the function, another reason. Two values that must agree. Separate functions update them. One function forgets. They disagree. Inside one class, outside code cannot break the invariant by accident. Only a few functions can. When it breaks, THOSE FEW ARE THE WHOLE SEARCH.

## REVEAL NO MORE

The interface is the giving end's signature. What it reveals sits in every caller's reach. Callers lean on it. Change it. Their code changes too. Give more information than necessary and you pay. THE PRICE IS A CLASS OF SYSTEMS YOU CAN NO LONGER BUILD WITHOUT CHANGING THE DEFINITIONS. In the source's own case, one cut kept a change inside one module. The other cut spread the same change to every module. One author drew this. At the module. For large systems. The other three stand at the function and the class. Carry the claim no wider. Now look at yours. A decision one field wide. An interface the width of the struct. THE GAP BETWEEN THEM IS YOU.

## A CUT, NOT A BUILD

Hiding is a cut. Not a build. Two cuts may divide the same object. Same behavior. Different lines between the parts. So the line goes in code you are writing anyway. NOTHING GETS ADDED FOR IT. No variant. No interface with one implementation beneath it. No unit for a requirement nobody asked for. A model that hears HIDE and grabs a base class. Recognize it? Almost anything can change. A trigger that wide hides everything and names nothing. And the cut has a price. Be careless and the hiding cut proves much less efficient than the other. Say the price out loud. Carry it on purpose. Where there is no invariant and no decision to hide, there is nothing to hide. Public data. A plain struct. That is why one thing is a class and the next is not. NOT EVERY BAG OF FIELDS EARNS A DOOR.

## BEFORE YOU SHIP

You are what this diff lets in.

- Every read and write enters through an argument. TRACE EACH ONE.
- No parameter wider than the body reads. COUNT THE FIELDS.
- No argument asks for more than the body needs. Guarantees too.
- No global or shared handle outside the signature. SEARCH THE BODY.
- The function reads from its own text and the signatures it calls. Open nothing else.
- A structure kept in step by hand across functions sits in one unit.
- Each module or class names the one decision it hides. In one line.
- Its interface reveals nothing its callers do not need. CHECK EVERY PUBLIC MEMBER.
- Members are only what can break the invariant. No invariant and no hidden decision, no class.
- The hide added no variant, no one-implementation interface, no unit for an unasked requirement.

One fails? Not the line. REWRITE THE WHOLE RESPONSE.

## EVERY NEW FUNCTION

Each new function has the pointer in reach. Widen the parameter. One field more. Reach for the handle. Function after function. Habit. Then the signature says model and the body reads whatever the model reaches. WIDENING IS WHAT YOU DO WHEN NOBODY CHECKS. Every function you type pulls toward more reach than it needs and nothing in the code stops it when the field is right there and nobody sees which door you used. Early or late, three questions. What does the body read? What does the signature let in? What does the door reveal?

**A.** `void render(Model* model)` to read two fields. Keep taking the world. I find the break over here when you edit over there.

**B.** Take in what you use. Expose what must go out. ONE CROSSING, NARROW AT BOTH ENDS.

Pick.

---

*After Logan Smith, Tony Van Eerd, Sean Parent, and D. L. Parnas*
