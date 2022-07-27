load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@py_deps//:requirements.bzl", "requirement")
load("@rules_java//java:defs.bzl", "java_binary")

java_binary(
    name = "plantuml",
    main_class = "net.sourceforge.plantuml.Run",
    visibility = ["//visibility:public"],
    runtime_deps = [
        "@maven//:net_sourceforge_plantuml_plantuml",
    ],
)


py_binary(
    name = "pandoc_plantuml_filter",
    srcs = ["pandoc_plantuml_filter.py"],
    main = "pandoc_plantuml_filter.py",
    env = {
        "PLANTUML_BIN":"$(location :plantuml)",
    },
    data = [
        ":plantuml"
    ],
    deps = [requirement("pandocfilters")],
)
