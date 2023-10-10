#include <stddef.h>
#include <stdlib.h>
#include"lists.h"
/**
 * is_palindrome - check if the list is palindrome or not
 * @head: is a pointer
 * Return: 0 if the list isn't palindrome and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int count = 0, i, indcat = 0;
	int *ptr = NULL;
	listint_t *temp = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp != NULL)
	{
		temp = temp->next;
		count++;
	}
	ptr = malloc(sizeof(int) * count);
	if (ptr == NULL)
		return (0);
	temp = *head;
	count = 0;
	while (temp != NULL)
	{
		ptr[count] = temp->n;
		temp = temp->next;
		count++;
	}
	for (i = 0; i < (count / 2); i++)
	{
		if (ptr[i] != ptr[count - 1 - i])
		{
			indcat = 0;
			break;
		}
		else
			indcat = 1;
	}
	free(ptr);
	return (indcat);
}
