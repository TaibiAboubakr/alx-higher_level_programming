#include "Python.h"
#include <stdio.h>
/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: A pointer to a Python object, assumed to be a list.
 */

void print_python_list_info(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size, i;
	Py_ssize_t allocated;

	if (!PyList_Check(p))
		return;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
