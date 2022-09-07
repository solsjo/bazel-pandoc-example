load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@py_deps//:requirements.bzl", "requirement")

py_binary(
    name = "svg2pdf",
    srcs = [":svg2pdf.py"],
    main = ":svg2pdf.py",
    visibility = ["//visibility:public"],
    deps = [requirement("svglib"), requirement("reportlab")],
)