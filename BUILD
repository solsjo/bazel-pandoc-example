load("@bazel_pandoc//:pandoc.bzl", "pandoc")

pandoc(
    name = "example",
    src = "//:example/example.md",
    from_format = "markdown",
    to_format = "revealjs",
    output = "index.html",
    options = [
        "--standalone",
        '-V revealjs-url="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0"',
    ],
)
