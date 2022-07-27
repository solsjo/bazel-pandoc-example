load("@bazel_pandoc//:pandoc.bzl", "pandoc")

pandoc(
    name = "example",
    src = "//:example/example.md",
    from_format = "markdown",
    to_format = "revealjs",
    output = "index.html",
    options = [
        "--standalone",
        "--filter $(location @pandoc_plantuml_filter//:pandoc_plantuml_filter)",
        #'-V revealjs-url="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0"',
    ],
    data = [
        "@pandoc_plantuml_filter//:pandoc_plantuml_filter",
    ],
)
