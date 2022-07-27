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

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

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

#maven_jar(
#    name = "plantuml",
#    artifact = "net.sourceforge.plantuml:plantuml:1.2021.3",
#    sha1 = "8b5be104e564b2b3cec307e2b0dba199f77fc422",
#)

http_archive(
    name = "pandoc_plantuml_filter",
    strip_prefix = "solsjo-bazel-pandoc-eb7e560",
    url = "https://github.com/timofurrer/pandoc-plantuml-filter/zipball/master",
    sha256 = "fe41858fe01ba6a2144e730d69510d684265cf0a49482c03aa2485ff69e43135",
    type = "zip",
)
