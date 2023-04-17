def study_schedule(permanence_period, target_time):
    if type(target_time) == str or not target_time:
        return None
    score = 0

    for tuple in permanence_period:
        if None in tuple or type(tuple[0]) == str or type(tuple[1]) == str:
            return None
        if target_time >= tuple[0] and target_time <= tuple[1]:
            score += 1
    return score
