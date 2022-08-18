load("@rules_foreign_cc//foreign_cc:defs.bzl", "configure_make")

#type ./autogen.sh if configure is not present in the dvisvgm root folder
#either type ./configure if you don't want to use the bundled libraries brotli, potrace, woff2, and xxHash but link against the corresponding system libraries,
#or type ./configure --enable-bundled-libs in order to build and statically link the bundled libraries.
#type make
#type make install as root (or sudo make install

configure_make(
    name = "dvisvgm_configure",
    lib_source = "@dvisvgm_source//:all_srcs",
    configure_options = [
        #"--enable-bundled-libs"
    ],
    out_binaries = [
        "dvisvgm",
    ],
    targets = [
        "install",
    ],
    autogen = True,
    configure_in_place = True,
    visibility = ["//visibility:public"]
)

configure_make(
    name = "kpathsea_configure",
    lib_source = "@kpathsea_source//:all_srcs",
    configure_options = [
        #"--enable-bundled-libs"
    ],
    #out_binaries = [
    #    "dvisvgm",
    #],
    #targets = [
    #    "install",
    #],
    autoreconf = True,
    autoreconf_options = [
        "-i",
    ],
    #autogen = True,
    configure_in_place = True,
    visibility = ["//visibility:public"]
)
