def solution(numbers, target):
    super = [0]
    for n in numbers:
        sub_node = []
        for sup in super:
            sub_node.append(sup+n)
            sub_node.append(sup-n)
        super=sub_node
    return super.count(target)
  
