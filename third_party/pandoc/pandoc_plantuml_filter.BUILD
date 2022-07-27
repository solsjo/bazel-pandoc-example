load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@py_deps//:requirements.bzl", "requirement")

py_binary(
    name = "pandoc_plantuml_filter",
    srcs = ["pandoc_plantuml_filter.py"],
    main = "pandoc_plantuml_filter.py",
    env = {
        "PLANTUML_BIN":"$(location @bazel_pandoc_example//third_party/plantuml:plantuml)",
    },
    data = [
        "@bazel_pandoc_example//third_party/plantuml:plantuml"
    ],
    deps = [requirement("pandocfilters")],
)
