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
    strip_prefix = "bazel-pandoc-0.4-beta",
    url = "https://github.com/solsjo/bazel-pandoc/archive/refs/tags/v0.4-beta.tar.gz",
    sha256 = "79770374a226f2cb73600806b1d24d5110127ec5bdef02f17aabfbd006d49445",
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
        "net.sourceforge.plantuml:plantuml:1.2022.7",
    ],
    fetch_sources = True,
    repositories = [
        "https://maven.google.com",
        "https://repo1.maven.org/maven2",
        "https://jcenter.bintray.com/",
    ],
    strict_visibility = True,
)

http_archive(
    name = "bazel_latex",
    sha256 = "c0adcce633edc604bb49488c3e10d5e59b570b66d43934fbfd7d0392b6c991ce",
    strip_prefix = "bazel-latex-0.1-extend-toolchain",
    #url = "https://github.com/ProdriveTechnologies/bazel-latex/archive/v1.1.1.tar.gz",
    url = "https://github.com/solsjo/bazel-latex/archive/refs/tags/v0.1-extend-toolchain.tar.gz",
)

load("@bazel_latex//:repositories.bzl", "latex_repositories")

latex_repositories()

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
    name = "rules_foreign_cc",
    sha256 = "2a4d07cd64b0719b39a7c12218a3e507672b82a97b98c6a89d38565894cf7c51",
    strip_prefix = "rules_foreign_cc-0.9.0",
    url = "https://github.com/bazelbuild/rules_foreign_cc/archive/refs/tags/0.9.0.tar.gz",
)

load("@rules_foreign_cc//foreign_cc:repositories.bzl", "rules_foreign_cc_dependencies")

# This sets up some common toolchains for building targets. For more details, please see
# https://bazelbuild.github.io/rules_foreign_cc/0.9.0/flatten.html#rules_foreign_cc_dependencies
rules_foreign_cc_dependencies()

_ALL_CONTENT = """\
filegroup(
    name = "all_srcs",
    srcs = glob(["**"]),
    visibility = ["//visibility:public"],
)
"""
