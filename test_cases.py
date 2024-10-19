import unittest
from api import create_rule, combine_rules, evaluate_rule

class TestRuleEngine(unittest.TestCase):
    def test_create_rule(self):
        rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        ast = create_rule(rule_string)
        self.assertIsInstance(ast, Node)

    def test_combine_rules(self):
        rules = ["rule1", "rule2"]
        combined_ast = combine_rules(rules)
        self.assertIsInstance(combined_ast, Node)

    def test_evaluate_rule(self):
        ast = create_rule("age > 30")
        data = {"age": 35}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
