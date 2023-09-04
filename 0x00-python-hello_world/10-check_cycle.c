#include "lists.h"

/**
 * check_cycle - that checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	const listint_t *adress[10] = {NULL};
	int i = 0;

	if (list == NULL)
		return (0);

	adress[0] = list;
	list = list->next;

	for (i = 1; list; list = list->next)
	{
		adress[i] = list;
		for (i = 0; adress[i]; i++)
			if (adress[i] == list)
				return (1);

	}
	return (0);
}
