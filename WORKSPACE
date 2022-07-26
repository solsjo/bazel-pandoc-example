workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "bazel-pandoc-0.3",
    url = "https://github.com/ProdriveTechnologies/bazel-pandoc/archive/v0.3.tar.gz",
)

load("@bazel_pandoc//:repositories.bzl", "pandoc_repositories")

pandoc_repositories()
