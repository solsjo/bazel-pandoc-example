workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "pandoc_plantuml_filter",
    strip_prefix = "timofurrer-pandoc-plantuml-filter-61ec9f8",
    build_file = "//:third_party/pandoc/pandoc_plantuml_filter.BUILD",
    workspace_file = "//:third_party/pandoc/pandoc_filter.WORKSPACE",
    url = "https://github.com/timofurrer/pandoc-plantuml-filter/zipball/master",
    sha256 = "a747321e6511fc2c846f95d5e78a873ed8b93d435600f4e5790e48cc5d6a58d4",
    type = "zip",
)

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "solsjo-bazel-pandoc-50b6f81",
    url = "https://github.com/solsjo/bazel-pandoc/zipball/master",
    sha256 = "86274b1bef9555df6201a1981734e99b7ffe78d1c432cb6b33d72f1473fe3cc2",
    type = "zip",
)

load("@bazel_pandoc//:repositories.bzl", "pandoc_repositories")

pandoc_repositories()

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

http_archive(
    name = "rules_jvm_external",
    sha256 = "62133c125bf4109dfd9d2af64830208356ce4ef8b165a6ef15bbff7460b35c3a",
    strip_prefix = "rules_jvm_external-3.0",
    url = "https://github.com/bazelbuild/rules_jvm_external/archive/3.0.zip",
)

load("@rules_jvm_external//:defs.bzl", "maven_install")

maven_install(
    artifacts = [
        "net.sourceforge.plantuml:plantuml:1.2021.3",
    ],
    fetch_sources = True,
    repositories = [
        "https://maven.google.com",
        "https://repo1.maven.org/maven2",
        "https://jcenter.bintray.com/",
    ],
    strict_visibility = True,
)
