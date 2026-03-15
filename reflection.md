# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first time I ran it it was telling me to go higher or lower based on what I entered but I noticed that one of the things it did wrong was tell me to go lower at a number which wouldn't lead to me to the number it actually wanted me to guess. It told me to go when I guessed 10, when the actual number it wanted me to guess was 34. So the instructions were off. Something else, was that when I tried clicking the button for starting a new game, it didn't work. I expected it to start a new game and let me start guessing, but it didn't do that, it just stayed on the page saying "game over. start a new game." Another bug is that it tells me to guess out of the range. Also it says the user has 8 attempts to guess, but it only provides 7 attempts after which it says game over. Its expected that it gives 8 tries to guess.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Github Copilot as my only AI tool. It was correct about the reset option not working in the game. I verified it by trying to create a new game and seeing that it didn't reset the game. It was incorrect about not requiring the parse_guess method. I verified the issue with what it suggested by passing in a number as a string and seeing that it didn't work.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

After running the pytests it generated and verifiying the changes took effect on the app, I confirmed the bugs were fixed. I ran a pytest that checked the high/low bug and if it provided the proper hint to go higher/lower. Yes, Copilot helped me understand the reset game test, when I told it to explicitly explain it. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
