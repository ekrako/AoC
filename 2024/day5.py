with open("input5.txt") as f:
    lines = f.readlines()
lines = "".join(lines)


def parse_input(input_text):
    rules, updates = input_text.strip().split("\n\n")

    # Parse rules into dict of dependencies
    rules = [tuple(map(int, rule.split("|"))) for rule in rules.strip().split("\n")]
    updates = [
        list(map(int, update.split(","))) for update in updates.strip().split("\n")
    ]

    return rules, updates


def is_valid_order(pages, rules):
    return not any(
        before in pages and after in pages and pages.index(before) > pages.index(after)
        for before, after in rules
    )


def part1(rules, updates):
    return sum(
        update[len(update) // 2] if is_valid_order(update, rules) else 0
        for update in updates
    )

def get_dependencies(rules, pages):
   # Build adjacency list for pages in current update
    # graph = {page: set() for page in pages}
    # indegree = {page: 0 for page in pages}
    # for before, after in rules:
    #     if before in pages and after in pages:
    #         graph[before].add(after)
    #         indegree[after] += 1
    graph = {page: {after for before, after in rules if before == page and after in pages} for page in pages}
    indegree = {
        page: sum(after == page and before in pages for before, after in rules)
        for page in pages
    }
    return graph, indegree

def topological_sort(rules, pages):
   graph, indegree = get_dependencies(rules, pages)
   queue = [page for page in pages if indegree[page] == 0]
   result = []
   
   while queue:
       node = min(queue)  # Use min for consistent ordering
       queue.remove(node)
       result.append(node)
       
       for neighbor in graph[node]:
           indegree[neighbor] -= 1
           if indegree[neighbor] == 0:
               queue.append(neighbor)
               
   return result if len(result) == len(pages) else None

def part2(rules, updates):
    return sum(
        topological_sort(rules, update)[len(topological_sort(rules, update)) // 2]
        for update in updates
        if not is_valid_order(update, rules)
    )


# Test with example input
example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

print(part1(*parse_input(example)))  # 143
print(part1(*parse_input(lines)))  # 4872
print(part2(*parse_input(example)))  # 123
print(part2(*parse_input(lines)))  # 5564

