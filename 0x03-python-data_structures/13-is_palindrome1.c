#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * sorted singly linked list.
 * @head: pointer to adress of head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = (*head);
	int *array, nbr_nodes = 0, i, j;

	if (head == NULL || (*head) == NULL || tmp->next == NULL)
		return (1);
	for (nbr_nodes = 0; tmp; tmp = tmp->next)
		nbr_nodes++;

	array = (int *)malloc(sizeof(int) * nbr_nodes);
	if (array == NULL)
		exit(1);
	tmp = (*head);
	for (i = 0; tmp; i++, tmp = tmp->next)
		array[i] = tmp->n;

	for (i = 0, j = nbr_nodes - 1; i <= j; i++, j--)
		if (array[i] != array[j])
		{ free(array);
			return (0); }
	free(array);
	return (1);
}
