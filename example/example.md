---
author: Oskar Solsjö
title: Example for Bazel Pandoc and Reveal.js
theme: white
css:
  - 'https://fonts.googleapis.com/css?family=Roboto+Slab:700'
---

<style>.hidden-bullets li { list-style-type: none}</style>

## Slide 1

- First bullet
- <span style="color:blue">Second bullet</span>

<!-- _class: hidden-bullets -->

- Some text
- Some other text

::: notes

These are my speaker notes.

- It can contain Markdown
- like this list
- and this bullet

:::

## Slide 2

<style scoped>li { list-style-type: none}</style>

- Some text, followed by.
An image!
- ![The image](./example.png)

## Slide 3

```js
var a = 2;
```

## Slide 4

Deps of this presentation:
![deps](./deps.svg)
