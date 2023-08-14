#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list
 *
 * @head: pointer to pointer to the head of the list
 *
 * Return: a pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	if (head == NULL || *head == NULL)
	{
		return (NULL);
	}

	while ((*head)->next != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	(*head)->next = prev;

	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to pointer to the head of the linked list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	if (!*head || (*head)->next)
	{
		return (0); /* Is palindrome */
	}

	/* Find the middle of the linked list using the hare and tortoise approach */
	listint_t *tortoise = *head;
	listint_t *hare = *head;

	while (hare->next && hare->next->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
	}

	/*Reverse the second half of the linked_list */
	listint_t *scnd_half_head = reverse_listint(&tortoise);

	/* Compare the 1st & 2nd halves for palindromicity */
	listint_t *current_1 = *head;
	listint_t *current_2 = scnd_half_head;

	while (current_2)
	{
		if (current_1->n != current_2->n)
		{
			return (1); /* Not palindrome */
		}
		current_1 = current_1->next;
		current_2 = current_2->next;
	}

	return (0);
}
