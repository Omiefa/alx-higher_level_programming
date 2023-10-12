#include "lists.h"

/**
 * print_listint- prints all the elements of a listint_t list
 * @h: pointer to a list
 * Return: the number of nodes printed
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *temp = h;

	while (temp != NULL)
	{
		printf("%d\n", temp->n);
		count++;
		temp = temp->next;
	}
	return (count);
}