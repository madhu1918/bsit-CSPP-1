def lenRecur(s):
   if s == '':
      return 0
   else:
      return 1 + lenRecur(s[1:])