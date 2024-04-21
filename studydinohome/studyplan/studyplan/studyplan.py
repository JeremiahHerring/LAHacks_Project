from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

pg_size = "300"
black = "rgba(0, 0, 0, 0.97)"
white = "rgba(255, 255, 255, 0.97)"

header1_style = { #sets font for header
    "font_family": "Arial Rounded MT Bold",
}

style1 = {
    "font_family": "Arial",
    rx.button: {
        "background_color": "#C3E3C3", #default CSS color: DarkSeaGreen
        "color": "black",
    },
}

# the removed astrick version should be passed through here 
def format_input(s: str) -> str:
    """Formats the given string to be formatted properly
    when displayed"""
    s = s.replace('*', '')
    each_line = s.split('\n')
    dupe_each_line = each_line.copy()
    
    # check for week # (if it's not week 1, then add '\n\n' to the start)
    for line in range(len(each_line)):
        curr_line = each_line[line]

        if len(curr_line.strip()) >= 4 and curr_line.strip()[0:4] == 'Week':
            week_num = curr_line.strip()[4:-1]
            if week_num != '' and int(week_num) != 1:
                dupe_each_line.insert(line, '\n\n')

    s = '\n'.join(dupe_each_line)

    return s


# list.insert(element, index) -- only updates curr list 
# ' '.join(list) -- convert a list into a string again

class State(rx.State):
    """The app state."""
    # include the given text

    test_str = """## Personalized Study Plan for Syntax Analysis 

Thank you for providing your syllabus and sharing your concerns about test anxiety and burnout. I understand that these challenges can significantly impact your academic performance and overall well-being. To address this, I've created a personalized study plan that considers the content of your "Syntax Analysis I" course and incorporates strategies to manage test anxiety and prevent burnout.

**Course Structure:**

It appears your course covers the fundamentals of syntax analysis, focusing on top-down parsing techniques. Key topics include:

*   **Grammar and Chomsky Hierarchy:** Understanding different grammar types and their classifications.
*   **Left Recursion and Backtracking:** Identifying and resolving issues that can arise during parsing.
*   **Top-Down Parsing Techniques:** Exploring methods like Recursive Descent Parsing (RDP), Predictive Recursive Descent Parsing (PRDP), and Table-Driven Predictive Parsing.

**Study Schedule:**

This schedule is designed to be flexible and adaptable to your individual needs. Please adjust the pace and workload as necessary, prioritizing your mental health and well-being.

**Week 1-2:**

*   **Focus:** Chapter 3.1 & 3.2 - Introduction and Grammar
*   **Activities:**
    *   Read the assigned textbook sections and lecture notes.
    *   Create flashcards for key terms like production, non-terminal symbols, terminal symbols, and BNF notation.
    *   Practice writing simple grammars in BNF notation.
    *   **Test Anxiety Tip:** Start practicing relaxation techniques like deep breathing or meditation to manage anxiety.

**Week 3-4:**

*   **Focus:** Chapter 3.3 - Chomsky Hierarchy
*   **Activities:**
    *   Understand the different types of grammars (Type 0 - 3) and their properties.
    *   Practice identifying the type of grammar based on given productions.
    *   Relate grammar types to their corresponding machine models (Turing Machine, LBA, PDA, FSM).
    *   **Burnout Prevention:** Schedule breaks between study sessions to avoid exhaustion. Engage in activities you enjoy to recharge.

**Week 5-6:**

*   **Focus:** Chapter 3.4 - Left Recursion and Backtracking
*   **Activities:**
    *   Learn how to identify and eliminate left recursion in grammars.    
    *   Understand the concept of backtracking and its implications for parsing.
    *   Practice applying left factorization to resolve backtracking issues.
    *   **Test Anxiety Tip:** Start working on practice problems and past exams to familiarize yourself with the format and build confidence.

**Week 7-8:**

*   **Focus:** Chapter 3.5 - Top-Down Parsers (RDP, PRDP, Table-Driven)    
*   **Activities:**
    *   Understand the working principles of RDP, PRDP, and Table-Driven parsers.
    *   Learn how to construct parsing tables and implement predictive parsing techniques.
    *   Practice implementing simple parsers for given grammars.
    *   **Burnout Prevention:** Connect with classmates or join study groups for support and motivation.

**Week 9-10:**

*   **Focus:** Review and Exam Preparation
*   **Activities:**
    *   Review all course materials, focusing on areas where you need additional practice.
    *   Work on practice problems and past exams to reinforce your understanding.
    *   Seek clarification from your professor or teaching assistants if needed.
    *   **Test Anxiety Tip:** Practice positive self-talk and visualize success in your exams.

**Additional Tips:**

*   **Break down tasks into smaller, manageable steps.** This can make studying feel less overwhelming and help you stay focused.
*   **Set realistic goals and celebrate your achievements.** This will help you stay motivated and build confidence.
*   **Prioritize sleep and healthy eating habits.** Taking care of your physical health can improve your mental well-being and cognitive function.    
*   **Seek professional help if needed.** If your test anxiety or burnout feels unmanageable, consider talking to a therapist or counselor.

**Remember, your mental health is just as important as your academic success. Be kind to yourself and seek help when needed. I believe in you!**     """
    ai_plan: str = format_input(test_str).replace('\n', '\n\n')

def navigation():
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.image(src="/dino_trans.png", width="50px"),
                    rx.heading(rx.text.em("studydino"), " | merging AI and mental health", size = "5",
                               style=header1_style, color=rx.color_mode_cond(black, white)
                    ),
                    align="center",
                ),
                href="/",
            ),
            rx.spacer(width="100%"),
            #menu here
            rx.color_mode.button(rx.color_mode.icon(), size="3", float="right", color=rx.color_mode_cond(black, white), background_color=rx.color_mode_cond("#C3E3C3", "#568356")),
            bg=rx.color_mode_cond(white, black),
            align="center",
            justify="center",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="10em",
            padding="1.5em",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
        height="50px",
    )

def index() -> rx.Component:
    return rx.center(
        navigation(),
        rx.vstack(
            rx.heading("Your custom ", rx.text.em("studydino"), " study plan", size="8", style=header1_style),
            rx.box(
                rx.container(
                    rx.markdown(State.ai_plan, padding='50px 25px', align='center', position="center"),
                ),
                size="4",
                border=f"1px dotted {rx.color_mode_cond(black, white)}",
                border_radius="25px",
                background_color=rx.color_mode_cond(white, black),
                padding="5em",
                align="center",
                width="85%",    
            ),   
            align="center",
            spacing="5",
            font_size="1.5em",
            height="260vh",
        ),
        padding="1em",
        height=pg_size + "vh",
        background=rx.color_mode_cond(
            "radial-gradient(circle at 22% 11%,rgba(229, 255, 231,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(253, 251, 230,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(255, 227, 237, 0.8),hsla(0,0%,100%,0) 40%)",
            "radial-gradient(circle at 22% 11%,rgba(124, 147, 124,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(187, 184, 159,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(221, 203, 209, 0.8),hsla(0,0%,100%,0) 40%)"
        ), 
    )


app = rx.App()
app.add_page(index)