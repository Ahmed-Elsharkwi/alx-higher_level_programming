#include"lists.h"
/**
 * insert_node - insert a new node inside the list
 * @head: is a pointer
 * @number: is an int
 * Return: the address of a new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *temp = *head;

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	while ((new->n > temp->n) && (temp->next != NULL) && (new->n > temp->next->n))
	{
		temp = temp->next;
	}
	if (temp == *head)
	{
		new->next = *head;
		*head = new;
	}
	else if (temp != *head && temp->next == NULL)
	{
		temp->next = new;
		new->next = NULL;
	}
	else
	{
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
