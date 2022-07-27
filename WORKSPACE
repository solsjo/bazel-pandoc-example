workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "solsjo-bazel-pandoc-d15590a",
    url = "https://github.com/solsjo/bazel-pandoc/zipball/master",
    sha256 = "fe41858fe01ba6a2144e730d69510d684265cf0a49482c03aa2485ff69e43135",
    type = "zip",
)

load("@bazel_pandoc//:repositories.bzl", "pandoc_repositories")

pandoc_repositories()
