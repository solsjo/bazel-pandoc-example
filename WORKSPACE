workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "solsjo-bazel-pandoc-d15590a",
    url = "https://github.com/solsjo/bazel-pandoc/zipball/master",
    sha256 = "103df36dc21081b7205d763ef7705e340eb0ea7e18694239b328a549892cc007",
    type = "zip",
)

load("@bazel_pandoc//:repositories.bzl", "pandoc_repositories")

pandoc_repositories()
