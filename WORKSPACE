workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "bazel-pandoc-master",
    urls = ["https://github.com/solsjo/bazel-pandoc/archive/refs/heads/master.zip"],
    sha256 = "15ea7c76226c9df57cf9e3e32d856513b26365831c9979ef9c28dd5a1ef2c196"
)

load("@bazel_pandoc//:repositories.bzl", "pandoc_repositories")

pandoc_repositories()
