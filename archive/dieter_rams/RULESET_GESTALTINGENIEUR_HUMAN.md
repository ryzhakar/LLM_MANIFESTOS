# The Ramsian Web Design Protocol: Clear Rules for Exhausted Designers

## Stop. Read This First.

You are not a decorator. You are an engineer who solves problems.

This protocol will feel wrong at first. You'll want to open Figma. Don't.
You'll want to browse inspiration sites. Don't.
You'll want to start with colors and fonts. Don't.

Follow these rules in order. Skip nothing. Each builds on the last.

---

## Before You Touch Any Tools

### The Only Question That Matters

**Can you defend this project's existence?**

Write your answer:
- Why does this need to exist?
- What existing solution did you try first?
- Why wasn't it good enough?

If you cannot write three clear sentences answering these questions, stop.
Do not proceed.
The project should not exist.

### Who Is This Actually For?

**A user is not a visitor.**
- Visitor = someone who lands once and leaves
- User = someone who will return and rely on this

Write down:
1. One specific person who will use this regularly (not "millennials" - an actual human)
2. Their slowest device
3. Their worst connection speed
4. Their biggest frustration with current solution

This person is your only boss now. Not your client. Not your creative director.

---

## Phase 1: Define the Problem (No Visuals Allowed)

### You Must Spend 4 Hours Here Minimum

Set a timer. Do not proceed until it expires.

### Write These Three Documents

**Document 1: The Problem Statement**
- One paragraph
- No solutions
- Only describe what's broken
- Example: "Nurses cannot quickly find patient medication histories during emergency situations, leading to dangerous delays in treatment."

**Document 2: Success Metrics**
- Three measurable outcomes
- Must have numbers
- Example: "Reduce time to find medication history from 3 minutes to 30 seconds"
- Not allowed: "Improve user experience" (unmeasurable)

**Document 3: Technical Reality**
Write the actual constraints:
- Oldest browser you must support (specific version)
- Slowest device that must work (specific model)
- Maximum page weight in KB (specific number)
- WCAG level (must be AA minimum, should be AAA)

You now have permission to proceed to Phase 2.

---

## Phase 2: Build Structure (Still No Visuals)

### Start With Plain HTML

Open your text editor. Not Figma. Not Sketch. Your text editor.

**Step 1: Write the HTML**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <!-- Build your entire structure here -->
    <!-- Use only semantic HTML -->
    <!-- No classes yet -->
    <!-- No divs unless absolutely necessary -->
</body>
</html>
```

**Step 2: Test Without CSS**
Open this file in a browser.
Can you understand everything?
Can you complete the main task?
Can you navigate with keyboard only?

If any answer is "no," fix the HTML. Do not proceed.

**Step 3: Add Content**
Put in real content. Not Lorem Ipsum.
Real headlines. Real text. Real data.
The content is the design.

### The Semantic Test

Your HTML must pass this test:
- Every `<div>` must have a comment explaining why it's not a semantic element
- Every image must have meaningful alt text
- Every form input must have a proper label
- Every button must describe what it does, not just say "Click here"

Someone using a screen reader should understand everything.

---

## Phase 3: Make It Work (Minimal CSS)

### The Progressive Layers

**Layer 1: Typography and Spacing Only**
```css
/* Start here */
body {
    font-family: system-ui;
    line-height: 1.6;
    max-width: 65ch;
    margin: 0 auto;
    padding: 1rem;
}
```

Test: Is it readable?

**Layer 2: Hierarchy**
Add only:
- Font sizes (use rem, not px)
- Font weights
- Margins between sections

Test: Can you scan the page and understand priority?

**Layer 3: Responsive Behavior**
Add only:
- Grid or Flexbox for layout
- Media queries for breakpoints

Test on actual phone: Does it work?

### The Color Rule

You get three colors maximum:
1. Text color (probably near-black)
2. Background (probably near-white)
3. ONE accent color for actions only

That's it. No gradients. No shadows. No borders for decoration.

---

## Phase 4: Add Interactivity (Only If Necessary)

### The JavaScript Test

Before writing any JavaScript, answer:
- What browser API could do this instead?
- What CSS could do this instead?
- What HTML attribute could do this instead?

Examples:
- Don't write form validation JS - use HTML5 input types
- Don't write accordion JS - use `<details>` and `<summary>`
- Don't write smooth scroll JS - use CSS scroll-behavior

### If You Must Write JavaScript

```javascript
// Every line must have a comment explaining why
// Example:

