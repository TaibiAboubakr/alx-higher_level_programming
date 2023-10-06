#include <Python.h>

void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        Py_UNICODE *str = PyUnicode_AsUnicode(p);
        Py_ssize_t length = PyUnicode_GetLength(p);
        int compact = PyUnicode_IS_COMPACT_ASCII(p);

        printf("[.] string object info\n");
        printf("  type: %s\n", compact ? "compact ascii" : "compact unicode object");
        printf("  length: %ld\n", length);
        printf("  value: %ls\n", str);
    } else {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
    }
}
