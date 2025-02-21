def snake_to_camel(snake_str):
    return "".join(word.capitalize() for word in snake_str.split("_"))

print(snake_to_camel("hello_world_____test"))