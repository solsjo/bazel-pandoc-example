load("@bazel_pandoc//:pandoc.bzl", "pandoc")

pandoc(
    name = "example",
    src = "//:example/example.md",
    from_format = "markdown",
    to_format = "revealjs",
    output = "index.html",
    options = [
        "--standalone",
        "--self-contained",
    ],
    data = [
        "example.svg",
    ],
)

genrule(
    name = "example_puml",
    srcs = ["//:example/example.puml"],
    outs = ["example.svg"],
    cmd = "$(location @pandoc_plantuml_filter//:plantuml) -nometadata -tsvg -p < $(location //:example/example.puml) > $(OUTS)",
    tools = ["@pandoc_plantuml_filter//:plantuml"],
)
