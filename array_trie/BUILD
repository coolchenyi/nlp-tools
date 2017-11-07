

py_binary(
    name = "abstract_double_array_trie",
    srcs = ["abstract_double_array_trie.py"],
    srcs_version = "PY2AND3",
    deps = ["//data_structure:treeset"]
)

py_binary(
    name = "double_array_trie",
    srcs = ["double_array_trie.py"],
    srcs_version = "PY2AND3",
    deps = [":abstract_double_array_trie", "//data_structure:treeset"]
)

py_binary(
    name = "count_trie",
    srcs = ["count_trie.py"],
    srcs_version = "PY2AND3",
    deps = [":double_array_trie"]
)

py_binary(
    name = "test_double_array_trie",
    srcs = ["test_double_array_trie.py"],
    srcs_version = "PY2AND3",
    deps = [":abstract_double_array_trie", ":double_array_trie", ":count_trie"]
)

