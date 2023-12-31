#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about a Python list.
 * @p: Pointer to a PyObject representing the Python list.
 *
 * This function prints information about the given Python list, including its
 * size, allocated memory, and various data types of its elements.
 *
 * Note: This function is designed to work with Python 3.4 and was compiled on
 *		 Ubuntu 14.04 LTS.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
