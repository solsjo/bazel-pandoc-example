---
author: Oskar Solsjö
title: Example for Bazel Pandoc and Reveal.js
theme: white
css:
  - 'https://fonts.googleapis.com/css?family=Roboto+Slab:700'
---

## Slide 1

- First bullet
- <span style="color:blue">Second bullet</span>

Some text<br/>
Some other text<br/>

::: notes


These are my speaker notes.

- It can contain Markdown
- like this list

:::

## Slide 2

Some text, followed by.
An image!
![The image](./example.svg)

## Slide 3

```js
var a = 2;
```

## Slide 4

Deps of this presentation:
![deps](./deps.svg)
