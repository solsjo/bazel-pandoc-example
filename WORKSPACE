workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "solsjo-bazel-pandoc-eb7e560",
    url = "https://github.com/solsjo/bazel-pandoc/zipball/master",
    sha256 = "fe41858fe01ba6a2144e730d69510d684265cf0a49482c03aa2485ff69e43135",
    type = "zip",
)

load("@bazel_pandoc//:repositories.bzl", "pandoc_repositories")

pandoc_repositories()

http_archive(
    name = "pandoc_plantuml_filter",
    strip_prefix = "solsjo-bazel-pandoc-eb7e560",
    build_file = "//:third_party/pandoc/pandoc_plantuml_filter.BUILD",
    workspace_file = "//:third_party/pandoc/pandoc_filter.WORKSPACE",
    url = "https://github.com/timofurrer/pandoc-plantuml-filter/zipball/master",
    sha256 = "fe41858fe01ba6a2144e730d69510d684265cf0a49482c03aa2485ff69e43135",
    type = "zip",
)

http_archive(
    name = "rules_python",
    sha256 = "a30abdfc7126d497a7698c29c46ea9901c6392d6ed315171a6df5ce433aa4502",
    strip_prefix = "rules_python-0.6.0",
    url = "https://github.com/bazelbuild/rules_python/archive/0.6.0.tar.gz",
)

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "py_deps",
    requirements = "//:requirements.txt",
)
