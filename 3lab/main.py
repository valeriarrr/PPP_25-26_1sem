def recursion(new_line, results=[]):
    new_line = new_line.strip()

    if new_line.isdigit() or (new_line.startswith('-') and new_line[1:].isdigit()):
        results.append((new_line, int(new_line)))
        return int(new_line), results

    for i in range(len(new_line) - 1, -1, -1):
        char = new_line[i]
        if char == '+':
            left_part = new_line[:i]
            right_part = new_line[i+1:]
            left_result, results = recursion(left_part, results)
            right_result, results = recursion(right_part, results)
            result = left_result + right_result
            results.append((f'{left_part} + {right_part} = {result}'))
            return result, results
        elif char == '-':
            if i > 0:
                left_part = new_line[:i]
                right_part = new_line[i+1:]
                left_result, results = recursion(left_part, results)
                right_result, results = recursion(right_part, results)
                result = left_result - right_result
                results.append((f'{left_part} - {right_part} = {result}'))
                return result, results

    for i in range(len(new_line) - 1, -1, -1):
        char = new_line[i]
        if char == '*':
            left_part = new_line[:i]
            right_part = new_line[i+1:]
            left_result, results = recursion(left_part, results)
            right_result, results = recursion(right_part, results)
            result = left_result * right_result
            results.append((f'{left_part} * {right_part} = {result}'))
            return result, results
        elif char == '/':
            left_part = new_line[:i]
            right_part = new_line[i+1:]
            left_result, results = recursion(left_part, results)
            right_result, results = recursion(right_part, results)
            result = left_result / right_result
            results.append((f'{left_part} / {right_part} = {result}'))
            return result, results

result, results_list = recursion('10/5+2-1+14/2*1')
print(results_list)
