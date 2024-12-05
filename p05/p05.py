class Update:
    def __init__(self, update_line):
        self.pages = [int(n) for n in update_line.split(',')]

    def __repr__(self):
        return f"<Update: {self.pages}>"

    def middle(self):
        return self.pages[len(self.pages) // 2]

    def is_ordered(self, rules: list['Rule']):
        return all(rule.is_satisfied(self) for rule in rules)

    def order(self, rules: list['Rule']):
        while unsatisfied := next((r for r in rules if not r.is_satisfied(self)), None):
            i, j = (self.pages.index(unsatisfied.before),
                    self.pages.index(unsatisfied.after))
            self.pages[i], self.pages[j] = self.pages[j], self.pages[i]


class Rule:
    def __init__(self, rule_line):
        self.before, self.after = [int(n) for n in rule_line.split('|')]

    def __repr__(self):
        return f"<Rule: {self.before} before {self.after}>"

    def is_satisfied(self, update: Update):
        if self.before not in update.pages or self.after not in update.pages:
            return True

        return update.pages.index(self.before) <= update.pages.index(self.after)


def parse_rules_updates(raw_input):
    raw_rules, raw_updates = raw_input.split('\n\n')

    return ([Rule(raw) for raw in raw_rules.splitlines()],
            [Update(raw) for raw in raw_updates.splitlines()])


def solve_part_1(raw_input):
    rules, updates = parse_rules_updates(raw_input)
    correct_updates = filter(lambda u: u.is_ordered(rules), updates)
    middle_numbers = (update.middle() for update in correct_updates)
    return sum(middle_numbers)


def solve_part_2(raw_input):
    rules, updates = parse_rules_updates(raw_input)
    updates_to_correct = [u for u in updates if not u.is_ordered(rules)]
    for u in updates_to_correct:
        u.order(rules)
    middle_numbers = (update.middle() for update in updates_to_correct)
    return sum(middle_numbers)
