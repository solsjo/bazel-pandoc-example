workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "solsjo-bazel-pandoc-v0.3-7-gd15590a",
    urls = ["https://github.com/solsjo/bazel-pandoc/zipball/master"],
    sha256 = "82e1058acfc265d22e1562c471c38c62521a1d9033d866d46fc7c0f34d22560e"
)

load("@bazel_pandoc//:repositories.bzl", "pandoc_repositories")

pandoc_repositories()
