#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * size_of_list - returns size of list
 * @head: head of listint_t
 *
 * Return: int
 */
int size_of_list(listint_t **head)
{
	listint_t *ptr = *head;
	int i = 0;

	while (ptr)
	{
		ptr = ptr->next;
		i++;
	}
	return (i);
}


/**
 * get_n_by_idx - get n value using index
 * @head: head of listint_t
 * @idx: index
 *
 * Return: int
 */
int get_n_by_idx(listint_t **head, int idx)
{
	int i = 0;
	listint_t *ptr = *head;

	while (ptr)
	{
		if (i == idx)
			break;
		ptr = ptr->next;
		i++;
	}
	return (ptr->n);
}

/**
 * is_palindrome - checks if list is a palindrome
 * @head: head of listint_t
 *
 * Return: true (1) or false (0)
 */
int is_palindrome(listint_t **head)
{
	int start, end;

	start = 0;
	end = size_of_list(head) - 1;

	for (; start <= end; start++, end--)
	{
		if (get_n_by_idx(head, start) != get_n_by_idx(head, end))
			return (0);
	}
	return (1);
}
