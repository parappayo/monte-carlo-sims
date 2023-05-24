//
//  Build:
//      gcc roll.c -std=c99 -Wall -o roll
//

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

enum combat_result_t { DefenderLosesTwo, EachLosesOne, AttackerLosesTwo };

typedef unsigned int roll_t;

#define len(x) sizeof(x) / sizeof(roll_t)

void swap(roll_t dice[], size_t index1, size_t index2) {
	roll_t temp = dice[index1];
	dice[index1] = dice[index2];
	dice[index2] = temp;
}

void print_roll(const roll_t dice[], size_t dice_len) {
	if (dice_len == 3) {
		printf("(%d, %d, %d)", dice[0], dice[1], dice[2]);
		return;
	}
	if (dice_len == 2) {
		printf("(%d, %d)", dice[0], dice[1]);
		return;
	}
	printf("fatal error: print_roll called with unsupported len: %zu\n", dice_len);
	exit(1);
}

void init_roll(roll_t dice[], size_t dice_len) {
	for (size_t i = 0; i < dice_len; i++) {
		dice[i] = 1;
	}
}

bool is_valid_roll(roll_t dice[], size_t dice_len) {
	return dice[0] <= 6 && dice[1] <= 6 && (dice_len < 3 || dice[2] <= 6);
}

void next_roll(roll_t dice[], size_t dice_len) {
	size_t die_index = dice_len - 1;
	while (die_index > 0 && dice[die_index] == 6) {
		dice[die_index] = 1;
		die_index -= 1;
	}
	dice[die_index] += 1;
}

void sort_roll(roll_t dice[], size_t dice_len) {
	if (dice_len == 2) {
		if (dice[0] < dice[1]) {
			swap(dice, 0, 1);
		}
		return;
	}
	if (dice_len == 3) {
		if (dice[0] < dice[1]) {
			swap(dice, 0, 1);
		}
		if (dice[0] < dice[2]) {
			swap(dice, 0, 2);
		}
		if (dice[1] < dice[2]) {
			swap(dice, 1, 2);
		}
		return;
	}
	printf("fatal error: sort_roll called with unsupported len: %zu\n", dice_len);
	exit(1);
}

enum combat_result_t eval_combat_result(
	const roll_t attack_roll[3],
	const roll_t defend_roll[2]
) {
	roll_t attack_sorted[3], defend_sorted[2];
	attack_sorted[0] = attack_roll[0];
	attack_sorted[1] = attack_roll[1];
	attack_sorted[2] = attack_roll[2];
	defend_sorted[0] = defend_roll[0];
	defend_sorted[1] = defend_roll[1];

	sort_roll(attack_sorted, 3);
	sort_roll(defend_sorted, 2);

	const bool result1 = attack_sorted[0] > defend_sorted[0];
	const bool result2 = attack_sorted[1] > defend_sorted[1];

	if (result1 && result2) {
		return DefenderLosesTwo;
	}
	if (result1 || result2) {
		return EachLosesOne;
	}
	return AttackerLosesTwo;
}

int main(void) {
	unsigned int results[3];
	unsigned int iteration_count = 0;
	roll_t attack_roll[3];
	roll_t defend_roll[2];

	results[0] = 0;
	results[1] = 0;
	results[2] = 0;

	for (	init_roll(attack_roll, len(attack_roll));
			is_valid_roll(attack_roll, len(attack_roll));
			next_roll(attack_roll, len(attack_roll))) {

		for(	init_roll(defend_roll, len(defend_roll));
				is_valid_roll(defend_roll, len(defend_roll));
				next_roll(defend_roll, len(defend_roll))) {

			iteration_count += 1;
			enum combat_result_t result = eval_combat_result(
				attack_roll, defend_roll);
			results[result] += 1;
		}
	}

	printf("iteration_count = %d\n", iteration_count);
	printf("defender loses two = %d / %d = %f\n",
		results[DefenderLosesTwo],
		iteration_count,
		(float)results[DefenderLosesTwo] / (float)iteration_count);
	printf("each loses one = %d / %d = %f\n",
		results[EachLosesOne],
		iteration_count,
		(float)results[EachLosesOne] / (float)iteration_count);
	printf("attacker loses two = %d / %d = %f\n",
		results[AttackerLosesTwo],
		iteration_count,
		(float)results[AttackerLosesTwo] / (float)iteration_count);

	return 0;
}
