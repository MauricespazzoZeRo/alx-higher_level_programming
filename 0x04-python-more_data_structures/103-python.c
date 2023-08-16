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



#include "Python.h"
#include <stdio.h>

/**
 * print_python_bytes_info - Prints basic info about a Python bytes object.
 * @p: Pointer to a PyObject representing the Python bytes object.
 *
 * This function prints information about the given Python bytes object, including
 * its size, data, and flags.
 *
 * Note: This function is designed to work with Python 3.4 and was compiled on
 *		 Ubuntu 14.04 LTS.
 */

void print_python_bytes_info(PyObject *p)
{
	Py_ssize_t size, i;
	char *data;
	unsigned char flags;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyBytesObject\n");
		return;
	}

	size = PyBytes_Size(p);
	data = PyBytes_AsString(p);
	flags = ((PyBytesObject *)p)->ob_sval[size];

	printf("[.] bytes object info\n");
	printf("  Size: %ld\n", size);
	printf("  Address of the first byte: %p\n", (void *)data);
	printf("  Bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)data[i]);
		if (i + 1 < size && i + 1 < 10)
			printf(" ");
	}
	printf("\n");
	printf("  First %ld bytes: ", size < 10 ? size : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		if (data[i] >= 0x20 && data[i] <= 0x7e)
			printf("%c", data[i]);
		else
			printf(".");
	}
	printf("\n");
	printf("  [");
	if (flags & 0x1)
		printf(" compactified");
	printf("]\n");
}
