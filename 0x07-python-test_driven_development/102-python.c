#include <Python.h>

void print_python_string(PyObject *p) {
    // Check if p is a valid string object
    if (PyUnicode_Check(p)) {
        // Convert the Python string to a C string (UTF-8 encoding)
        const char *str = PyUnicode_AsUTF8(p);

        if (str != NULL) {
            // Print the Python string
            printf("'%s'\n", str);
        } else {
            // Failed to decode the string
            PyErr_Print();
        }
    } else {
        // p is not a valid string object
        PyErr_SetString(PyExc_TypeError, "Expected a string object");
        PyErr_Print();
    }
}

int main() {
    // Initialize the Python interpreter
    Py_Initialize();

    // Create a sample Python string
    PyObject *sample_string = PyUnicode_DecodeUTF8("Hello, Python!", strlen("Hello, Python!"), "strict");

    // Call the print_python_string function
    print_python_string(sample_string);

    // Clean up and finalize the Python interpreter
    Py_Finalize();

    return 0;
}
