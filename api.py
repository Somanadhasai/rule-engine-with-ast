from ast import Node
def create_rule(rule_string):
    ast = parse_rule_string(rule_string)
    return ast
def combine_rules(rules):
    combined_ast = combine_asts(rules)
    return combined_ast
def evaluate_rule(ast, data):
    result = evaluate_ast(ast, data)
    return result
