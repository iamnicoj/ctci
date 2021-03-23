def powerset(the_set):
    if the_set is None or len(the_set) == 0:
        return [{}]
    
    subsets = []

    if len(the_set) == 1:
        item = the_set.pop()
        subsets += [{item}]

    else:
        item = the_set.pop()
        subsets += [{item}]
        inner_subsets = powerset(the_set)
        for inner in inner_subsets:
            if len(inner) == 0:
                continue
            partial_set = set()
            partial_set.add(item)
            partial_set = partial_set.union(inner)
            subsets.append(partial_set)
        subsets += inner_subsets 
    return subsets


def example():
    print(powerset({}))
    print(powerset({1}))  # [{}, {1}]
    print(powerset({1, 2}))  # [{}, {1}, {2}, {1,2}]
    print(powerset({1, 2, 3}))  # [{}, {1}, {2}, {3}, {1,2}, {2, 3}, {1, 3}, {1, 2, 3}]

if __name__ == '__main__':
    example()