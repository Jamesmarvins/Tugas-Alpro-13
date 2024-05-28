def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    def check_palindrome(s, left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return check_palindrome(s, left + 1, right - 1)
    
    return check_palindrome(s, 0, len(s) - 1)

kalimat = "Nama saya andi saya umur 18"
if is_palindrome(kalimat):
    print(f'"{kalimat}" adalah palindrom.')
else:
    print(f'"{kalimat}" bukan palindrom.')