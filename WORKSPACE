workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "pandoc_plantuml_filter",
    strip_prefix = "solsjo-pandoc-plantuml-filter-9524ce5",
    build_file = "//:third_party/pandoc/pandoc_plantuml_filter.BUILD",
    workspace_file = "//:third_party/pandoc/pandoc_filter.WORKSPACE",
    url = "https://github.com/solsjo/pandoc-plantuml-filter/zipball/master",
    sha256 = "038f636ee66bcab6dfb3a3b1d0a769b0de7438a8ac821c14b1596ac2626ec653",
    type = "zip",
)

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "solsjo-bazel-pandoc-8f13aac",
    url = "https://github.com/solsjo/bazel-pandoc/zipball/master",
    sha256 = "e2b234021efda6888c255d6e70902491729c542281dc8e6e7d3b00b17d5a0884",
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
