from os import system
system('cls')

def wrap_brackets(text):
  return "(" + text + ")"

def wrap_SquareBrackets(text):
  return "[" + text + "]"

def wrap_LessThan_GreaterThan(text):
  return "<" + text + ">"

print(wrap_LessThan_GreaterThan \
     (wrap_LessThan_GreaterThan \
     (wrap_LessThan_GreaterThan \
     (wrap_SquareBrackets \
     (wrap_SquareBrackets \
     (wrap_SquareBrackets \
     (wrap_brackets("12345"))))))))