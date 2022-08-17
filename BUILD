load("@bazel_pandoc//:pandoc.bzl", "pandoc")
load("@bazel_latex//:latex.bzl", "latex_document")
load("@py_deps//:requirements.bzl", "requirement")

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

pandoc(
    name = "example_pptx",
    src = "//:example/example_pptx.md",
    from_format = "markdown",
    to_format = "pptx",
    output = "example.pptx",
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
    cmd = "$(location //third_party/plantuml:plantuml) -nometadata -tsvg -p < $(location //:example/example.puml) > $(OUTS)",
    tools = ["//third_party/plantuml:plantuml"],
)

latex_document(
    name = "example_tex",
    srcs = ["@bazel_latex//packages:drawstack"],
    main = "//:example/example.tex",
)

py_binary(
    name = "pdf2image",
    srcs = [":pdf_to_image.py"],
    main = ":pdf_to_image.py",
    visibility = ["//visibility:public"],
    deps = [requirement("pdf2image")],
)
