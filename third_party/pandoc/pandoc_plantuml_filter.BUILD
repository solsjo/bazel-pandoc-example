load("@rules_python//python:defs.bzl", "py_binary", "py_library")


py_binary(
    name = "pandoc_plantuml_filter",
    srcs = ["pandoc_plantuml_filter.py"],
    main = "pandoc_plantuml_filter.py",
    env = {
        "PLANTUML_BIN":"$(location @bazel_pandoc_example//third_party/plantuml:plantuml)",
    },
    #deps = [":testlib"],
)
