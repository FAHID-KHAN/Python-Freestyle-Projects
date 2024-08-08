class Madlib:
    def __init__(self,template,placeholders):
        self.template = template 
        self.placeholders = placeholders 
        self.user_inputs = {}
    def get_user_inputs(self):
        for placeholder in self.placeholders:
            user_input = input(f"Please enter a {placeholder}")
            self.user_inputs[placeholder] = user_input
    def construct_story(self):
        story = self.template.format(**self.user_inputs)
        return story
    
    
def main():
    
    template = "Once upon a time, there was a(n) {adjective} {noun} who loved to {verb}."
    placeholders = ["adjective", "noun", "verb"]


    madlib = Madlib(template, placeholders)

   
    madlib.get_user_inputs()

    # Construct and print the story
    story = madlib.construct_story()
    print("\nYour MadLib story:")
    print(story)

if __name__ == "__main__":
    main()