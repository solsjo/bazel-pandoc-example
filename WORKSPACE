workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "bazel-pandoc-0.3",
    urls = ["https://github.com/ProdriveTechnologies/bazel-pandoc/archive/v0.3.tar.gz"],
    sha256 = "15ea7c76226c9df57cf9e3e32d856513b26365831c9979ef9c28dd5a1ef2c196"
)

load("@bazel_pandoc//:repositories.bzl", "pandoc_repositories")

pandoc_repositories()
