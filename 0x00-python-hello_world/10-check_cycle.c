#include"lists.h"
/**
 * check_cycle: check if the list has a cycle or not
 * @list: is a pointer
 * Return: 0 if that list has not any cycle or 1 if it has
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	fast = list;
	slow = list;
	while(fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
