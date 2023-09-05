#include "lists.h"

/**
 * insert_node - function in C that inserts a number into a
 * sorted singly linked list.
 * @head: pointer to adress of head
 * @number : number to add to the linked_list
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = (*head), *new_node;

	if (head == NULL || (*head) == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (tmp->n > number)
	{
		new_node->next = (*head);
		(*head) = new_node;
		return (new_node);
	}

	for (; tmp->next; tmp = tmp->next)
	{
		if (tmp->next->n >= number)
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
			return (new_node);
		}
	}
	tmp->next = new_node;
	new_node->next = NULL;
	return (new_node);

	return (NULL);
}
