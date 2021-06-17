def tree_by_levels(node):
    fringe = [node]
    result = []
    
    while fringe:
        current = fringe.pop(0)
        if not current:
            continue
        result.append(current.value)
        fringe.append(current.left)
        fringe.append(current.right)
    
    return result