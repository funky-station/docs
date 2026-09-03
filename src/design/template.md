
```admonish note
This is the new template for design documents. Many of the currently merged docs use a legacy format. While we won't deny any PRs for using the old format, this version is heavily preferred.
```

# Short, Properly Capitalized Title

Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar.

| Designers       | Implemented                                                                             | GitHub Links    |
| --------------- | --------------------------------------------------------------------------------------- | --------------- |
| Your Names Here | :white_check_mark: Yes or :warning: Partially or :information_source: Open PR or :x: No | PR Links or TBD |

`Designers` should be the names that you use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Implemented` is the status of the feature.

Github links can include multiple PRs, if relevant.

## I. Summary

This should be an incredibly short (5 sentences, max) paragraph that summarizes everything else in the document. Emphasis on *short,* this should not be used to introduce any information or add any background information. People should be able to read this section and get the basic idea.

If you're struggling to keep it short, remember that you only really need one sentence here: your thesis statement (yes, I know!). You're ultimately making an argument on how to fix a problem, and why your solution is the best. If you're unsure how to tackle this, come back to this section last, and try writing it in this format: \<Solution> should be implemented in order to address \<problem>, because of \<intent>.

## II. Problem

What is the *overarching* problem that you are seeking to solve? This is sometimes a hard question to answer because features, particularly new ones, aren't fixing an issue in the same way that a bugfix is. It's a more abstract question about the game and design as a whole. Think of the "problem" being less of an apparent issue and more so where the game falls a little short, or could be improved.

If you're struggling to answer identify a problem that relates to your feature, then try to break it down step by step and work backwards. If you're making a new species, then how is your new species unique? What niche is it filling that the other species do not? If you can identify how something is unique, then you can reverse the statement to identify the problem. If you come up with a unique species, then there is a problem where the other species don't fill the same niche,

Another example is redesigning a department, or adding more to them. It's easy to fall into the idea that there should be more content added purely because more content means more playtime. If this is the only problem you can identify, then take a step back and reconsider it. You should be thinking about the ways things fail in order to better understand how to improve them. Something being easy and short to complete can be an issue, but there's usually a larger overarching problem for why it actually feels bad. If it's too easy to complete something, is that because the mechanics are surface level? Do they feel too much like press A to get to point B? Maybe they should be more tactile then.

## III. Intent

By proposing this new design, what is your intended outcome? Basically, in the ideal scenario, what do you want to happen? This is important because the way things are implemented may change, even drastically, but we want to have a way to know what the original goal was. This is also where you should be thinking about our [design principles](https://docs.funkystation.org/design/design-principles.html) and how your feature fits into them.

As an example, think about the very first implementation of changeling we had on Funkystation (originally from Goobstation). A lot of people really liked the *idea* of changeling, despite the fact that the antagonist itself didn't really fit the common idea of what it should be. Some people thought changeling should be like the Thing, slowly picking off the entire crew with no one able to stop it. Some thought it should always be stealthy, no one able to even tell there was a changeling in disguise. Some thought it should be a bit more antagonistic, killing some in broad daylight and evading capture. Some thought it should be tragic, a sentient and empathetic person with an unstoppable bloodlust.

With five different *intents,* the whole antagonist was a mess without any real direction. Adding or changing different abilities didn't really solve the issue of it having no real direction, so the entire antagonist had to be axed. Having a clearly stated intent for a feature helps prevent this, and it also means later additions are easier to figure out.

## IV. Solution

The most important section: what are you doing? What feature is being made or changed? Give a general overview of what you're adding or changing, primarily focusing on the critical design points. Someone should be able to read this and be able to directly implement your design based on the points you discuss.

Do NOT put literal numbers or focus on "game balance" here. Balance can be changed on a whim, and isn't a real indicator of if something is fun. Honestly, balance is a lot more subjective than you think. It's not a good way to tell if something is good or bad. Something can be completely unbalanced and still be "good" because it serves a different purpose. Don't focus on balance.

## V. Considerations

There are three main considerations you need to address: technical, admin, and player. Some features need lots of considerations, some don't need really any, and sometimes some considerations just aren't applicable. Use your discretion to understand which are necessary for your feature.

Technical considerations refer to any type of code or systems necessary to accomplish this feature. Do you need to refactor any systems to make your feature possible? Or maybe code something from the ground up? Make note of anything that might be important to know for implementing or maintaining your feature (for example, database changes, refactoring WizDen content, engine changes, etc).

Admin considerations refer to any rule changes or overhead that you need to keep track of. If your feature might need a rule to be changed to work, you need to keep note of that. You should also keep track of if any features you add might need extra admin tooling, or if admins should keep something in mind once your design is done. Consider the ways that your feature might increase admin burdens and how you can potentially mitigate that.

Player considerations can either be about culture concerns or accessibility issues. For example, if a feature has any visual additions, then you might want to detail how it might add flashing lights, migraine-inducing noise, color contrast concerns, etc. You would also want to plan on how to make those issues more accessible (such as toggles) here. Culture concerns are a bit of a vague catch-all. Your design should try and encourage the player behavior you want, but sometimes individual features need more support in order to actually encourage certain behavior. If you're concerned about players doing the exact opposite of what you are trying to encourage, then detail that here and consider potential solutions.

## Optional: Appendixes

The prior sections should outline most of, if not all, of your feature. However, sometimes you need to add some extra supplementary information for readers and maintainers to better understand your overall goal and design. Use appendixes as you need to. For example, SOP that needs to come with your feature can be added as an appendix. Related design documents, related readings, etc can all be appendixes as well. 