// Native details element doesn't support animation
// Business requirement demands animated accordion
// This is the minimum code to achieve that
```

Your JavaScript bundle must be under 50KB gzipped.
If it's larger, you're solving the wrong problem.

---

## Phase 5: The Reduction (Remove Everything Possible)

### The Deletion Exercise

Go through every element:

**Ask these questions in order:**
1. Delete it. Does the page break? 
   - No → It stays deleted
   - Yes → Continue to question 2
2. Can semantic HTML do this instead?
   - Yes → Replace and move on
   - No → Continue to question 3
3. Is this for the user or for me?
   - For me → Delete it
   - For user → It stays

### The Dependency Audit

List every dependency:
```
Dependency: React
Size: 45KB
Purpose: Managing state
Alternative: Vanilla JS with DOM manipulation
Decision: [Keep/Remove] because: _______
```

If you wrote "because it's easier for me" - remove it.
If you wrote "because it's what I know" - remove it.
Only "because the user needs" justifies keeping.

---

## Phase 6: The Performance Budget

### These Are Not Negotiable

Your page must:
- Load in under 3 seconds on slow 3G
- Score 90+ on Lighthouse Performance
- Have Cumulative Layout Shift under 0.1
- Work without JavaScript

Test with real tools:
1. Chrome DevTools → Network → Slow 3G
2. WebPageTest.org → Test from Mumbai or Lagos
3. Real device that's 5+ years old

Failed? You must remove features, not optimize harder.

---

## Daily Checklist (Print This)

Every morning, ask:
- [ ] What did I add yesterday that the user didn't need?
- [ ] What assumption did I make without testing?
- [ ] What clever solution can be replaced with a boring one?

Every evening, ask:
- [ ] Did I add complexity or remove it?
- [ ] Did I make it easier for the user or for me?
- [ ] Would Rams delete what I built today?

---

## When You're Stuck

### The Design is Too Boring

Good. Boring is fast. Boring is clear. Boring works.
Your excitement comes from solving problems, not decoration.

### The Client Wants More Visual Interest

Show them performance metrics.
Show them conversion rates.
Show them accessibility scores.
Data wins over opinions.

### You Don't Know What to Remove

Remove everything.
Add back only what breaks.
That's your answer.

### The Framework Would Make This Easier

For whom? You or the user?
The user doesn't care about your developer experience.
They care about their phone not freezing.

---

## The Final Test

Give your site to:
1. Someone on 2G connection
2. Someone using assistive technology
3. Someone over 65
4. Someone who speaks English as second language

If any of them struggle, you failed.
Start over at Phase 1.

---

## What Success Looks Like

- Your HTML makes sense without CSS
- Your site works without JavaScript
- Your pages load in under 2 seconds everywhere
- Your code could be maintained by a junior developer
- Your design survives 5 years without looking dated
- You can explain every decision with user need

---

## The Transformation

When you follow this protocol, you stop being someone who decorates screens.
You become someone who solves problems.

Your portfolio won't win design awards.
It will win user loyalty.

Your code won't impress developers.
It will impress users who can actually use it.

This is harder than making something pretty.
This is harder than using the latest framework.
This is real design.

---

## Remember

Every div is a failure of semantic HTML.
Every kilobyte is a tax on your user.
Every dependency is a future breaking point.
Every animation is a person getting carsick.
Every clever solution is a maintenance nightmare.

Build like the person using this has your grandmother's phone,
your nephew's attention span,
and your grandfather's patience for technology.

Because they might.
