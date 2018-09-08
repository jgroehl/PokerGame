import numpy as np
import pokerlib.Evalutaor as Evaluator

def decide_on_victory(hand_evaluations):
    hand_evaluations = np.asarray(hand_evaluations)
    orig_indexes = np.argsort(hand_evaluations[:, 0])
    hand_evaluations = hand_evaluations[orig_indexes]

    indexes_in_question = np.where(hand_evaluations[:, 0] == np.max(hand_evaluations[:, 0]))[0]

    if np.prod(np.shape(indexes_in_question)) == 1:
        return orig_indexes[indexes_in_question]
    else:
        hand_evals = hand_evaluations[indexes_in_question]
        evaluation_value = hand_evals[0][0]

        if evaluation_value == Evaluator.ROYAL_FLUSH:
            #All royal flushes win
            return orig_indexes[indexes_in_question]

        elif evaluation_value == Evaluator.FLUSH:
            # All flushes win, where the 5 highest cards are all the same
            values = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[:, 1]])
            return_indexes_in_question = [i for i in range(len(values))]
            for i in range(5):
                new_indexes_in_question = np.where(values[:, i]
                                                   == np.max(values[return_indexes_in_question][:, i]))[0]
                return_indexes_in_question = np.intersect1d(return_indexes_in_question,
                                                            new_indexes_in_question)
                if np.prod(np.shape(return_indexes_in_question)) == 1:
                    return orig_indexes[indexes_in_question[return_indexes_in_question]]
            return orig_indexes[indexes_in_question[return_indexes_in_question]]

        elif evaluation_value == Evaluator.STRAIGHT or evaluation_value == Evaluator.STRAIGHT_FLUSH:
            # All straights with the same highest card win
            values = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[:, 1]])
            new_indexes_in_question = np.where(values[:, 0]
                                               == np.max(values[:, 0]))
            return orig_indexes[indexes_in_question[new_indexes_in_question]]

        elif evaluation_value == Evaluator.FULL_HOUSE:
            #The full house with the highest set or with the same set and highest pair wins
            values = [[value.value for value in hand] for hand in hand_evals[:, 1]]
            uniques_and_counts = np.asarray([np.unique(value, return_counts=True) for value in values])
            sets = [uniques_and_counts[i, 1] == 3 for i in range(len(uniques_and_counts))]
            sets = np.asarray([uniques_and_counts[i, 0][np.where(sets[i])] for i in range(len(uniques_and_counts))])
            max_sets = [np.max(sets[i]) for i in range(len(sets))]
            top_sets = np.asarray(np.where(max_sets == np.max(max_sets)))
            if np.prod(np.shape(top_sets)) == 1:
                return orig_indexes[indexes_in_question[top_sets[0]]]
            else:
                pairs = [uniques_and_counts[i, 1] == 2 | ((uniques_and_counts[i, 1] == 3) &
                                                          (uniques_and_counts[i, 0] != max_sets[i]))
                         for i in range(len(uniques_and_counts))]
                pairs = np.asarray(
                    [uniques_and_counts[i, 0][np.where(pairs[i])] for i in top_sets[0]])
                max_pairs = [np.max(pairs[i]) for i in range(len(pairs))]
                top_pairs = np.asarray(np.where(max_pairs == np.max(max_pairs)))
                return orig_indexes[indexes_in_question[top_sets[0][top_pairs[0]]]]

        elif evaluation_value == Evaluator.FOUR_OF_A_KIND:
            # The four of a kind with the highest value wins
            values = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[:, 1]])
            value_indexes = np.where(values[:, 0] == np.max(values[:, 0]))
            if np.prod(np.shape(value_indexes)) == 1:
                return orig_indexes[indexes_in_question[value_indexes[0]]]
            else:
                # The highest kicker wins
                kickers = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[value_indexes[0], 2]])
                kicker_indexes = np.where(kickers[:, 0] == np.max(kickers[:, 0]))
                kicker_indexes = np.intersect1d(value_indexes[0], kicker_indexes[0])
                return orig_indexes[indexes_in_question[kicker_indexes]]

        elif evaluation_value == Evaluator.THREE_OF_A_KIND:
            # The 3OAK with the highest value wins
            values = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[:, 1]])
            value_indexes = np.where(values[:, 0] == np.max(values[:, 0]))
            if np.prod(np.shape(value_indexes)) == 1:
                return orig_indexes[indexes_in_question[value_indexes[0]]]
            else:
                # The highest two kickers win
                kickers = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[value_indexes[0], 2]])
                return_indexes_in_question = np.copy(value_indexes[0])
                for i in range(2):
                    kicker_indexes_in_question = np.where(kickers[:, i]
                                                       == np.max(kickers[:, i]))[0]
                    return_indexes_in_question = np.intersect1d(return_indexes_in_question,
                                                                kicker_indexes_in_question)
                    if np.prod(np.shape(return_indexes_in_question)) == 1:
                        return orig_indexes[return_indexes_in_question]
                return orig_indexes[return_indexes_in_question]

        elif evaluation_value == Evaluator.TWO_PAIR:
            # The highest pair wins
            values = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[:, 1]])
            value_indexes = np.where(values[:, 0] == np.max(values[:, 0]))
            if np.prod(np.shape(value_indexes)) == 1:
                return orig_indexes[indexes_in_question[value_indexes[0]]]
            else:
                # The second highest pair wins
                values = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[value_indexes[0], 1]])
                value_indexes_second = np.where(values[:, 2] == np.max(values[:, 2]))
                if np.prod(np.shape(value_indexes_second)) == 1:
                    return orig_indexes[indexes_in_question[value_indexes[0][value_indexes_second]]]
                else:
                    # The highest kicker wins
                    kickers = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[value_indexes_second[0], 2]])
                    kicker_indexes = np.where(kickers[:, 0] == np.max(kickers[:, 0]))
                    kicker_indexes = np.intersect1d(value_indexes[0], kicker_indexes[0])
                    return orig_indexes[indexes_in_question[kicker_indexes]]

        elif evaluation_value == Evaluator.PAIR:
            # The 3OAK with the highest value wins
            values = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[:, 1]])
            value_indexes = np.where(values[:, 0] == np.max(values[:, 0]))
            if np.prod(np.shape(value_indexes)) == 1:
                return orig_indexes[indexes_in_question[value_indexes[0]]]
            else:
                # The highest three kickers win
                kickers = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[value_indexes[0], 2]])
                return_indexes_in_question = np.copy(value_indexes[0])
                for i in range(3):
                    kicker_indexes_in_question = np.where(kickers[:, i]
                                                       == np.max(kickers[:, i]))[0]
                    return_indexes_in_question = np.intersect1d(return_indexes_in_question,
                                                                kicker_indexes_in_question)
                    if np.prod(np.shape(return_indexes_in_question)) == 1:
                        return orig_indexes[return_indexes_in_question]
                return orig_indexes[return_indexes_in_question]

        elif evaluation_value == Evaluator.HIGH_CARD:
            # The highest 5 cards win
            kickers = np.asarray([[value.value for value in hand][::-1] for hand in hand_evals[:, 2]])
            return_indexes_in_question = np.copy(indexes_in_question)
            for i in range(5):
                new_indexes_in_question = np.where(kickers[:, i]
                                                   == np.max(kickers[return_indexes_in_question][:, i]))[0]
                return_indexes_in_question = np.intersect1d(return_indexes_in_question,
                                                            indexes_in_question[new_indexes_in_question])
                if np.prod(np.shape(return_indexes_in_question)) == 1:
                    return orig_indexes[return_indexes_in_question]
            return orig_indexes[return_indexes_in_question]

