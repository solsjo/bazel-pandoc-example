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
    strip_prefix = "solsjo-bazel-pandoc-a6c0e55",
    url = "https://github.com/solsjo/bazel-pandoc/zipball/master",
    sha256 = "cc76d1b6e7981d9a22d6e96d10306f75ce25b9497d0f93e2c7ce93b7c421f173",
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

http_archive(
    name = "io_tweag_rules_nixpkgs",
    sha256 = "b01f170580f646ee3cde1ea4c117d00e561afaf3c59eda604cf09194a824ff10",
    strip_prefix = "rules_nixpkgs-0.9.0",
    urls = ["https://github.com/tweag/rules_nixpkgs/archive/v0.9.0.tar.gz"],
)
load("@io_tweag_rules_nixpkgs//nixpkgs:repositories.bzl", "rules_nixpkgs_dependencies")
rules_nixpkgs_dependencies()
load("@io_tweag_rules_nixpkgs//nixpkgs:nixpkgs.bzl", "nixpkgs_git_repository", "nixpkgs_package")

load(
    "@io_tweag_rules_nixpkgs//nixpkgs:nixpkgs.bzl",
    "nixpkgs_package",
    "nixpkgs_git_repository",
)

nixpkgs_git_repository(
    name = "nixpkgs",
    revision = "22.05",
    sha256 = "0f8c25433a6611fa5664797cd049c80faefec91575718794c701f3b033f2db01",
)

nixpkgs_package(
    name = "graphviz",
    repository = "@nixpkgs",
    build_file_content = """
package(default_visibility = [ "//visibility:public" ])
exports_files([
  "nix/bin/dot",
  "nix/bin/neato",
])
filegroup(
  name = "bin",
  srcs = glob(["nix/bin/*"]),
)
filegroup(
  name = "lib",
  srcs = glob(["nix/lib/**/*.so"]),
)
""")
