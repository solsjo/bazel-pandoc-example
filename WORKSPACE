workspace(name = "pandoc_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

#http_archive(
#    name = "pandoc_plantuml_filter",
#    strip_prefix = "solsjo-pandoc-plantuml-filter-9f364fd",
#    build_file = "//:third_party/pandoc/pandoc_plantuml_filter.BUILD",
#    workspace_file = "//:third_party/pandoc/pandoc_filter.WORKSPACE",
#    url = "https://github.com/solsjo/pandoc-plantuml-filter/zipball/master",
#    sha256 = "7fed92c1b7050a8b73ace4ecbccc8dd37e17bddad6aacf01dfd228bde2052942",
#    type = "zip",
#)

http_archive(
    name = "bazel_pandoc",
    strip_prefix = "solsjo-bazel-pandoc-3543350",
    url = "https://github.com/solsjo/bazel-pandoc/zipball/master",
    sha256 = "ea17ca177dc20a8c92cd3b7bb5d4f79ad5785bcc04ede1a8aef88a1175745815",
    type = "zip",
)

load("@bazel_pandoc//:repositories.bzl", "pandoc_repositories")

pandoc_repositories()


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
