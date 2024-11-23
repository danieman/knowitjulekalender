def parse_snow(code):
    stack = []
    for line in code:
        for char in line:
            if char == " ": stack.append(31)
            if char == ":": stack = [sum(stack)]
            if char == "|": stack.append(3)
            if char == "'": stack[-2] += stack[-1]; stack.pop()
            if char == ".": stack[-2], stack[-1] = stack[-1]-stack[-2], stack[-2]-stack[-1]
            if char == "_": stack[-2] *= stack[-1]
            if char == "/": stack.pop()
            if char == "i": stack.append(stack[-1])
            if char =="\\": stack[-1] += 1
            if char == "*": stack[-2] = int(stack[-1]/stack[-2]); stack.pop()
            if char == "~": stack[-3] = max(stack[-3:]); del stack[-2:]
            if char == "K": break
            if char == "[" and not stack[-1]%2: stack.pop()
            if char == "]": 
                if not stack[-1]%2:
                    stack[-1] = 1
                else:
                    stack.pop()
    return max(stack)

lines = open('input.spp').readlines()
print(parse_snow(lines))
