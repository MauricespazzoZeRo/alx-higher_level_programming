#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	tortoise = list;
	hare = list->next;

	while(hare && hare->next)
	{
		if (tortoise == hare)
		{
			return (1);
		}

		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0);
}
