import ngspicehlp as ng

dummy_text1 = "line one\nline two"
ng.print_section("My Dummy Text", dummy_text1)

dummy_title = "My Dummy Text"
line_one = "line one"
line_two = "line two"
dummy_text = f"{line_one}\n{line_two}"
# ng.print_section("My Dummy Text", dummy_text)
line_title = f"--- {dummy_title} ---"
last_line = "---------------------"

expected = f"{line_title}\n{dummy_text}\n{last_line}\n"
print(expected)
