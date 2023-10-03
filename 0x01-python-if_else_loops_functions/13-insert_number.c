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
	while((new->n > temp->n) && (new->n > temp->next->n))
	{
		/*pointer = temp;*/
		temp = temp->next;
	}
	/*pointer->next = new;*/
	
	new->next = temp->next;
	temp->next = new;
	return (new);
}
