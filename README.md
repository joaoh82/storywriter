# Storywriter Microservice:

Services tells a story based on a template and input words

## Action
1. A story action should receive a template and words to be replaced in the template

## Goals
2. Input consists of an array os words and a string template
3. The string templates references words via &1 (first word), &2 (second word) and so forth
4. The output is a string of the word references replaced with their actual words
   1. Being a RESTful microservice I thought it would be best to return a JSON object instead of a plain string
5. The words array is an optional input

## Testing
You can test your microservice with `omg run`:

```$ omg run story -a template='On a fine &2 he saw &1.' -a words='["a sparrow", "morning"]'
✔ Ran action: `story` with output: "On a fine morning he saw a sparrow."```

```$ omg run story -a template='Afterwards he ate &1 & &2.' -a words='["an apple", "two bananas"]'
✔ Ran action: `story` with output: "Afterwards he ate an apple & two bananas."```

```$ omg run story -a template='No words.'
✔ Ran action: `story` with output: "No words."```
If you have any questions please do not hesitate to get in touch with us.