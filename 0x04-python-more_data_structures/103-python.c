#include <Python.h>
/**
 * print_python_list - print_python_list
 * @p : A pointer to a Python object (PyObject) that is expected to be a list.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		PyErr_Print();
		return;
	}
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	PyObject *element;
	Py_ssize_t i;

	for (i = 0; i < PyList_Size(p); i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}

/**
 * print_python_bytes - print_python_bytes
 * @p : A pointer to a Python object (PyObject) that is expected to be a list.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size, max_print_size;

	if (!PyBytes_Check(p))
	{
		PyErr_Print();
		return;
	}
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first 10 bytes: ");
	size = PyBytes_Size(p);
	max_print_size = size > 10 ? 10 : size;
	for (i = 0; i < max_print_size; i++)
	{
		printf("%02hhx", PyBytes_AS_STRING(p)[i]);
		if (i < max_print_size - 1)
			printf(" ");
	}
	printf("\n");
}
/**
 * main - entry level
 * Return: 0 on success
 */
int main(void)
{
	Py_Initialize();
	PyObject *list = PyList_New(0);
	PyObject *bytes;

	PyList_Append(list, Py_BuildValue("i", 42));
	PyList_Append(list, Py_BuildValue("i", 123));
	PyList_Append(list, Py_BuildValue("i", 789));
	print_python_list(list);
	bytes = Py_BuildValue("y#", "Hello, World!", 13);
	print_python_bytes(bytes);
	Py_Finalize();
	return (0);
}
