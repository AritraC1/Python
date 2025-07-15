# Convert Roman to Integer numbers

def roman_to_int(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        
    result = 0
    prev_value = 0
        
    # Look at the letters from right to left
    for char in reversed(s):
        current_value = roman_map[char]
            
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
            
        prev_value = current_value
        
    return result


roman = input("Enter Roman number = ")
print(f"Integer of given roman number {roman} is", roman_to_int(roman))